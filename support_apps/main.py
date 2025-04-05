import argparse
import json  # Import json for create_default_config
import logging
import os
import sys

# Import functions from converter module
# Assuming converter.py is in the same directory or Python path
try:
    from converter import load_diagram_config, process_markdown_file
except ImportError:
    # Log error using basic print since logger might not be set up yet
    print(
        "ERROR: Failed to import 'converter' module. Ensure converter.py is in the same directory or Python path.",
        file=sys.stderr,
    )
    sys.exit(1)


# --- Constants ---
# Define constants for filenames and defaults for clarity and easy modification
DEFAULT_CONFIG_FILENAME = "diagram_config.json"
DEFAULT_OUTPUT_SUFFIX = "-img"
LOG_FILENAME = "mermaid_converter.log"


# --- Logger Setup ---
def setup_logger():
    """
    Set up the root logger for command-line usage.
    Adds console and file handlers if they don't already exist.
    """
    # Get the root logger. Handlers added here will apply to logging.info etc.
    logger = logging.getLogger()

    # Set level only if not already configured (e.g., by basicConfig in converter)
    # Check current effective level if handlers exist, or just level if not.
    current_level = logger.getEffectiveLevel() if logger.hasHandlers() else logger.level
    if current_level == logging.NOTSET or current_level > logging.INFO:
        logger.setLevel(logging.INFO)  # Default level for CLI

    # Check if handlers of specific types are already present
    has_stream_handler = any(
        isinstance(h, logging.StreamHandler) for h in logger.handlers
    )
    # Check FileHandler by class and filename attribute if it exists
    has_file_handler = any(
        isinstance(h, logging.FileHandler)
        and hasattr(h, "baseFilename")
        and os.path.normpath(h.baseFilename) == os.path.normpath(LOG_FILENAME)
        for h in logger.handlers
    )

    log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Add Console Handler (if missing)
    if not has_stream_handler:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_formatter)
        # Set level for console handler (e.g., INFO)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
        # Use logging.debug for internal setup messages
        logging.debug("Added StreamHandler to logger.")

    # Add File Handler (if missing)
    if not has_file_handler:
        try:
            # Ensure log directory exists (optional, depends on desired behavior)
            # log_dir = os.path.dirname(LOG_FILENAME)
            # if log_dir and not os.path.exists(log_dir):
            #     os.makedirs(log_dir)

            file_handler = logging.FileHandler(
                LOG_FILENAME, encoding="utf-8", mode="a"
            )  # Append mode
            file_handler.setFormatter(log_formatter)
            # Set level for file handler (e.g., DEBUG for more detail in file)
            file_handler.setLevel(logging.DEBUG)
            logger.addHandler(file_handler)
            logging.debug(f"Added FileHandler ({LOG_FILENAME}) to logger.")
        except Exception as e:
            # Log error regarding file handler creation (will go to console if added)
            logging.error(f"Failed to create log file handler for {LOG_FILENAME}: {e}")


# --- Helper Functions ---
def create_default_config(output_path):
    """
    Create a default diagram configuration JSON file at the specified path.
    """
    # Define default configuration (Keep consistent with converter.py's defaults)
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

    abs_output_path = os.path.abspath(output_path)
    output_dir = os.path.dirname(abs_output_path)

    try:
        # Ensure the target directory exists
        if (
            output_dir
        ):  # Check if dirname is not empty (e.g., for relative paths in CWD)
            os.makedirs(output_dir, exist_ok=True)
            # --- FIX: Use logging.debug directly ---
            logging.debug(f"Ensured directory exists: {output_dir}")

        # Write the JSON file
        with open(abs_output_path, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=2)  # Use indent for readability
        # --- FIX: Use logging.info directly ---
        logging.info(
            f"Successfully created default configuration file: {abs_output_path}"
        )
        return True
    except OSError as dir_err:
        # --- FIX: Use logging.error directly ---
        logging.error(
            f"Failed to create directory for config file {abs_output_path}: {dir_err}"
        )
        return False
    except Exception as e:
        # --- FIX: Use logging.error directly ---
        logging.error(
            f"Error creating configuration file at {abs_output_path}: {str(e)}"
        )
        return False


