import json  # For creating default config
import logging
import os
import queue
import sys
import threading
import tkinter as tk
from tkinter import (
    filedialog,
    messagebox,  # Import messagebox explicitly
    scrolledtext,
    ttk,
)

# Attempt to import converter module components
try:
    from converter import load_diagram_config, process_markdown_file
except ImportError:
    # Handle import error gracefully, perhaps show in GUI later
    print(
        "ERROR: Failed to import 'converter' module. Ensure converter.py is accessible.",
        file=sys.stderr,
    )
    # Set functions to None so checks later can detect the failure
    load_diagram_config = None
    process_markdown_file = None

# --- Constants ---
DEFAULT_OUTPUT_SUFFIX = "-img"
DEFAULT_CONFIG_FILENAME = "diagram_config.json"
APP_TITLE = "Mermaid Markdown Converter"

# --- Logging Setup for GUI ---
log_queue = queue.Queue()  # Queue for thread-safe logging from background tasks
logger = logging.getLogger()  # Get the root logger


class QueueHandler(logging.Handler):
    """Custom logging handler that puts records into a Queue."""

    def __init__(self, log_queue_instance):
        super().__init__()
        self.log_queue = log_queue_instance
        # Optional: Set a basic formatter if none is provided later
        self.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

    def emit(self, record):
        """Put the log record into the queue."""
        # Add the handler that should format this record (itself)
        # This allows the GUI thread to access the correct formatter later
        record.handler = self
        self.log_queue.put(record)


def setup_gui_logger():
    """
    Configure the root logger specifically for the GUI.
    Removes any existing handlers and adds a QueueHandler.
    """
    # Remove all handlers from the root logger to avoid conflicts/duplicates
    # Especially important if converter.py's basicConfig ran on import
    for handler in logger.handlers[:]:
        # Attempt to close handler before removing, especially file handlers
        try:
            handler.close()
        except Exception:
            pass  # Ignore errors during close
        logger.removeHandler(handler)

    # Add the queue handler for messages destined for the GUI log widget
    queue_handler = QueueHandler(log_queue)
    # Set a specific format for logs displayed in the GUI
    gui_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S"
    )
    queue_handler.setFormatter(gui_formatter)
    logger.addHandler(queue_handler)

    # Set the desired logging level for the application
    logger.setLevel(logging.INFO)  # Show INFO and above in GUI log
    logger.info("GUI Logger Initialized.")  # Log initialization message


def check_dependencies():
    """
    Check if the core mermaid-py dependency seems available and functional.
    Returns a list of missing/problematic dependencies (strings).
    """
    missing = []
    try:
        # Try importing core components
        import mermaid as md
        from mermaid.graph import Graph

        # Perform a very basic instantiation test
        test_graph = Graph("flowchart", "graph TD; A-->B;")
        _ = md.Mermaid(test_graph)  # Try creating the main Mermaid object

        # Optional: Add a more involved check if needed, e.g., a quick render
        # Be cautious of checks that might hang or require external processes

    except ImportError:
        missing.append("mermaid-py (package: python-mermaid) - Not found.")
    except Exception as e:
        # Catch other potential errors during basic mermaid-py initialization/use
        missing.append(f"mermaid-py - Error during basic test: {str(e)}")

    # Check if converter module failed to load earlier
    if process_markdown_file is None:
        missing.append("converter.py - Failed to load module.")

    return missing


