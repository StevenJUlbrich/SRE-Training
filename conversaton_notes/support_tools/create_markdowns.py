import os


def create_markdown_files(num_files, template_name, target_dir):
    """
    Creates a specified number of empty Markdown files based on a template
    in a target directory.

    Args:
        num_files (int): The number of files to create.
        template_name (str): The template for the filename, containing '##'
                             as a placeholder for the file number.
                             Example: "chapter_##_scaffold_draft.md"
        target_dir (str): The directory where the files will be created.
                          It will be created if it doesn't exist.
    """
    # --- Input Validation ---
    if not isinstance(num_files, int) or num_files <= 0:
        print("Error: Number of files must be a positive integer.")
        return
    if "##" not in template_name:
        print("Error: Template name must contain '##' as a placeholder for the number.")
        return
    if not target_dir:
        print("Error: Target directory cannot be empty.")
        return

    try:
        # --- Create Target Directory if it Doesn't Exist ---
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"Created directory: {target_dir}")
        else:
            if not os.path.isdir(target_dir):
                print(f"Error: '{target_dir}' exists but is not a directory.")
                return
            print(f"Target directory: {target_dir}")

        # --- Generate Files ---
        print(f"\nGenerating {num_files} files...")
        for i in range(1, num_files + 1):
            # Format the number to be two digits (e.g., 1 -> "01", 10 -> "10")
            file_number_str = f"{i:02d}"

            # Replace the '##' placeholder in the template with the formatted number
            file_name = template_name.replace("##", file_number_str)

            # Construct the full path to the file
            file_path = os.path.join(target_dir, file_name)

            try:
                # Create an empty file
                with open(file_path, "w") as f:
                    # You can add default content here if needed, e.g.:
                    # f.write(f"# {template_name.replace('##', file_number_str).replace('.md', '')}\n")
                    pass  # Creates an empty file
                print(f"Successfully created: {file_path}")
            except IOError as e:
                print(f"Error creating file {file_path}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred while creating {file_path}: {e}")

        print("\nFile generation complete.")

    except OSError as e:
        print(f"Error related to directory operations: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("--- Markdown File Generator ---")

    while True:
        try:
            num_files_input = input("Enter the number of files to create: ")
            if not num_files_input:  # Handle empty input
                print("Input cannot be empty. Please enter a number.")
                continue
            num_files_to_create = int(num_files_input)
            if num_files_to_create <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    while True:
        file_template_input = input(
            "Enter the file template (e.g., chapter_##_scaffold_draft.md): "
        )
        if not file_template_input:  # Handle empty input
            print("Input cannot be empty. Please enter a template name.")
            continue
        if "##" not in file_template_input:
            print("Template name must contain '##'. Please try again.")
            continue
        if not file_template_input.endswith(".md"):
            add_md = input(
                f"The template '{file_template_input}' does not end with '.md'. Add it? (y/n): "
            ).lower()
            if add_md == "y":
                file_template_input += ".md"
        break

    while True:
        target_directory_input = input(
            "Enter the target directory (e.g., ./output_files or C:\\Users\\YourName\\Documents\\Drafts): "
        )
        if not target_directory_input:  # Handle empty input
            print("Input cannot be empty. Please enter a target directory.")
            continue
        break

    create_markdown_files(
        num_files_to_create, file_template_input, target_directory_input
    )