# --- Main Execution Logic ---
def main():
    """Main entry point and argument parsing for the command-line interface."""
    # Set up logging as the first step
    setup_logger()
    logging.debug("Logger configured for CLI.")  # Use logging.debug here too

    # --- Argument Parser Setup ---
    parser = argparse.ArgumentParser(
        description="Convert Mermaid diagrams within Markdown files into linked images (SVG or PNG).",
        epilog=f"Example: python main.py report.md --format png --output-suffix -png",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,  # Shows default values in --help
    )

    # --- Define Arguments ---
    parser.add_argument(
        "file",
        nargs="?",  # File is optional only if --gui or --create-config is used
        metavar="MARKDOWN_FILE",
        help="Path to the input Markdown file (.md) to process.",
    )
    parser.add_argument(
        "--prefix",
        "-p",
        default="diagram",
        help="Prefix used for naming the generated image files.",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["svg", "png"],
        default="svg",
        help="Image format for the generated diagrams.",
    )
    parser.add_argument(
        "--image-dir",
        "-i",
        metavar="DIR",
        help="Custom directory path for saving generated images. Can be relative or absolute. "
        "Default: Creates an 'images' subdirectory next to the input file.",
    )
    parser.add_argument(
        "--config",
        "-c",
        default=DEFAULT_CONFIG_FILENAME,  # Use constant for default
        metavar="CONFIG_JSON",
        help="Path to a JSON file containing diagram styling/sizing configurations.",
    )
    # --- Output Suffix Argument ---
    parser.add_argument(
        "--output-suffix",
        "-s",
        default=DEFAULT_OUTPUT_SUFFIX,  # Use constant for default
        help="Suffix to append to the output markdown filename (inserted before the '.md' extension).",
    )
    # --- End Output Suffix Argument ---
    parser.add_argument(
        "--markdown-style",
        "-m",
        action="store_true",  # If present, value is True. Default: False.
        help="Use standard Markdown image syntax `![alt](path)` for links. "
        "Default is to use an HTML `<div><img>...</div>` wrapper (recommended for SVG styling).",
    )

    # --- Action Flags ---
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Launch the graphical user interface (GUI) instead of processing a file via CLI.",
    )
    parser.add_argument(
        "--create-config",
        metavar="OUTPUT_PATH",
        help=f"Create a default configuration file at the specified OUTPUT_PATH and exit. "
        f"If OUTPUT_PATH is omitted, defaults to '{DEFAULT_CONFIG_FILENAME}' in the current directory.",
        nargs="?",  # Makes the argument value optional
        const=DEFAULT_CONFIG_FILENAME,  # Value used if flag is present without a value
    )

    # --- Parse Arguments ---
    try:
        args = parser.parse_args()
        logging.debug(f"Parsed arguments: {args}")  # Use logging.debug
    except Exception as parse_err:
        # This typically shouldn't happen with argparse default handling
        logging.error(f"Error parsing arguments: {parse_err}")  # Use logging.error
        sys.exit(2)  # Use standard exit code for command line syntax errors

    # --- Handle Actions (Mutually Exclusive Recommended) ---

    # 1. Create Config Action
    if args.create_config is not None:  # Check if --create-config flag was used
        config_path_to_create = (
            args.create_config
        )  # Will be filename or None->const value
        logging.info(
            f"Action: Create default config requested at '{config_path_to_create}'"
        )  # Use logging.info
        success = create_default_config(config_path_to_create)
        sys.exit(0 if success else 1)  # Exit after attempting creation

    # 2. GUI Action
    if args.gui:
        # Ensure 'file' wasn't also provided if GUI is primary action
        if args.file:
            logging.warning(
                "Ignoring specified input file because --gui flag was used."
            )  # Use logging.warning
        logging.info("Action: Launching GUI...")  # Use logging.info
        try:
            # Attempt to import and run the GUI main function
            import tkinter  # Check if tkinter is available first

            # Ensure gui.py is in the path or same directory
            from gui import main as gui_main

            gui_main()  # This should block until the GUI is closed
            logging.info("GUI closed.")  # Use logging.info
            sys.exit(0)  # Exit cleanly after GUI closes
        except ImportError as import_err:
            logging.critical(
                f"GUI launch failed. Could not import required modules (tkinter or gui.py): {import_err}"
            )  # Use logging.critical
            logging.critical(
                "Ensure tkinter is installed (`python -m tkinter` should run) and gui.py is accessible."
            )  # Use logging.critical
            sys.exit(1)
        except Exception as gui_err:
            logging.critical(
                f"An unexpected error occurred while launching or running the GUI: {gui_err}"
            )  # Use logging.critical
            logging.exception("GUI Traceback:")  # Use logging.exception
            sys.exit(1)

    # 3. File Processing Action (Default if no other action)
    # Check if input file was provided (it's required if not --gui or --create-config)
    if not args.file:
        parser.error(
            "Input MARKDOWN_FILE is required for processing."
        )  # Use parser.error for standard handling

    input_file_path = args.file
    logging.info(
        f"Action: Processing input file '{input_file_path}' via CLI."
    )  # Use logging.info

    # --- Validate Input File ---
    abs_input_file_path = os.path.abspath(input_file_path)
    if not os.path.isfile(abs_input_file_path):
        logging.critical(
            f"Input file not found or is not a regular file: {abs_input_file_path}"
        )  # Use logging.critical
        sys.exit(1)
    if not abs_input_file_path.lower().endswith(".md"):
        logging.warning(
            f"Input file '{abs_input_file_path}' does not have a standard .md extension."
        )  # Use logging.warning

    # --- Load Diagram Configuration ---
    # load_diagram_config handles default path and non-existence warnings internally
    diagram_config = load_diagram_config(args.config)
    logging.debug(
        f"Using diagram configuration loaded from '{args.config}' (or defaults)."
    )  # Use logging.debug

    # --- Determine Image Directory ---
    # If specified, resolve path relative to CWD; otherwise, pass None to converter
    image_directory = args.image_dir
    if image_directory:
        image_directory = os.path.abspath(image_directory)  # Resolve to absolute path
        logging.info(
            f"Using specified image directory: {image_directory}"
        )  # Use logging.info
    else:
        logging.info(
            "Using default image directory ('images' subdir next to input file)."
        )  # Use logging.info

    # --- Execute File Processing ---
    logging.info("Calling process_markdown_file...")  # Use logging.info
    try:
        stats = process_markdown_file(
            file_path=abs_input_file_path,  # Pass absolute path
            image_prefix=args.prefix,
            image_format=args.format,
            image_dir=image_directory,  # Pass resolved absolute path or None
            diagram_config=diagram_config,
            use_html_wrapper=(not args.markdown_style),  # Note the inversion
            output_suffix=args.output_suffix,  # Pass the suffix argument
        )

        # --- Print Summary ---
        # Use print for final user output, logging for detailed info
        print("\n--- Conversion Summary ---")
        if stats:
            # Provide informative summary based on returned stats
            print(f"Input File:          {abs_input_file_path}")
            print(
                f"Output File:         {stats.get('output_file', 'N/A - Check logs')}"
            )
            print(f"Image Directory:     {stats.get('image_directory', 'N/A')}")
            print(f"Diagrams Found:      {stats.get('total_diagrams', 0)}")
            print(f"Successful Converts: {stats.get('successful_conversions', 0)}")
            print(f"Failed Converts:     {stats.get('failed_conversions', 0)}")

            # Determine exit code based on results
            if stats.get("failed_conversions", 0) > 0:
                print(
                    "\nWARNING: One or more diagrams failed to convert. See log file for details."
                )
                sys.exit(1)  # Exit with error code if any failures
            elif stats.get("total_diagrams", 0) == 0:
                print(
                    "\nProcessing complete. No Mermaid diagrams were found to convert."
                )
                sys.exit(0)  # Normal exit, but indicate nothing was converted
            elif stats.get("successful_conversions", 0) == stats.get(
                "total_diagrams", 0
            ):
                print("\nConversion completed successfully.")
                sys.exit(0)  # Success
            else:
                # Should be covered by failed>0 case, but as a fallback
                print("\nConversion finished with unexpected results (check counts).")
                sys.exit(1)
        else:
            # This case might occur if process_markdown_file had an early exit or error
            print(
                "\nProcessing did not complete successfully or returned no statistics. Check logs."
            )
            sys.exit(1)

    except Exception as proc_err:
        # Catch unexpected errors during the main processing call
        logging.critical(
            f"An unexpected error occurred during file processing: {proc_err}"
        )  # Use logging.critical
        logging.exception("Processing Traceback:")  # Use logging.exception
        sys.exit(1)


# --- Script Execution Guard ---
if __name__ == "__main__":
    main()
