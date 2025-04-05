import hashlib
import logging
import os
import re
import shutil
import time  # Import the time module
import traceback
from pathlib import Path

# --- Top Level Imports ---
try:
    import mermaid as md
    from mermaid.graph import Graph

    MERMAID_AVAILABLE = True
except ImportError:
    logging.critical(
        "Mermaid library (python-mermaid) not found. Conversion will fail."
    )
    MERMAID_AVAILABLE = False
# --- End Top Level Imports ---


# Configure logging (Consider moving to main entry points)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("mermaid_converter.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def extract_mermaid_blocks(markdown_content):
    """
    Extract Mermaid code blocks from markdown content.
    Returns a list of tuples (code_block, start_pos, end_pos)
    """
    pattern = r"```mermaid\s+(.*?)```"
    matches = []
    for match in re.finditer(pattern, markdown_content, re.DOTALL):
        block_text = match.group(1).strip()
        start_pos = match.start()
        end_pos = match.end()
        matches.append((block_text, start_pos, end_pos))
    return matches


def create_image_directory(markdown_path, image_dir=None):
    """
    Create a directory for the images next to the markdown file or use specified one.
    Returns the absolute path to the created/specified directory.
    """
    if image_dir:
        abs_image_dir = os.path.abspath(image_dir)
        os.makedirs(abs_image_dir, exist_ok=True)
        logger.info(f"Ensured specified image directory exists: {abs_image_dir}")
        return abs_image_dir
    else:
        markdown_abs_path = os.path.abspath(markdown_path)
        markdown_dir = os.path.dirname(markdown_abs_path)
        default_image_dir = os.path.join(markdown_dir, "images")
        os.makedirs(default_image_dir, exist_ok=True)
        logger.info(f"Ensured default image directory exists: {default_image_dir}")
        return default_image_dir


def _determine_diagram_type(mermaid_code):
    """Helper function to determine the diagram type from the first line."""
    if not mermaid_code:
        return "flowchart"
    first_line = mermaid_code.strip().split("\n", 1)[0].strip()
    type_map = {
        "sequenceDiagram": "sequence",
        "classDiagram": "classdiagram",
        "stateDiagram": "statediagram",
        "erDiagram": "erdiagram",
        "gantt": "gantt",
        "pie": "pie",
        "graph": "flowchart",
        "flowchart": "flowchart",
        "journey": "journey",
    }
    for keyword, diagram_type in type_map.items():
        if first_line.startswith(keyword):
            logger.debug(
                f"Detected diagram type '{diagram_type}' from line: {first_line}"
            )
            return diagram_type
    logger.warning(
        f"Could not determine diagram type from first line: '{first_line}'. Defaulting to 'flowchart'."
    )
    return "flowchart"


