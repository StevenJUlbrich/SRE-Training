import hashlib
import logging
import os
import re
import shutil
import traceback
from pathlib import Path

# Configure logging
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
        block_text = match.group(1)
        start_pos = match.start()
        end_pos = match.end()
        matches.append((block_text, start_pos, end_pos))

    return matches


def modify_svg_dimensions(svg_path, max_width="600px", max_height=None, min_width=None):
    """
    Modify an SVG file to add width, height, and viewBox attributes while preserving layout.
    """
    try:
        # Read the SVG file
        with open(svg_path, "r", encoding="utf-8") as f:
            svg_content = f.read()

        import re

        # First, extract any existing viewBox, width, and height
        viewbox_match = re.search(r'viewBox=["\']([^"\']+)["\']', svg_content)
        width_match = re.search(r'width=["\']([^"\']+)["\']', svg_content)
        height_match = re.search(r'height=["\']([^"\']+)["\']', svg_content)

        # If we have a viewBox, we'll preserve it
        if viewbox_match:
            original_viewbox = viewbox_match.group(1)
        # If no viewBox but we have width and height, create one
        elif width_match and height_match:
            try:
                width_val = width_match.group(1)
                height_val = height_match.group(1)

                # Try to convert to numbers, stripping units
                width_num = float(re.sub(r"[^0-9.]", "", width_val))
                height_num = float(re.sub(r"[^0-9.]", "", height_val))

                original_viewbox = f"0 0 {width_num} {height_num}"
            except ValueError:
                original_viewbox = "0 0 1000 1000"  # Default if conversion fails
        else:
            # Default viewBox
            original_viewbox = "0 0 1000 1000"

        # Create a modified SVG by adding a wrapping svg element with our constraints
        # This preserves the original SVG's internal scaling while allowing us to constrain its display size
        modified_svg = f'<svg xmlns="http://www.w3.org/2000/svg" '

        if max_width:
            modified_svg += f'width="{max_width}" '

        if max_height:
            modified_svg += f'height="{max_height}" '
        else:
            modified_svg += 'height="auto" '

        # Add preserveAspectRatio to maintain proper scaling
        modified_svg += 'preserveAspectRatio="xMidYMid meet" '

        # Add style for min-width if provided
        if min_width:
            modified_svg += f'style="min-width: {min_width};" '

        # Add the viewBox using the original or calculated viewBox
        modified_svg += f'viewBox="{original_viewbox}">\n'

        # Add the original SVG content, removing the outer <svg> tags
        inner_content = re.sub(r"<svg[^>]*>", "", svg_content, count=1)
        inner_content = re.sub(r"</svg>\s*$", "", inner_content)
        modified_svg += inner_content + "\n</svg>"

        # Write the modified content back to the file
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(modified_svg)

        return True
    except Exception as e:
        logger.error(f"Error modifying SVG dimensions: {e}")
        return False


def create_image_directory(markdown_path, image_dir=None):
    """
    Create a directory for the images next to the markdown file.
    Returns the path to the created directory.
    """
    if image_dir:
        # Use specified directory if provided
        os.makedirs(image_dir, exist_ok=True)
        return image_dir

    # Create 'images' directory next to the markdown file
    markdown_dir = os.path.dirname(os.path.abspath(markdown_path))
    image_dir = os.path.join(markdown_dir, "images")
    os.makedirs(image_dir, exist_ok=True)

    return image_dir


def generate_image_from_mermaid(
    mermaid_code, output_path, image_format="svg", diagram_config=None
):
    """
    Generate an image from Mermaid code using mermaid-py.
    Returns True if successful, False otherwise.
    """
    try:
        # Import here to handle import errors gracefully
        import mermaid as md
        from mermaid.graph import Graph

        # Determine diagram type from the first line of the code
        first_line = mermaid_code.strip().split("\n")[0].strip()

        # Default to flowchart if we can't determine the type
        diagram_type = "flowchart"

        # Try to detect diagram type
        if first_line.startswith("sequenceDiagram"):
            diagram_type = "sequence"
        elif first_line.startswith("classDiagram"):
            diagram_type = "classdiagram"
        elif first_line.startswith("stateDiagram"):
            diagram_type = "statediagram"
        elif first_line.startswith("erDiagram"):
            diagram_type = "erdiagram"
        elif first_line.startswith("gantt"):
            diagram_type = "gantt"
        elif first_line.startswith("pie"):
            diagram_type = "pie"
        elif first_line.startswith("graph") or first_line.startswith("flowchart"):
            diagram_type = "flowchart"

        # Create the graph
        graph = Graph(diagram_type, mermaid_code)

        # Generate the image directly to file without modifying the SVG
        if image_format.lower() == "svg":
            md.Mermaid(graph).to_svg(output_path)
            # Skip SVG modification as it causes rendering issues
        else:
            md.Mermaid(graph).to_png(output_path)

        # Check if the image was created
        if os.path.exists(output_path):
            logger.info(f"Successfully generated image: {output_path}")
            return True
        else:
            logger.error(f"Failed to generate image: {output_path}")
            return False

    except Exception as e:
        logger.error(f"Error generating image: {str(e)}")
        logger.error(traceback.format_exc())
        return False


