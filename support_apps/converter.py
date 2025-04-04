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


def generate_image_from_mermaid(mermaid_code, output_path, image_format="svg"):
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

        # Generate the image directly to file
        if image_format.lower() == "svg":
            md.Mermaid(graph).to_svg(output_path)
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
    file_path, image_prefix="diagram", image_format="svg", image_dir=None
):
    """
    Process a markdown file to convert Mermaid diagrams to images.

    Parameters:
    - file_path: Path to the markdown file
    - image_prefix: Prefix for generated image files
    - image_format: Format for the images (svg or png)
    - image_dir: Custom directory for images (default: ./images/)

    Returns:
    - Dictionary with statistics about the conversion
    """
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

            # Generate the image
            success = generate_image_from_mermaid(block, image_path, image_format)

            if success:
                # Use relative path in the markdown
                rel_path = os.path.join("./images", image_name).replace("\\", "/")
                image_paths.append(rel_path)
                stats["successful_conversions"] += 1
            else:
                image_paths.append(None)
                stats["failed_conversions"] += 1

        # Create the output file path
        output_file = file_path.replace(".md", "-img.md")
        if output_file == file_path:  # Handle case where input doesn't end with .md
            output_file = f"{file_path}-img.md"

        stats["output_file"] = output_file

        # Replace Mermaid blocks with image references in a new file
        new_content, successful = replace_mermaid_with_images(
            content, mermaid_blocks, image_paths
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