def generate_image_from_mermaid(
    mermaid_code, output_path, image_format="svg", diagram_config=None
):
    """
    Generate an image from Mermaid code using the mermaid-py library.
    Includes timing for Mermaid() instantiation and the core conversion call.
    Returns True if successful, False otherwise.
    """
    if not MERMAID_AVAILABLE:
        logger.error("Mermaid library not available. Cannot generate image.")
        return False

    try:
        # --- Step 1: Determine Type & Create Graph Object ---
        graph_start_time = time.time()
        diagram_type = _determine_diagram_type(mermaid_code)
        graph_obj = Graph(diagram_type, mermaid_code)
        graph_end_time = time.time()
        logger.debug(
            f"Graph object creation took {graph_end_time - graph_start_time:.4f} seconds."
        )

        # --- Step 2: Instantiate Mermaid Object (Suspected Bottleneck) ---
        mermaid_instance = None  # Initialize to None
        instantiation_start_time = time.time()
        try:
            mermaid_instance = md.Mermaid(graph_obj)
        except Exception as init_err:
            logger.error(f"Error instantiating Mermaid object: {init_err}")
            logger.error(traceback.format_exc())
            return False  # Cannot proceed if instantiation fails
        finally:
            instantiation_end_time = time.time()
            instantiation_duration = instantiation_end_time - instantiation_start_time
            logger.info(
                f"Mermaid object instantiation took {instantiation_duration:.2f} seconds."
            )

        # --- Step 3: Generate Output ---
        output_format = image_format.lower()
        render_start_time = time.time()
        generation_success = False

        try:
            if output_format == "svg":
                mermaid_instance.to_svg(output_path)
                generation_success = True
            elif output_format == "png":
                mermaid_instance.to_png(output_path)
                generation_success = True
            else:
                logger.error(f"Unsupported image format requested: {image_format}")
                return False
        except Exception as render_err:
            logger.error(
                f"Error during {output_format.upper()} generation: {render_err}"
            )
            generation_success = False
        finally:
            render_end_time = time.time()
            render_duration = render_end_time - render_start_time
            logger.info(
                f"Mermaid {output_format.upper()} generation call for {os.path.basename(output_path)} took {render_duration:.2f} seconds."
            )

        # --- Step 4: Verify Output & Cleanup ---
        if (
            generation_success
            and os.path.exists(output_path)
            and os.path.getsize(output_path) > 0
        ):
            logger.debug(f"Successfully generated image file: {output_path}")
            return True
        else:
            # Log failure reasons
            if not generation_success:
                logger.error(
                    f"Image generation failed due to rendering error for: {os.path.basename(output_path)}"
                )
            elif not os.path.exists(output_path):
                logger.error(
                    f"Image generation failed: Output file does not exist: {os.path.basename(output_path)}"
                )
            elif os.path.getsize(output_path) == 0:
                logger.error(
                    f"Image generation failed: Output file is empty: {os.path.basename(output_path)}"
                )
            else:
                logger.error(
                    f"Image generation failed for unknown reason: {os.path.basename(output_path)}"
                )

            # Clean up empty/failed file
            if os.path.exists(output_path):
                try:
                    os.remove(output_path)
                    logger.warning(
                        f"Removed empty/failed output file: {os.path.basename(output_path)}"
                    )
                except OSError as rm_err:
                    logger.error(
                        f"Failed to remove empty/failed output file {output_path}: {rm_err}"
                    )
            return False

    except Exception as e:
        logger.error(
            f"Unexpected error in generate_image_from_mermaid for {output_path}: {str(e)}"
        )
        logger.error(traceback.format_exc())
        return False


def create_image_name(prefix, index, mermaid_code, image_format="svg"):
    """Create a unique image filename."""
    code_hash = hashlib.md5(mermaid_code.encode("utf-8")).hexdigest()[:8]
    safe_prefix = re.sub(r"[^\w\-]+", "", prefix)
    filename = f"{safe_prefix}-{index}-{code_hash}.{image_format.lower()}"
    logger.debug(f"Generated image filename: {filename}")
    return filename