def create_image_name(prefix, index, mermaid_code, image_format="svg"):
    """
    Create a unique image name based on prefix, index and content hash.
    """
    # Create a short hash of the mermaid code
    code_hash = hashlib.md5(mermaid_code.encode()).hexdigest()[:8]
    return f"{prefix}-{index}-{code_hash}.{image_format}"


def replace_mermaid_with_images(
    markdown_content, mermaid_blocks, image_paths, max_width="600px"
):
    """
    Replace Mermaid code blocks with image references.
    Returns the updated markdown content and count of successful replacements.
    """
    new_content = markdown_content
    offset = 0  # Offset to adjust positions after replacements
    successful = 0

    for i, (block, start, end) in enumerate(mermaid_blocks):
        image_path = image_paths[i]

        # Calculate positions adjusted by the offset
        adj_start = start + offset
        adj_end = end + offset

        if image_path:
            # Create markdown image reference with style attribute
            image_ref = f'\n\n<img src="{image_path}" alt="Diagram" style="max-width: {max_width};">\n\n'

            # Replace the mermaid block with the image reference
            new_content = new_content[:adj_start] + image_ref + new_content[adj_end:]

            # Update the offset based on difference in length
            offset += len(image_ref) - (adj_end - adj_start)
            successful += 1
        else:
            # Add warning comment and keep original block
            warning = f"\n\n<!-- WARNING: Failed to generate diagram -->\n"
            orig_block = f"```mermaid\n{block}```"

            # Replace with warning + original
            replacement = warning + orig_block
            new_content = new_content[:adj_start] + replacement + new_content[adj_end:]

            # Update the offset
            offset += len(replacement) - (adj_end - adj_start)

    return new_content, successful


def process_markdown_file(
    file_path,
    image_prefix="diagram",
    image_format="svg",
    image_dir=None,
    diagram_config=None,
    use_html_wrapper=True,
):
    """
    Process a markdown file to convert Mermaid diagrams to images.

    Parameters:
    - file_path: Path to the markdown file
    - image_prefix: Prefix for generated image files
    - image_format: Format for the images (svg or png)
    - image_dir: Custom directory for images (default: ./images/)
    - diagram_config: Configuration for diagram dimensions by type
    - use_html_wrapper: Whether to use HTML wrapper (True) or standard Markdown image syntax (False)

    Returns:
    - Dictionary with statistics about the conversion
    """
    # If no diagram config is provided, use a default
    if diagram_config is None:
        diagram_config = {
            "default": {"max_width": "600px", "max_height": None, "min_width": None},
            "flowchart": {
                "max_width": "650px",
                "max_height": None,
                "min_width": "300px",
            },
            "sequence": {
                "max_width": "550px",
                "max_height": None,
                "min_width": "250px",
            },
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
            "erdiagram": {
                "max_width": "700px",
                "max_height": None,
                "min_width": "400px",
            },
            "gantt": {"max_width": "800px", "max_height": None, "min_width": "500px"},
            "pie": {"max_width": "450px", "max_height": "450px", "min_width": "300px"},
        }

    stats = {
        "total_diagrams": 0,
        "successful_conversions": 0,
        "failed_conversions": 0,
        "output_file": "",
        "image_directory": "",
    }

    try:
        # Verify the input file exists
        if not os.path.exists(file_path):
            logger.error(f"Input file does not exist: {file_path}")
            return stats

        # Read the markdown file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract Mermaid blocks
        mermaid_blocks = extract_mermaid_blocks(content)
        stats["total_diagrams"] = len(mermaid_blocks)

        if not mermaid_blocks:
            logger.info(f"No Mermaid diagrams found in {file_path}")
            return stats

        logger.info(f"Found {len(mermaid_blocks)} Mermaid diagrams in {file_path}")

        # Create the image directory
        image_dir = create_image_directory(file_path, image_dir)
        stats["image_directory"] = image_dir

        # Generate images for each Mermaid block
        image_paths = []
        for i, (block, _, _) in enumerate(mermaid_blocks):
            # Create image file name
            image_name = create_image_name(image_prefix, i + 1, block, image_format)
            image_path = os.path.join(image_dir, image_name)

            # Determine diagram type to apply appropriate configuration
            first_line = block.strip().split("\n")[0].strip()
            diagram_type = "flowchart"  # Default

            # Try to detect diagram type
            if first_line.startswith("sequenceDiagram"):
                diagram_type = "sequence"
            elif first_line.startswith("classDiagram"):
                diagram_type = "classdiagram"
            elif first_line.startswith("stateDiagram"):
                diagram_type = "statediagram"
            elif first_line.startswith("erDiagram"):
                diagram_type = "erdiagram"
            elif first_line.startswith("gantt"):
                diagram_type = "gantt"
            elif first_line.startswith("pie"):
                diagram_type = "pie"
            elif first_line.startswith("graph") or first_line.startswith("flowchart"):
                diagram_type = "flowchart"

            # Generate the image with the appropriate configuration
            success = generate_image_from_mermaid(
                block, image_path, image_format, diagram_config
            )

            if success:
                # Use relative path in the markdown
                rel_path = os.path.join("./images", image_name).replace("\\", "/")
                image_paths.append(rel_path)
                stats["successful_conversions"] += 1

                # If this is an SVG, we've already embedded dimensions, so update image_paths
                # to include information about whether dimensions are embedded
                if image_format.lower() == "svg":
                    image_paths[-1] = (
                        rel_path,
                        True,
                    )  # Tuple: (path, dimensions_embedded)
                else:
                    image_paths[-1] = (rel_path, False)
            else:
                image_paths.append(None)
                stats["failed_conversions"] += 1

        # Create the output file path
        output_file = file_path.replace(".md", "-img.md")
        if output_file == file_path:  # Handle case where input doesn't end with .md
            output_file = f"{file_path}-img.md"

        stats["output_file"] = output_file

        # Replace Mermaid blocks with image references
        new_content, successful = replace_mermaid_with_images_enhanced(
            content, mermaid_blocks, image_paths, diagram_config, use_html_wrapper
        )

        # Write the new content to the output file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(new_content)

        logger.info(f"Created output file: {output_file}")
        logger.info(f"Conversion stats: {stats}")

        return stats

    except Exception as e:
        logger.error(f"Error processing file {file_path}: {str(e)}")
        logger.error(traceback.format_exc())
        return stats


