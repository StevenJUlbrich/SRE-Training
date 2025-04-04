import argparse
import logging
import os
import sys

from converter import process_markdown_file


def setup_logger():
    """Set up the logger for command-line usage"""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create console handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Create file handler
    file_handler = logging.FileHandler("mermaid_converter.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def main():
    """Main entry point for the command-line interface"""
    parser = argparse.ArgumentParser(
        description="Convert Mermaid diagrams in Markdown to images"
    )
    parser.add_argument("file", help="Path to the Markdown file")
    parser.add_argument(
        "--prefix", default="diagram", help="Prefix for image filenames"
    )
    parser.add_argument(
        "--format",
        choices=["svg", "png"],
        default="svg",
        help="Image format (svg or png)",
    )
    parser.add_argument("--image-dir", help="Custom directory for generated images")
    parser.add_argument("--gui", action="store_true", help="Launch the GUI")

    args = parser.parse_args()

    # Set up logging
    setup_logger()

    # Launch GUI if requested
    if args.gui:
        try:
            from gui import main as gui_main

            gui_main()
            return
        except ImportError as e:
            logging.error(f"Could not launch GUI: {str(e)}")
            sys.exit(1)

    # Process the file
    if not os.path.exists(args.file):
        logging.error(f"File not found: {args.file}")
        sys.exit(1)

    stats = process_markdown_file(args.file, args.prefix, args.format, args.image_dir)

    # Print summary
    print("\nConversion Summary:")
    print(f"Total diagrams found: {stats['total_diagrams']}")
    print(f"Successfully converted: {stats['successful_conversions']}")
    print(f"Failed conversions: {stats['failed_conversions']}")

    if stats["output_file"]:
        print(f"\nOutput file: {stats['output_file']}")
    if stats["image_directory"]:
        print(f"Image directory: {stats['image_directory']}")


if __name__ == "__main__":
    main()
