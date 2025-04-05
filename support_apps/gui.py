import logging
import os
import queue
import sys
import threading
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk

# Import the converter module
from converter import load_diagram_config, process_markdown_file

# Configure logging to use a queue handler for the GUI
log_queue = queue.Queue()
logger = logging.getLogger()


class QueueHandler(logging.Handler):
    """Handler that puts logs into a queue for the GUI"""

    def __init__(self, log_queue):
        logging.Handler.__init__(self)
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(record)


def setup_logger():
    """Configure the logger to use our queue handler"""
    # Remove all existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Add the queue handler
    queue_handler = QueueHandler(log_queue)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    queue_handler.setFormatter(formatter)
    logger.addHandler(queue_handler)
    logger.setLevel(logging.INFO)


def check_dependencies():
    """Check if required dependencies are installed"""
    missing = []
    try:
        import mermaid
        from mermaid.graph import Graph

        # Try a small test to confirm the render method works
        test_graph = Graph("flowchart", "graph TD\nA-->B")
        test_mermaid = mermaid.Mermaid(test_graph)
        test_mermaid.render()
    except ImportError:
        missing.append("mermaid-py")
    except Exception as e:
        # If there's an error initializing or using mermaid-py
        missing.append(f"mermaid-py (error: {str(e)})")

    return missing


class MermaidConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mermaid to Image Converter")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)

        # Configure styles
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 10))
        self.style.configure("TButton", font=("Arial", 10))

        # Create the main container
        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Variables
        self.file_path_var = tk.StringVar()
        self.image_prefix_var = tk.StringVar(value="diagram")
        self.image_format_var = tk.StringVar(value="svg")
        self.image_dir_var = tk.StringVar()
        self.config_file_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Ready")
        self.is_processing = False

        # Create the UI
        self.create_file_selection_frame()
        self.create_options_frame()
        self.create_log_frame()
        self.create_status_bar()

        # Set up periodic checks of the log queue
        self.process_log_queue()

        # Check dependencies
        missing_deps = check_dependencies()
        if missing_deps:
            self.log_text.insert(tk.END, "Missing dependencies detected:\n")
            for dep in missing_deps:
                self.log_text.insert(tk.END, f"  - {dep}\n")
            self.log_text.insert(tk.END, "Please install required packages with:\n")
            self.log_text.insert(tk.END, "pip install python-mermaid\n\n")

    def create_file_selection_frame(self):
        """Create the file selection section"""
        frame = ttk.LabelFrame(self.main_frame, text="Input File", padding=10)
        frame.pack(fill=tk.X, pady=5)

        ttk.Label(frame, text="Select Markdown File:").grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        ttk.Entry(frame, textvariable=self.file_path_var, width=50).grid(
            row=0, column=1, padx=5, pady=5, sticky=tk.EW
        )
        ttk.Button(frame, text="Browse...", command=self.browse_file).grid(
            row=0, column=2, padx=5, pady=5
        )

        frame.columnconfigure(1, weight=1)

    def create_options_frame(self):
        """Create the options section"""
        frame = ttk.LabelFrame(self.main_frame, text="Options", padding=10)
        frame.pack(fill=tk.X, pady=5)

        # Image prefix
        ttk.Label(frame, text="Image Prefix:").grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        ttk.Entry(frame, textvariable=self.image_prefix_var, width=20).grid(
            row=0, column=1, padx=5, pady=5, sticky=tk.W
        )

        # Image format
        ttk.Label(frame, text="Image Format:").grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        format_combo = ttk.Combobox(
            frame,
            textvariable=self.image_format_var,
            values=["svg", "png"],
            width=10,
            state="readonly",
        )
        format_combo.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Custom image directory
        ttk.Label(frame, text="Image Directory:").grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        ttk.Entry(frame, textvariable=self.image_dir_var, width=50).grid(
            row=2, column=1, padx=5, pady=5, sticky=tk.EW
        )
        ttk.Button(frame, text="Browse...", command=self.browse_directory).grid(
            row=2, column=2, padx=5, pady=5
        )
        ttk.Label(frame, text="(Leave empty for default './images/' directory)").grid(
            row=3, column=1, sticky=tk.W
        )

        # Configuration file
        ttk.Label(frame, text="Config JSON:").grid(row=4, column=0, sticky=tk.W, pady=5)
        ttk.Entry(frame, textvariable=self.config_file_var, width=50).grid(
            row=4, column=1, padx=5, pady=5, sticky=tk.EW
        )
        ttk.Button(frame, text="Browse...", command=self.browse_config).grid(
            row=4, column=2, padx=5, pady=5
        )
        ttk.Label(frame, text="(Optional: JSON configuration for diagram sizing)").grid(
            row=5, column=1, sticky=tk.W
        )

        # Add buttons for creating and editing config
        config_button_frame = ttk.Frame(frame)
        config_button_frame.grid(row=6, column=1, sticky=tk.W, pady=5)
        # Add a checkbox for using standard Markdown syntax
        self.use_markdown_style_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            frame,
            text="Use standard Markdown image syntax (![Diagram](path))",
            variable=self.use_markdown_style_var,
        ).grid(row=6, column=2, columnspan=3, sticky=tk.W, pady=5)

        ttk.Button(
            config_button_frame,
            text="Create Default Config",
            command=self.create_default_config,
        ).pack(side=tk.LEFT, padx=5)
        ttk.Button(
            config_button_frame, text="Edit Config", command=self.edit_config
        ).pack(side=tk.LEFT, padx=5)

        # Convert button
        convert_btn = ttk.Button(frame, text="Convert", command=self.start_conversion)
        convert_btn.grid(row=7, column=0, columnspan=3, pady=10)

        frame.columnconfigure(1, weight=1)

    def create_log_frame(self):
        """Create the log output section"""
        frame = ttk.LabelFrame(self.main_frame, text="Log", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, pady=5)

        # Create a scrolled text widget for logs
        self.log_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=10)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.log_text.config(state=tk.DISABLED)

    def create_status_bar(self):
        """Create the status bar"""
        status_bar = ttk.Frame(self.root)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Progress bar
        self.progress = ttk.Progressbar(
            status_bar, orient=tk.HORIZONTAL, mode="indeterminate"
        )
        self.progress.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=2)

        # Status label
        ttk.Label(status_bar, textvariable=self.status_var).pack(side=tk.RIGHT, padx=5)

    def browse_file(self):
        """Open file dialog to select a markdown file"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
        )
        if file_path:
            self.file_path_var.set(file_path)

            # Default image dir to same location as the file
            if not self.image_dir_var.get():
                default_dir = os.path.join(os.path.dirname(file_path), "images")
                self.image_dir_var.set(default_dir)

    def browse_directory(self):
        """Open directory dialog to select image directory"""
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.image_dir_var.set(dir_path)

    def browse_config(self):
        """Open file dialog to select a JSON configuration file"""
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            self.config_file_var.set(file_path)

    def create_default_config(self):
        """Create a default configuration file"""
        import json

        # Define default configuration
        default_config = {
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

        # Get save location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialfile="diagram_config.json",
        )

        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(default_config, f, indent=2)

                self.config_file_var.set(file_path)
                self.log_message(
                    f"Created default configuration file: {file_path}", logging.INFO
                )
            except Exception as e:
                self.log_message(
                    f"Error creating configuration file: {str(e)}", logging.ERROR
                )

    def edit_config(self):
        """Open the configuration file in the default editor"""
        config_path = self.config_file_var.get()

        if not config_path:
            self.log_message("No configuration file selected", logging.WARNING)
            return

        if not os.path.exists(config_path):
            self.log_message(
                f"Configuration file not found: {config_path}", logging.ERROR
            )
            return

        try:
            # Try to open the file with the default system editor
            if sys.platform == "win32":
                os.startfile(config_path)
            elif sys.platform == "darwin":  # macOS
                os.system(f'open "{config_path}"')
            else:  # Linux
                os.system(f'xdg-open "{config_path}"')

            self.log_message(
                f"Opened configuration file in editor: {config_path}", logging.INFO
            )
        except Exception as e:
            self.log_message(
                f"Error opening configuration file: {str(e)}", logging.ERROR
            )

    def log_message(self, message, level=logging.INFO):
        """Add a message to the log text widget"""
        tag = "info"
        if level == logging.ERROR:
            tag = "error"
        elif level == logging.WARNING:
            tag = "warning"

        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n", tag)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

        # Configure tags for different log levels
        self.log_text.tag_configure("error", foreground="red")
        self.log_text.tag_configure("warning", foreground="orange")
        self.log_text.tag_configure("info", foreground="black")

    def process_log_queue(self):
        """Check for logs in the queue and display them"""
        while True:
            try:
                record = log_queue.get_nowait()
                self.log_message(self.format_log_record(record), record.levelno)
            except queue.Empty:
                break

        # Schedule to check again soon
        self.root.after(100, self.process_log_queue)

    def format_log_record(self, record):
        """Format the log record for display"""
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        return formatter.format(record)

    def start_conversion(self):
        """Start the conversion process in a separate thread"""
        if self.is_processing:
            return

        file_path = self.file_path_var.get()
        if not file_path:
            self.log_message("Error: No input file selected", logging.ERROR)
            return

        if not os.path.exists(file_path):
            self.log_message(f"Error: File does not exist: {file_path}", logging.ERROR)
            return
        # Get the style option
        use_html_wrapper = not self.use_markdown_style_var.get()

        # Clear the log
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)

        # Start the progress bar
        self.progress.start(10)
        self.status_var.set("Processing...")
        self.is_processing = True

        # Get options
        image_prefix = self.image_prefix_var.get() or "diagram"
        image_format = self.image_format_var.get() or "svg"
        image_dir = self.image_dir_var.get() or None
        config_path = self.config_file_var.get() or None

        # Load diagram configuration if specified
        diagram_config = None
        if config_path:
            try:
                diagram_config = load_diagram_config(config_path)
                self.log_message(
                    f"Loaded configuration from: {config_path}", logging.INFO
                )
            except Exception as e:
                self.log_message(
                    f"Error loading configuration: {str(e)}", logging.ERROR
                )
                # Continue with default config

        # Run conversion in a separate thread
        threading.Thread(
            target=self.run_conversion,
            args=(
                file_path,
                image_prefix,
                image_format,
                image_dir,
                diagram_config,
                use_html_wrapper,
            ),
            daemon=True,
        ).start()

    def run_conversion(
        self,
        file_path,
        image_prefix,
        image_format,
        image_dir,
        diagram_config=None,
        use_html_wrapper=True,
    ):
        """Run the conversion process and update the UI when done"""
        try:
            stats = process_markdown_file(
                file_path,
                image_prefix,
                image_format,
                image_dir,
                diagram_config,
                use_html_wrapper,
            )

            # Update the UI from the main thread
            self.root.after(0, self.conversion_completed, stats)
        except Exception as e:
            # Log the error and update the UI
            logging.error(f"Conversion failed: {str(e)}")
            self.root.after(0, self.conversion_failed, str(e))

    def conversion_completed(self, stats):
        """Handle completion of the conversion process"""
        self.progress.stop()
        self.is_processing = False

        # Display summary
        total = stats["total_diagrams"]
        success = stats["successful_conversions"]
        failed = stats["failed_conversions"]

        if total == 0:
            self.status_var.set("No diagrams found")
            return

        success_rate = (success / total) * 100 if total > 0 else 0

        summary = f"""
Conversion completed!

Summary:
- Total diagrams found: {total}
- Successfully converted: {success}
- Failed conversions: {failed}
- Success rate: {success_rate:.1f}%

Output file: {stats["output_file"]}
Image directory: {stats["image_directory"]}
"""
        self.log_message(summary)

        if success == total:
            self.status_var.set("Conversion completed successfully")
        else:
            self.status_var.set(f"Conversion completed with {failed} failures")

    def conversion_failed(self, error_message):
        """Handle failure of the conversion process"""
        self.progress.stop()
        self.is_processing = False
        self.status_var.set("Conversion failed")

        self.log_message(f"Conversion failed: {error_message}", logging.ERROR)


def main():
    # Set up logging
    setup_logger()

    # Create the main window
    root = tk.Tk()
    app = MermaidConverterGUI(root)

    # Start the main loop
    root.mainloop()


if __name__ == "__main__":
    main()