def process_markdown_file(
    file_path,
    image_prefix="diagram",
    image_format="svg",
    image_dir=None,
    diagram_config=None,
    use_html_wrapper=True,
    output_suffix="-img",
):
    """
    Processes a Markdown file: finds Mermaid blocks, converts them to images,
    updates the Markdown content with image links, and saves to a new file.
    Includes timing for the call to generate_image_from_mermaid.
    """
    if diagram_config is None:
        diagram_config = load_diagram_config()

    stats = {
        "total_diagrams": 0,
        "successful_conversions": 0,
        "failed_conversions": 0,
        "output_file": "",
        "image_directory": "",
    }

    try:
        abs_file_path = os.path.abspath(file_path)
        logger.info(f"Starting processing for file: {abs_file_path}")
        if not os.path.isfile(abs_file_path):
            logger.error(f"Input path is not a file or does not exist: {abs_file_path}")
            return stats

        try:
            with open(abs_file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as read_err:
            logger.error(f"Failed to read input file {abs_file_path}: {read_err}")
            return stats

        mermaid_blocks = extract_mermaid_blocks(content)
        stats["total_diagrams"] = len(mermaid_blocks)
        if not mermaid_blocks:
            logger.info(
                f"No Mermaid diagrams found in {abs_file_path}. No output file generated."
            )
            return stats
        logger.info(
            f"Found {len(mermaid_blocks)} Mermaid diagram(s) in {abs_file_path}"
        )

        abs_image_dir = create_image_directory(abs_file_path, image_dir)
        stats["image_directory"] = abs_image_dir
        logger.info(f"Using image directory: {abs_image_dir}")

        image_paths_info = []
        output_md_dir = os.path.dirname(abs_file_path)

        # --- Loop through diagrams ---
        total_loop_time = 0
        loop_start_time = time.time()

        for i, (block, _, _) in enumerate(mermaid_blocks):
            iter_start_time = time.time()  # Time start of this iteration
            logger.info(f"--- Processing Diagram {i+1}/{len(mermaid_blocks)} ---")
            image_name = create_image_name(image_prefix, i + 1, block, image_format)
            abs_image_path = os.path.join(abs_image_dir, image_name)

            # --- Timing the entire generation function call ---
            gen_func_start_time = time.time()
            success = generate_image_from_mermaid(block, abs_image_path, image_format)
            gen_func_end_time = time.time()
            gen_func_duration = gen_func_end_time - gen_func_start_time
            logger.info(
                f"Call to generate_image_from_mermaid for diagram {i+1} took {gen_func_duration:.2f} seconds."
            )
            # --- End timing generation function call ---

            if success:
                try:
                    rel_path = os.path.relpath(
                        abs_image_path, start=output_md_dir
                    ).replace("\\", "/")
                except ValueError:
                    logger.warning(
                        f"Cannot create relative path for image {abs_image_path} from {output_md_dir}. Using absolute URI path."
                    )
                    rel_path = Path(abs_image_path).as_uri()
                image_paths_info.append((rel_path, True))
                stats["successful_conversions"] += 1
            else:
                image_paths_info.append((None, False))
                stats["failed_conversions"] += 1

            iter_end_time = time.time()  # Time end of this iteration
            iter_duration = iter_end_time - iter_start_time
            total_loop_time += iter_duration
            logger.info(
                f"--- Finished Diagram {i+1}/{len(mermaid_blocks)} (Iteration took {iter_duration:.2f}s) ---"
            )

        loop_end_time = time.time()
        logger.info(
            f"Finished processing all diagrams. Total loop time: {total_loop_time:.2f}s. Average per diagram: {total_loop_time / len(mermaid_blocks) if mermaid_blocks else 0:.2f}s."
        )

        # --- Determine Output Filename ---
        abs_file_path_obj = Path(abs_file_path)
        output_file_name = f"{abs_file_path_obj.stem}{output_suffix}.md"
        abs_output_file = abs_file_path_obj.parent / output_file_name
        stats["output_file"] = str(abs_output_file)
        logger.info(f"Output Markdown file will be generated at: {abs_output_file}")

        # --- Replace Blocks ---
        replace_start_time = time.time()
        new_content, successful_replacements = replace_mermaid_with_images_enhanced(
            content, mermaid_blocks, image_paths_info, diagram_config, use_html_wrapper
        )
        replace_end_time = time.time()
        logger.info(
            f"Replacing blocks in content took {replace_end_time - replace_start_time:.2f} seconds."
        )

        if successful_replacements != stats["successful_conversions"]:
            logger.warning(
                f"Mismatch: {stats['successful_conversions']} successful conversions vs {successful_replacements} replacements."
            )

        # --- Write Output File ---
        write_start_time = time.time()
        try:
            with open(abs_output_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            logger.info(f"Successfully created output file: {abs_output_file}")
        except Exception as write_err:
            logger.error(f"Failed to write output file {abs_output_file}: {write_err}")
            return stats  # Return stats accumulated so far
        write_end_time = time.time()
        logger.info(
            f"Writing output file took {write_end_time - write_start_time:.2f} seconds."
        )

        logger.info(f"Processing complete for {abs_file_path}. Stats: {stats}")
        return stats

    except Exception as e:
        logger.error(
            f"An unexpected error occurred processing file {file_path}: {str(e)}"
        )
        logger.error(traceback.format_exc())
        stats["failed_conversions"] = stats.get("total_diagrams", 0) - stats.get(
            "successful_conversions", 0
        )
        return stats


def replace_mermaid_with_images_enhanced(
    markdown_content,
    mermaid_blocks,
    image_paths_info,
    diagram_config,
    use_html_wrapper=True,
):
    """
    Replace Mermaid code blocks with image references (HTML or Markdown syntax).
    """
    new_content = markdown_content
    offset = 0
    successful_replacements = 0

    for i, (block_text, start_pos, end_pos) in enumerate(mermaid_blocks):
        relative_image_path, success_flag = image_paths_info[i]
        adj_start = start_pos + offset
        adj_end = end_pos + offset
        replacement_text = ""

        if success_flag and relative_image_path:
            is_svg = relative_image_path.lower().endswith(".svg")
            diagram_type = _determine_diagram_type(block_text)
            config = diagram_config.get(diagram_type, diagram_config.get("default", {}))
            max_width = config.get("max_width", "600px")
            alt_text = f"Diagram: {diagram_type}"

            if use_html_wrapper and is_svg:
                replacement_text = f"""

<div style="max-width: {max_width}; margin: 1em auto; text-align: center;">
    <img src="{relative_image_path}" alt="{alt_text}" style="max-width: 100%; height: auto; display: block; margin: 0 auto;" />
</div>

"""
            else:
                replacement_text = f"\n\n![{alt_text}]({relative_image_path})\n\n"
            successful_replacements += 1
            # logger.debug(f"Replacing block {i+1} with image link: {relative_image_path}") # Reduce log noise
        else:
            # Ensure warning comment is added correctly even on failure
            warning_comment = "\n\n\n"
            original_block_text = f"```mermaid\n{block_text.strip()}\n```\n"
            replacement_text = warning_comment + original_block_text
            logger.warning(
                f"Keeping original code block {i+1} due to generation failure."
            )

        new_content = new_content[:adj_start] + replacement_text + new_content[adj_end:]
        offset += len(replacement_text) - (end_pos - start_pos)

    return new_content, successful_replacements


def load_diagram_config(config_path="diagram_config.json"):
    """
    Load diagram configuration from a JSON file.
    """
    default_config = {
        "default": {"max_width": "600px", "max_height": None, "min_width": None},
        "flowchart": {"max_width": "650px", "max_height": None, "min_width": "300px"},
        "sequence": {"max_width": "550px", "max_height": None, "min_width": "250px"},
        "classdiagram": {
            "max_width": "600px",
            "max_height": None,
            "min_width": "300px",
        },
        "statediagram": {
            "max_width": "550px",
            "max_height": None,
            "min_width": "250px",
        },
        "erdiagram": {"max_width": "700px", "max_height": None, "min_width": "400px"},
        "gantt": {"max_width": "800px", "max_height": None, "min_width": "500px"},
        "pie": {"max_width": "450px", "max_height": "450px", "min_width": "300px"},
    }
    path_to_check = config_path if config_path else "diagram_config.json"
    abs_path_to_check = os.path.abspath(path_to_check)

    if not os.path.isfile(abs_path_to_check):
        if config_path:
            logger.warning(
                f"Specified configuration file not found at {abs_path_to_check}. Using default configuration."
            )
        else:
            logger.info(
                f"Default configuration file '{path_to_check}' not found. Using default configuration."
            )
        return default_config

    try:
        import json

        with open(abs_path_to_check, "r", encoding="utf-8") as f:
            loaded_config = json.load(f)
            logger.info(f"Successfully loaded configuration from {abs_path_to_check}")

        final_config = default_config.copy()
        for diagram_type, settings in loaded_config.items():
            if diagram_type in final_config:
                if isinstance(settings, dict) and isinstance(
                    final_config[diagram_type], dict
                ):
                    final_config[diagram_type].update(settings)
                else:
                    final_config[diagram_type] = settings
            else:
                final_config[diagram_type] = settings
        if "default" not in final_config:
            final_config["default"] = default_config["default"]
        return final_config

    except json.JSONDecodeError as json_err:
        logger.error(
            f"Error decoding JSON from configuration file {abs_path_to_check}: {json_err}. Using default configuration."
        )
        return default_config
    except Exception as e:
        logger.error(
            f"An unexpected error occurred loading diagram config from {abs_path_to_check}: {e}. Using default configuration."
        )
        return default_config