def replace_mermaid_with_images_enhanced(
    markdown_content, mermaid_blocks, image_paths, diagram_config, use_html_wrapper=True
):
    """
    Replace Mermaid code blocks with image references.
    Supports both standard Markdown syntax and HTML with configuration.
    """
    new_content = markdown_content
    offset = 0  # Offset to adjust positions after replacements
    successful = 0

    for i, (block, start, end) in enumerate(mermaid_blocks):
        image_path_info = image_paths[i]

        # Calculate positions adjusted by the offset
        adj_start = start + offset
        adj_end = end + offset

        if image_path_info:
            # Unpack the image path info
            if isinstance(image_path_info, tuple):
                image_path, dimensions_embedded = image_path_info
            else:
                # For backward compatibility
                image_path = image_path_info
                dimensions_embedded = False

            # Get the image format from the file extension
            is_svg = image_path.lower().endswith(".svg")

            # Determine what type of diagram this is
            first_line = block.strip().split("\n")[0].strip()
            diagram_type = "flowchart"  # Default

            if first_line.startswith("sequenceDiagram"):
                diagram_type = "sequence"
            elif first_line.startswith("classDiagram"):
                diagram_type = "classdiagram"
            elif first_line.startswith("stateDiagram"):
                diagram_type = "statediagram"
            elif first_line.startswith("erDiagram"):
                diagram_type = "erdiagram"
            elif first_line.startswith("gantt"):
                diagram_type = "gantt"
            elif first_line.startswith("pie"):
                diagram_type = "pie"
            elif first_line.startswith("graph") or first_line.startswith("flowchart"):
                diagram_type = "flowchart"

            # Get diagram-specific configuration
            config = (
                diagram_config.get(diagram_type, diagram_config.get("default", {}))
                if diagram_config
                else {"max_width": "600px"}
            )
            max_width = config.get("max_width", "600px")

            # Choose the appropriate image reference format
            if not use_html_wrapper or not is_svg:
                # Use standard Markdown image syntax for PNGs or if HTML wrapper is disabled
                image_ref = f"\n\n![Diagram]({image_path})\n\n"
            else:
                # For SVGs with HTML wrapper, use a div container
                image_ref = f"""
<div style="width: {max_width}; margin: 0 auto;">
    <img src="{image_path}" alt="Diagram" style="width: 100%; height: auto;" />
</div>
"""
            # Replace the mermaid block with the image reference
            new_content = new_content[:adj_start] + image_ref + new_content[adj_end:]

            # Update the offset based on difference in length
            offset += len(image_ref) - (adj_end - adj_start)
            successful += 1
        else:
            # Add warning comment and keep original block
            warning = f"\n\n<!-- WARNING: Failed to generate diagram -->\n"
            orig_block = f"```mermaid\n{block}```"

            # Replace with warning + original
            replacement = warning + orig_block
            new_content = new_content[:adj_start] + replacement + new_content[adj_end:]

            # Update the offset
            offset += len(replacement) - (adj_end - adj_start)

    return new_content, successful


def load_diagram_config(config_path=None):
    """
    Load diagram configuration from a JSON file or return the default configuration.

    Args:
        config_path: Path to the JSON configuration file (optional)

    Returns:
        dict: Configuration dictionary
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

    if not config_path or not os.path.exists(config_path):
        return default_config

    try:
        import json

        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        # Merge with defaults for any missing values
        for diagram_type, default_values in default_config.items():
            if diagram_type not in config:
                config[diagram_type] = default_values
            else:
                for key, value in default_values.items():
                    if key not in config[diagram_type]:
                        config[diagram_type][key] = value

        return config
    except Exception as e:
        logger.error(f"Error loading diagram config from {config_path}: {e}")
        return default_config