# --- Main GUI Application Class ---
class MermaidConverterGUI:
    """Encapsulates the GUI application."""

    def __init__(self, root_window):
        """Initialize the GUI application."""
        self.root = root_window
        self.root.title(APP_TITLE)
        # Set initial size and minimum size
        self.root.geometry("850x650")  # Width x Height
        self.root.minsize(650, 500)

        # --- Theming ---
        self.style = ttk.Style()
        # Try available themes - 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'
        available_themes = self.style.theme_names()
        preferred_themes = [
            "clam",
            "vista",
            "xpnative",
            "alt",
            "default",
        ]  # Order of preference
        for theme in preferred_themes:
            if theme in available_themes:
                try:
                    self.style.theme_use(theme)
                    logger.debug(f"Using theme: {theme}")
                    break  # Use the first preferred theme found
                except tk.TclError:
                    logger.debug(f"Theme '{theme}' failed to apply, trying next.")
                    continue  # Theme might exist but fail to apply

        # Configure widget styles for consistency
        font_family = "Segoe UI"  # Or "Calibri", "Arial", etc.
        font_size = 10
        self.style.configure("TLabel", font=(font_family, font_size))
        self.style.configure("TButton", font=(font_family, font_size), padding=5)
        self.style.configure("TEntry", font=(font_family, font_size), padding=3)
        self.style.configure("TCombobox", font=(font_family, font_size))
        self.style.configure("TCheckbutton", font=(font_family, font_size))
        self.style.configure("TLabelframe.Label", font=(font_family, font_size, "bold"))
        self.style.configure(
            "Status.TLabel", font=(font_family, font_size - 1)
        )  # Smaller status font

        # --- Main Container Frame ---
        self.main_frame = ttk.Frame(root_window, padding="15")  # Padding around content
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Allow main row/column to expand
        # Row 3 (log frame) should expand vertically
        self.main_frame.rowconfigure(3, weight=1)
        # Column 0 (the only column used by pack) should expand horizontally
        self.main_frame.columnconfigure(0, weight=1)

        # --- Tkinter Variables (Model) ---
        self.file_path_var = tk.StringVar()
        self.image_prefix_var = tk.StringVar(value="diagram")
        self.image_format_var = tk.StringVar(value="svg")
        self.image_dir_var = tk.StringVar()  # Empty initially
        self.config_file_var = tk.StringVar(
            value=DEFAULT_CONFIG_FILENAME
        )  # Default config path
        self.output_suffix_var = tk.StringVar(
            value=DEFAULT_OUTPUT_SUFFIX
        )  # Variable for the suffix
        self.use_markdown_style_var = tk.BooleanVar(
            value=False
        )  # Default to HTML wrapper
        self.status_var = tk.StringVar(value="Ready.")
        self.is_processing = False  # Flag to prevent concurrent processing

        # --- Create UI Sections (View) ---
        # Pack frames vertically, allowing log frame to expand
        # Assign row numbers for clarity, though pack doesn't use them directly
        self.create_file_selection_frame().pack(fill=tk.X, pady=(0, 10))  # Row 0
        self.create_options_frame().pack(fill=tk.X, pady=(0, 10))  # Row 1
        self.create_action_buttons_frame().pack(fill=tk.X, pady=(5, 15))  # Row 2
        self.create_log_frame().pack(
            fill=tk.BOTH, expand=True, pady=(0, 10)
        )  # Row 3 (expands)
        self.create_status_bar().pack(side=tk.BOTTOM, fill=tk.X)  # Bottom

        # --- Initial Setup ---
        self.check_and_log_dependencies()  # Check dependencies after UI is built
        self.process_log_queue()  # Start the log queue monitor

    def check_and_log_dependencies(self):
        """Checks dependencies and logs messages to the GUI log."""
        missing_deps = check_dependencies()
        if missing_deps:
            logger.error("--- Dependency Issues Detected ---")
            for dep in missing_deps:
                logger.error(f"  - {dep}")
            logger.error("Conversion functionality may be limited or fail.")
            logger.error("See console/readme for installation instructions.")
            logger.error("------------------------------------")
            # Optionally show a warning messagebox
            messagebox.showwarning(
                "Dependency Warning",
                "Potential dependency issues detected:\n\n- "
                + "\n- ".join(missing_deps)
                + "\n\nPlease ensure required packages (like python-mermaid) and modules (converter.py) are installed/accessible correctly.",
            )
        else:
            logger.info("Dependency check passed.")

    # --- UI Creation Methods ---

    def create_file_selection_frame(self):
        """Create the frame for selecting the input Markdown file."""
        frame = ttk.LabelFrame(self.main_frame, text="Input File", padding="10")
        # Grid layout within this frame
        frame.columnconfigure(1, weight=1)  # Allow entry field to expand

        ttk.Label(frame, text="Markdown File:").grid(
            row=0, column=0, sticky=tk.W, padx=5, pady=5
        )
        entry = ttk.Entry(frame, textvariable=self.file_path_var, width=60)
        entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        button = ttk.Button(frame, text="Browse...", command=self.browse_file)
        button.grid(row=0, column=2, padx=(5, 0), pady=5)
        return frame

    def create_options_frame(self):
        """Create the frame for conversion options."""
        frame = ttk.LabelFrame(self.main_frame, text="Options", padding="10")
        # Grid layout within this frame
        frame.columnconfigure(
            1, weight=1
        )  # Allow first value column to expand slightly
        frame.columnconfigure(
            3, weight=1
        )  # Allow second value column to expand slightly

        # Row 0: Image Prefix & Format
        ttk.Label(frame, text="Image Prefix:").grid(
            row=0, column=0, sticky=tk.W, padx=5, pady=5
        )
        ttk.Entry(frame, textvariable=self.image_prefix_var, width=20).grid(
            row=0, column=1, padx=5, pady=5, sticky=tk.W
        )
        ttk.Label(frame, text="Image Format:").grid(
            row=0, column=2, sticky=tk.W, padx=(15, 5), pady=5
        )
        format_combo = ttk.Combobox(
            frame,
            textvariable=self.image_format_var,
            values=["svg", "png"],
            width=8,
            state="readonly",
        )
        format_combo.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        # Row 1 & 2: Image Directory
        ttk.Label(frame, text="Image Directory:").grid(
            row=1, column=0, sticky=tk.W, padx=5, pady=5
        )
        ttk.Entry(frame, textvariable=self.image_dir_var, width=50).grid(
            row=1, column=1, columnspan=2, padx=5, pady=5, sticky=tk.EW
        )
        ttk.Button(frame, text="Browse...", command=self.browse_directory).grid(
            row=1, column=3, padx=5, pady=5, sticky=tk.W
        )
        ttk.Label(
            frame, text="(Optional. Default: 'images/' subdir next to input file)"
        ).grid(row=2, column=1, columnspan=3, sticky=tk.W, padx=5, pady=(0, 5))

        # Row 3 & 4: Config File
        ttk.Label(frame, text="Config JSON:").grid(
            row=3, column=0, sticky=tk.W, padx=5, pady=5
        )
        ttk.Entry(frame, textvariable=self.config_file_var, width=50).grid(
            row=3, column=1, columnspan=2, padx=5, pady=5, sticky=tk.EW
        )
        ttk.Button(frame, text="Browse...", command=self.browse_config).grid(
            row=3, column=3, padx=5, pady=5, sticky=tk.W
        )
        config_button_frame = ttk.Frame(frame)  # Frame for config buttons
        config_button_frame.grid(
            row=4, column=1, columnspan=3, sticky=tk.W, padx=5, pady=(0, 5)
        )
        ttk.Button(
            config_button_frame,
            text="Create Default",
            command=self.create_default_config_file,
        ).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(
            config_button_frame, text="Edit", command=self.edit_config_file
        ).pack(side=tk.LEFT)

        # Row 5: Output Suffix (NEW WIDGET)
        ttk.Label(frame, text="Output Suffix:").grid(
            row=5, column=0, sticky=tk.W, padx=5, pady=5
        )
        ttk.Entry(frame, textvariable=self.output_suffix_var, width=15).grid(
            row=5, column=1, padx=5, pady=5, sticky=tk.W
        )
        ttk.Label(frame, text="(e.g., -svg, -png)").grid(
            row=5, column=2, columnspan=2, sticky=tk.W, padx=5, pady=5
        )

        # Row 6: Markdown Style Checkbox
        ttk.Checkbutton(
            frame,
            text="Use standard Markdown image syntax (![alt](path))",
            variable=self.use_markdown_style_var,
        ).grid(row=6, column=0, columnspan=4, sticky=tk.W, padx=5, pady=(10, 5))

        return frame

    def create_action_buttons_frame(self):
        """Create the frame for the main action button (Convert)."""
        frame = ttk.Frame(self.main_frame)  # No padding needed here, use button padding
        # Center the button using pack geometry manager within this frame
        convert_btn = ttk.Button(
            frame, text="Convert File", command=self.start_conversion, width=20
        )
        convert_btn.pack(pady=5)  # Add vertical padding around the button
        return frame

    def create_log_frame(self):
        """Create the frame for displaying log messages."""
        frame = ttk.LabelFrame(self.main_frame, text="Log Output", padding="10")
        # Configure grid weights for resizing within the log frame
        frame.rowconfigure(0, weight=1)  # Allow text widget row to expand
        frame.columnconfigure(0, weight=1)  # Allow text widget column to expand

        self.log_text = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            height=10,
            font=("Consolas", 9),  # Monospaced font for logs
            relief=tk.SUNKEN,
            borderwidth=1,
            state=tk.DISABLED,  # Start disabled
        )
        self.log_text.grid(row=0, column=0, sticky="nsew")  # Expand in all directions

        # Configure tags for log levels (adjust colors as desired)
        self.log_text.tag_configure("INFO", foreground="black")
        self.log_text.tag_configure("WARNING", foreground="#E69900")  # Dark orange
        self.log_text.tag_configure("ERROR", foreground="red")
        self.log_text.tag_configure(
            "CRITICAL", foreground="red", font=("Consolas", 9, "bold")
        )
        self.log_text.tag_configure("DEBUG", foreground="gray50")  # Darker gray

        return frame

    def create_status_bar(self):
        """Create the status bar at the bottom."""
        status_bar = ttk.Frame(
            self.root, relief=tk.GROOVE, padding=2
        )  # Use Groove for slight indent
        # Progress bar on the left
        self.progress = ttk.Progressbar(
            status_bar, orient=tk.HORIZONTAL, mode="indeterminate", length=150
        )
        self.progress.pack(side=tk.LEFT, padx=(5, 10), pady=2)
        # Status label expands to fill remaining space
        status_label = ttk.Label(
            status_bar, textvariable=self.status_var, style="Status.TLabel", anchor=tk.W
        )
        status_label.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=2)
        return status_bar

    # --- Event Handlers and Actions (Controller Logic) ---

    def browse_file(self):
        """Handle the 'Browse...' button click for the input file."""
        file_path = filedialog.askopenfilename(
            title="Select Markdown File",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
        )
        if file_path:
            self.file_path_var.set(file_path)
            logger.info(f"Input file selected: {file_path}")

    def browse_directory(self):
        """Handle the 'Browse...' button click for the image directory."""
        dir_path = filedialog.askdirectory(
            title="Select Custom Image Directory (Optional)"
        )
        if dir_path:
            self.image_dir_var.set(dir_path)
            logger.info(f"Custom image directory selected: {dir_path}")

    def browse_config(self):
        """Handle the 'Browse...' button click for the config file."""
        file_path = filedialog.askopenfilename(
            title="Select Configuration JSON File (Optional)",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )
        if file_path:
            self.config_file_var.set(file_path)
            logger.info(f"Configuration file selected: {file_path}")

    def create_default_config_file(self):
        """Handle the 'Create Default Config' button click."""
        # Use the helper function from main.py (or duplicate logic here)
        # For simplicity, duplicating the create logic:
        default_config = {  # Keep consistent with converter/main defaults
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
        file_path = filedialog.asksaveasfilename(
            title="Save Default Configuration File As...",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialfile=DEFAULT_CONFIG_FILENAME,
        )
        if file_path:
            try:
                abs_path = os.path.abspath(file_path)
                os.makedirs(
                    os.path.dirname(abs_path), exist_ok=True
                )  # Ensure dir exists
                with open(abs_path, "w", encoding="utf-8") as f:
                    json.dump(default_config, f, indent=2)
                self.config_file_var.set(abs_path)  # Update field to show saved path
                logger.info(f"Created default configuration file: {abs_path}")
                messagebox.showinfo(
                    "Success", f"Default configuration saved to:\n{abs_path}"
                )
            except Exception as e:
                logger.error(f"Error creating configuration file: {str(e)}")
                messagebox.showerror(
                    "Error", f"Could not save configuration file:\n{e}"
                )

    def edit_config_file(self):
        """Handle the 'Edit Config' button click."""
        config_path = self.config_file_var.get()
        if not config_path:
            logger.warning("Attempted to edit config, but no file path is set.")
            messagebox.showwarning(
                "Edit Config", "Please select or create a configuration file first."
            )
            return

        abs_config_path = os.path.abspath(config_path)
        if not os.path.isfile(abs_config_path):
            logger.error(
                f"Attempted to edit non-existent config file: {abs_config_path}"
            )
            messagebox.showerror(
                "Edit Config", f"Configuration file not found:\n{abs_config_path}"
            )
            return

        try:
            logger.info(f"Attempting to open '{abs_config_path}' in default editor...")
            # Platform-specific ways to open a file with default application
            if sys.platform.startswith("win"):
                os.startfile(abs_config_path)
            elif sys.platform.startswith("darwin"):  # macOS
                os.system(f'open "{abs_config_path}"')
            else:  # Linux and other POSIX
                os.system(f'xdg-open "{abs_config_path}"')
            logger.info(f"Issued command to open config file.")
        except Exception as e:
            logger.error(
                f"Error trying to open config file '{abs_config_path}': {str(e)}"
            )
            messagebox.showerror(
                "Error", f"Could not open configuration file in editor:\n{e}"
            )

    def log_message_to_gui(self, message, level=logging.INFO):
        """Safely add a message to the log text widget from the GUI thread."""
        if (
            not hasattr(self, "log_text") or not self.log_text.winfo_exists()
        ):  # Check if widget still exists
            print(f"Log widget destroyed, message not shown: {message}")
            return
        try:
            self.log_text.config(state=tk.NORMAL)  # Enable writing
            level_name = logging.getLevelName(level)  # Get level name (e.g., "INFO")
            # Insert message with the level name as a tag for coloring
            self.log_text.insert(tk.END, message + "\n", level_name)
            self.log_text.see(tk.END)  # Auto-scroll to the end
            self.log_text.config(state=tk.DISABLED)  # Disable writing
        except Exception as e:
            # Fallback if GUI logging fails unexpectedly
            print(
                f"GUI Log Error: {e}\nOriginal message ({logging.getLevelName(level)}): {message}"
            )

    def process_log_queue(self):
        """Periodically check the log queue and display messages in the GUI log widget."""
        try:
            while True:  # Process all messages currently in the queue
                record = log_queue.get_nowait()  # Get record without blocking
                # Format the log record using the handler's formatter
                # Access formatter via record.handler set in QueueHandler.emit
                if hasattr(record, "handler") and hasattr(record.handler, "formatter"):
                    formatted_msg = record.handler.formatter.format(record)
                else:
                    # Basic formatting if formatter is missing (should not happen)
                    formatted_msg = f"{record.levelname}: {record.getMessage()}"

                # Schedule the GUI update using root.after to ensure it runs in the main thread
                self.root.after(
                    0, self.log_message_to_gui, formatted_msg, record.levelno
                )
        except queue.Empty:
            # Queue is empty, do nothing this time
            pass
        except Exception as e:
            print(f"Error processing log queue: {e}")  # Log errors to console

        # Schedule the next check after a delay (e.g., 100ms)
        # Ensure root window still exists before scheduling next check
        if hasattr(self, "root") and self.root.winfo_exists():
            self.root.after(100, self.process_log_queue)

    def start_conversion(self):
        """Validate inputs and initiate the conversion process in a background thread."""
        if self.is_processing:
            logger.warning("Conversion already in progress. Ignoring request.")
            messagebox.showwarning("Busy", "A conversion process is already running.")
            return

        # --- Input Validation ---
        file_path = self.file_path_var.get()
        if not file_path:
            logger.error("Validation failed: Input file not selected.")
            messagebox.showerror("Input Error", "Please select an input Markdown file.")
            return
        abs_file_path = os.path.abspath(file_path)
        if not os.path.isfile(abs_file_path):
            logger.error(f"Validation failed: Input file not found at {abs_file_path}")
            messagebox.showerror(
                "Input Error", f"Input file not found:\n{abs_file_path}"
            )
            return

        # Check if converter module is loaded (critical dependency)
        if process_markdown_file is None:
            logger.critical("Cannot start conversion: converter module failed to load.")
            messagebox.showerror(
                "Critical Error",
                "Core conversion module (converter.py) could not be loaded.\nPlease check installation and restart.",
            )
            return

        # --- Prepare for Processing ---
        # Safely clear log widget
        try:
            self.log_text.config(state=tk.NORMAL)
            self.log_text.delete(1.0, tk.END)  # Clear previous log content
            self.log_text.config(state=tk.DISABLED)
        except tk.TclError:
            logger.warning("Log widget clearing failed (already destroyed?).")

        logger.info("=" * 25 + " Starting Conversion " + "=" * 25)  # Log separator

        self.progress.start(10)  # Start indeterminate progress animation
        self.status_var.set("Processing... Please wait.")
        self.is_processing = True  # Set processing flag

        # --- Gather Options ---
        image_prefix = self.image_prefix_var.get() or "diagram"  # Use default if empty
        image_format = (
            self.image_format_var.get()
        )  # Should always have a value from combobox
        image_dir_input = self.image_dir_var.get() or None  # Pass None if empty string
        config_path_input = (
            self.config_file_var.get() or None
        )  # Pass None if empty string
        use_html_wrapper = not self.use_markdown_style_var.get()  # Checkbox state
        output_suffix = (
            self.output_suffix_var.get() or DEFAULT_OUTPUT_SUFFIX
        )  # Use default if empty

        # Load diagram configuration (handle potential errors during load)
        diagram_config = load_diagram_config(
            config_path_input
        )  # Function handles None/errors

        # Resolve image directory path (make absolute if provided)
        abs_image_dir = None
        if image_dir_input:
            try:
                abs_image_dir = os.path.abspath(image_dir_input)
                logger.info(f"Resolved image directory to: {abs_image_dir}")
            except Exception as path_err:
                logger.error(
                    f"Could not resolve image directory path '{image_dir_input}': {path_err}"
                )
                messagebox.showerror(
                    "Path Error", f"Invalid image directory path:\n{image_dir_input}"
                )
                # Trigger failure cleanup in GUI
                self.conversion_failed("Invalid image directory path.")
                return  # Stop processing

        # --- Start Background Thread ---
        logger.info("Starting conversion in background thread...")
        conversion_thread = threading.Thread(
            target=self.run_conversion_thread,  # Target the wrapper method
            args=(  # Pass all necessary data to the thread
                abs_file_path,
                image_prefix,
                image_format,
                abs_image_dir,  # Pass resolved absolute path or None
                diagram_config,
                use_html_wrapper,
                output_suffix,
            ),
            daemon=True,  # Allows main app to exit even if thread hangs (use carefully)
        )
        conversion_thread.start()

    def run_conversion_thread(
        self,  # Arguments passed from start_conversion
        abs_file_path,
        image_prefix,
        image_format,
        abs_image_dir,
        diagram_config,
        use_html_wrapper,
        output_suffix,
    ):
        """
        The actual conversion logic that runs in the background thread.
        Calls the core processing function and schedules GUI updates.
        """
        logger.debug(f"Background thread started for {os.path.basename(abs_file_path)}")
        try:
            # --- Call Core Processing Function ---
            # Ensure process_markdown_file is available (checked in start_conversion, but double-check)
            if process_markdown_file is None:
                raise RuntimeError(
                    "process_markdown_file function not available (import failed)."
                )

            stats = process_markdown_file(
                file_path=abs_file_path,
                image_prefix=image_prefix,
                image_format=image_format,
                image_dir=abs_image_dir,  # Pass absolute path or None
                diagram_config=diagram_config,
                use_html_wrapper=use_html_wrapper,
                output_suffix=output_suffix,
            )
            logger.debug("process_markdown_file completed.")
            # --- Schedule Success Update ---
            # Use root.after(0, ...) to run conversion_completed in the main GUI thread
            if hasattr(self, "root") and self.root.winfo_exists():
                self.root.after(0, self.conversion_completed, stats)

        except Exception as e:
            # --- Handle Errors in Thread ---
            thread_error_msg = f"Error during conversion process: {str(e)}"
            logger.critical(thread_error_msg)  # Log critical error
            logger.exception("Conversion Thread Traceback:")  # Log full traceback
            # --- Schedule Failure Update ---
            # Use root.after(0, ...) to run conversion_failed in the main GUI thread
            if hasattr(self, "root") and self.root.winfo_exists():
                self.root.after(0, self.conversion_failed, thread_error_msg)

    def conversion_completed(self, stats):
        """Update the GUI after a successful conversion. Runs in the main GUI thread."""
        # Check if the root window still exists before updating UI
        if not hasattr(self, "root") or not self.root.winfo_exists():
            logger.warning("GUI window closed before conversion completion callback.")
            return

        logger.debug("Running conversion_completed callback.")
        self.progress.stop()
        self.is_processing = False  # Reset processing flag

        # Extract results from stats dictionary safely using .get()
        total = stats.get("total_diagrams", 0)
        success = stats.get("successful_conversions", 0)
        failed = stats.get("failed_conversions", 0)
        output_file = stats.get("output_file", "N/A")
        image_dir = stats.get("image_directory", "N/A")

        # Log detailed summary
        logger.info("=" * 25 + " Conversion Finished " + "=" * 25)
        summary = f"""
------------------- Conversion Summary -------------------
Input File:           {self.file_path_var.get()}
Output File:          {output_file}
Image Directory:      {image_dir}
Diagrams Found:       {total}
Successfully Converted: {success}
Failed Conversions:   {failed}
----------------------------------------------------------
"""
        logger.info(summary)  # Log summary details to file/console via logger

        # Update status bar and show messagebox
        if total == 0:
            final_status = "Finished. No diagrams found."
            messagebox.showinfo(
                "Complete",
                "Processing finished.\nNo Mermaid diagrams were found in the input file.",
            )
        elif failed > 0:
            final_status = f"Completed with {failed} errors."
            messagebox.showwarning(
                "Complete",
                f"Processing finished, but {failed} diagram(s) failed to convert.\nPlease check the log for details.",
            )
        else:
            final_status = "Conversion completed successfully!"
            messagebox.showinfo("Complete", "Conversion completed successfully!")

        self.status_var.set(final_status)

    def conversion_failed(self, error_message):
        """Update the GUI after a failed conversion. Runs in the main GUI thread."""
        # Check if the root window still exists before updating UI
        if not hasattr(self, "root") or not self.root.winfo_exists():
            logger.warning("GUI window closed before conversion failure callback.")
            return

        logger.debug("Running conversion_failed callback.")
        self.progress.stop()
        self.is_processing = False  # Reset processing flag
        self.status_var.set("Conversion failed!")
        logger.error("=" * 25 + " Conversion Failed! " + "=" * 25)

        # Display error message box to the user
        messagebox.showerror(
            "Conversion Failed",
            f"An error occurred during the conversion process:\n\n{error_message}\n\nPlease check the log output for more details.",
        )


# --- Main Application Entry Point ---
def main():
    """Sets up the logger and starts the Tkinter GUI application."""
    # Configure logging specifically for the GUI environment
    setup_gui_logger()

    # Create the main Tkinter window
    root = tk.Tk()

    # Create the application instance, passing the root window
    try:
        app = MermaidConverterGUI(root)
    except Exception as init_err:
        # Handle potential errors during GUI initialization
        logger.critical(f"Failed to initialize GUI: {init_err}")
        logger.exception("GUI Initialization Traceback:")
        # Attempt to show an error message if Tkinter is partially working
        try:
            # Ensure root exists before showing messagebox
            if root:
                messagebox.showerror(
                    "Initialization Error",
                    f"Failed to initialize the application GUI:\n\n{init_err}",
                )
        except Exception:
            print(
                f"CRITICAL: Failed to show GUI initialization error message box.",
                file=sys.stderr,
            )
        sys.exit(1)

    # Start the Tkinter event loop - this blocks until the window is closed
    try:
        root.mainloop()
    except KeyboardInterrupt:
        logger.info("Application interrupted by user (Ctrl+C).")
    except Exception as loop_err:
        logger.critical(f"An error occurred in the Tkinter main loop: {loop_err}")
        logger.exception("Main Loop Traceback:")
        sys.exit(1)

    logger.info("Application exiting.")


# --- Script Execution Guard ---
if __name__ == "__main__":
    # This block runs only when the script is executed directly
    main()
