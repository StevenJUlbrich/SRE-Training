#!/usr/bin/env python3
"""
Corrected CSV Filtering Script (Alternative Version)

This script:
    - Reads a CSV file.
    - Filters rows by a user-specified column and value.
    - Writes only matching rows to a new file.
    - Provides basic validation and helpful feedback.
"""

import csv
import os
import sys


def extract_rows_correct(
    source_file: str,
    destination_file: str,
    target_column: str,
    match_value: str,
) -> int:
    """
    Extract rows from a CSV where `target_column` equals `match_value`.

    Args:
        source_file: Path to the CSV input file
        destination_file: Path to write the filtered output
        target_column: Name of the column we want to match
        match_value: Value that must match for rows to be included

    Returns:
        The number of rows that matched the criteria (excluding the header).
    """
    # Verify that input file exists
    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"Input file '{source_file}' does not exist.")

    matched_count = 0

    # Use context managers to handle file resources
    with open(source_file, "r", newline="", encoding="utf-8") as fin, open(
        destination_file, "w", newline="", encoding="utf-8"
    ) as fout:

        reader = csv.reader(fin)
        writer = csv.writer(fout)

        # Retrieve the header from the input CSV
        try:
            header_row = next(reader)
        except StopIteration:
            # The file is empty
            raise ValueError(f"File '{source_file}' appears to be empty.")

        # Ensure the target_column is present
        if target_column not in header_row:
            raise ValueError(
                f"Column '{target_column}' not found in CSV header: {header_row}"
            )

        # Determine the index of the target_column
        col_index = header_row.index(target_column)

        # Write the header row to the output
        writer.writerow(header_row)

        # Iterate and filter rows
        for row in reader:
            # Basic length check
            if len(row) < len(header_row):
                # Could skip or raise an error; here we skip rows shorter than header
                continue

            if row[col_index] == match_value:
                writer.writerow(row)
                matched_count += 1

    return matched_count


def main() -> int:
    """
    Main function to parse command-line arguments and run the CSV extraction.
    Returns an integer status code: 0 for success, non-zero for errors.
    """
    # Basic argument checks
    if len(sys.argv) < 5:
        print(
            "USAGE: python corrected_filter_alternative.py <input> <output> <column> <value>"
        )
        return 1

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    column_name = sys.argv[3]
    desired_value = sys.argv[4]

    # Attempt to filter
    try:
        match_count = extract_rows_correct(
            input_csv, output_csv, column_name, desired_value
        )
        print(f"Filtering complete. {match_count} row(s) matched the criteria.")
        print(f"Filtered rows saved to: {output_csv}")
        return 0

    except FileNotFoundError as fnfe:
        print(f"ERROR: {fnfe}")
        return 1
    except ValueError as ve:
        print(f"ERROR: {ve}")
        return 1
    except OSError as ose:
        print(f"ERROR: Failed to read/write files: {ose}")
        return 1
    except Exception as ex:
        print(f"ERROR: An unexpected error occurred: {ex}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
