#!/usr/bin/env python3
"""
CSV Filtering Script - Basic Scripting

This module provides functionality to filter rows in a CSV file based on a specified
column's value. The result is written to a new CSV file.

Key Concepts:
    - CSV file handling
    - Command-line argument parsing
    - File I/O with context managers
    - Error handling
    - User feedback

Learning Objectives:
    - Understand how to work with CSV files in Python
    - Learn to create command-line tools with argparse
    - Practice proper error handling techniques
    - Recognize the importance of user feedback in scripts
"""

import argparse
import csv
import os
import sys
from typing import Any, Dict, List, Union


def filter_csv(
    input_file: str, output_file: str, filter_column: str, filter_value: str
) -> int:
    """
    Filter rows of a CSV file based on a given column's matching value.

    Args:
        input_file: Path to the input CSV file
        output_file: Path to the output CSV file
        filter_column: Name of the column to filter on
        filter_value: Value to match in the filter column

    Returns:
        int: The number of matching rows written to the output file

    Raises:
        FileNotFoundError: If the input file does not exist
        ValueError: If the filter column does not exist in the CSV
        IOError: If there are issues reading or writing files
    """
    # Check if input file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    try:
        # Counter for matching rows
        matched_rows = 0

        with open(input_file, mode="r", newline="", encoding="utf-8") as infile, open(
            output_file, mode="w", newline="", encoding="utf-8"
        ) as outfile:

            # Create CSV readers and writers
            reader = csv.DictReader(infile)

            # Verify filter column exists
            if not reader.fieldnames or filter_column not in reader.fieldnames:
                raise ValueError(
                    f"Filter column '{filter_column}' not found in the CSV. "
                    f"Available columns: {', '.join(reader.fieldnames or [])}"
                )

            # Set up writer with the same fieldnames
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            # Process each row
            for row in reader:
                # Check if the row matches the filter
                if row[filter_column] == filter_value:
                    writer.writerow(row)
                    matched_rows += 1

        return matched_rows

    except csv.Error as e:
        raise IOError(f"CSV error: {e}")
    except IOError as e:
        raise IOError(f"I/O error: {e}")


def csv_preview(file_path: str, num_rows: int = 5) -> List[Dict[str, Any]]:
    """
    Preview the first few rows of a CSV file.

    Args:
        file_path: Path to the CSV file
        num_rows: Number of rows to preview (default: 5)

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the preview rows

    Raises:
        FileNotFoundError: If the file does not exist
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    preview_rows = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for i, row in enumerate(reader):
            if i >= num_rows:
                break
            preview_rows.append(row)

    return preview_rows


def display_csv_info(file_path: str) -> Dict[str, Union[int, List[str]]]:
    """
    Display information about a CSV file.

    Args:
        file_path: Path to the CSV file

    Returns:
        Dict: A dictionary containing information about the CSV file

    Raises:
        FileNotFoundError: If the file does not exist
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, [])

        # Count total rows
        row_count = sum(1 for _ in reader)

    return {
        "file_name": os.path.basename(file_path),
        "columns": header,
        "row_count": row_count,
    }


def parse_arguments():
    """
    Parse command-line arguments for the CSV filter script.

    Returns:
        argparse.Namespace: Parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description="Filter rows in a CSV file based on column values.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input_file", help="Path to the input CSV file")

    parser.add_argument("output_file", help="Path to the output CSV file")

    parser.add_argument("filter_column", help="Name of the column to filter on")

    parser.add_argument("filter_value", help="Value to match in the filter column")

    parser.add_argument(
        "--preview",
        type=int,
        default=0,
        help="Preview the specified number of rows from the result (0 to disable)",
    )

    return parser.parse_args()


def main():
    """Main function to run the CSV filter script."""
    args = parse_arguments()

    try:
        # Display input file information
        print("Input CSV Information:")
        info = display_csv_info(args.input_file)
        print(f"  File: {info['file_name']}")
        print(f"  Columns: {', '.join(info['columns'])}")
        print(f"  Total rows: {info['row_count']}")

        # Check if filter column is valid
        if args.filter_column not in info["columns"]:
            print(f"ERROR: Filter column '{args.filter_column}' not found in the CSV.")
            print(f"Available columns: {', '.join(info['columns'])}")
            return 1

        # Filter the CSV
        print(f"\nFiltering rows where {args.filter_column} = '{args.filter_value}'...")
        matched_rows = filter_csv(
            args.input_file, args.output_file, args.filter_column, args.filter_value
        )

        # Display result information
        print(f"Filter complete: {matched_rows} matching rows found.")
        print(f"Results saved to: {args.output_file}")

        # Preview the result if requested
        if args.preview > 0 and matched_rows > 0:
            print(f"\nPreview of first {min(args.preview, matched_rows)} result(s):")
            preview_rows = csv_preview(args.output_file, args.preview)

            for i, row in enumerate(preview_rows, 1):
                print(f"\nRow {i}:")
                for column, value in row.items():
                    print(f"  {column}: {value}")

        return 0

    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return 1
    except ValueError as e:
        print(f"ERROR: {e}")
        return 1
    except IOError as e:
        print(f"ERROR: {e}")
        return 1
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
