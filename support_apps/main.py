import argparse
import logging
import os
import sys

from converter import load_diagram_config, process_markdown_file


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


def create_default_config(output_path):
    """Create a default configuration file"""
    import json

    # Define default configuration
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

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=2)
        logging.info(f"Created default configuration file: {output_path}")
        return True
    except Exception as e:
        logging.error(f"Error creating configuration file: {str(e)}")
        return False


def main():
    """Main entry point for the command-line interface"""
    parser = argparse.ArgumentParser(
        description="Convert Mermaid diagrams in Markdown to images"
    )
    parser.add_argument("file", nargs="?", help="Path to the Markdown file")
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
    parser.add_argument("--config", help="Path to diagram configuration JSON file")
    parser.add_argument(
        "--create-config",
        metavar="FILE",
        help="Create a default configuration file at the specified path",
    )

    args = parser.parse_args()

    # Set up logging
    setup_logger()

    # Create default config if requested
    if args.create_config:
        success = create_default_config(args.create_config)
        sys.exit(0 if success else 1)

    # Launch GUI if requested
    if args.gui:
        try:
            from gui import main as gui_main

            gui_main()
            return
        except ImportError as e:
            logging.error(f"Could not launch GUI: {str(e)}")
            sys.exit(1)

    # Check if file is provided when not in GUI mode and not creating config
    if not args.file:
        logging.error(
            "No input file specified. Use --gui for GUI mode or specify a file."
        )
        parser.print_help()
        sys.exit(1)

    # Process the file
    if not os.path.exists(args.file):
        logging.error(f"File not found: {args.file}")
        sys.exit(1)

    # Load diagram configuration if specified
    diagram_config = None
    if args.config:
        diagram_config = load_diagram_config(args.config)
        logging.info(f"Loaded configuration from: {args.config}")

    stats = process_markdown_file(
        args.file, args.prefix, args.format, args.image_dir, diagram_config
    )

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
