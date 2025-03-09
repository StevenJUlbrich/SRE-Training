#!/usr/bin/env python3
"""
Flawed CSV Filtering Script (Alternative Version)

OBJECTIVE:
    - Reads a CSV file.
    - Filters by a user-specified column and value.
    - Writes only matching rows to a new file.

INSTRUCTIONS:
    - Identify the logical and structural flaws.
    - Consider improvements in error handling, user experience, and best practices.
"""

import csv
import sys


def extract_rows(source_file, destination_file, target_column, match_value):
    """
    Extract rows from a CSV where target_column = match_value.

    FLAWS/HINTS:
        1) No checks to see if the CSV file exists or can be opened.
        2) Missing context managers (using plain open without 'with').
        3) Ignores whether target_column actually appears in the header.
        4) Does not handle rows of unexpected length.
        5) No meaningful error handling or user feedback.
    """

    # Open files directly (Flaw: no context manager, potential resource leak).
    f_in = open(source_file, "r")
    f_out = open(destination_file, "w")

    reader = csv.reader(f_in)
    writer = csv.writer(f_out)

    # Attempt to grab a header row
    # (Flaw: no validation if header actually exists or is too short.)
    header_row = next(reader)

    # (Flaw: no attempt to check if target_column is actually in the header.)
    # We'll just do a naive scan to find the column index
    col_idx = 0  # This is a guess that 'target_column' will be at index 0
    for i, col_name in enumerate(header_row):
        if col_name == target_column:
            col_idx = i
            break

    # Write the header to the new file
    writer.writerow(header_row)

    # For each row, compare the value in col_idx
    # (Flaw: no boundary checks for row length.)
    for row in reader:
        if row[col_idx] == match_value:
            writer.writerow(row)

    # Close files (Flaw: lack of try-except or context manager)
    f_in.close()
    f_out.close()


def main():
    """
    Main function that parses arguments from sys.argv.
    FLAWS/HINTS:
        6) No robust command-line argument parsing.
        7) Minimal feedback to the user.
        8) No checks on number/type of arguments or file existence.
    """
    if len(sys.argv) < 5:
        print(
            "Usage: python flawed_filter_alternative.py <input> <output> <column> <value>"
        )
        return 1

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    column_name = sys.argv[3]
    desired_value = sys.argv[4]

    # Call the flawed extraction function
    extract_rows(input_csv, output_csv, column_name, desired_value)

    # (Flaw: no indication of how many rows matched or success/failure states.)
    print("Extraction completed (possibly).")
    return 0


if __name__ == "__main__":
    # (Flaw: return code is unused; no handling in a larger system.)
    main()
