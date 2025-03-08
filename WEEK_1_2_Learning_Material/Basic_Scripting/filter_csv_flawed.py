#!/usr/bin/env python3
"""
Flawed CSV Filtering Script - Basic Scripting

This module contains a flawed implementation of a CSV filtering script.
There are several errors and inefficiencies that need to be identified and fixed.

TASK:
    - Review the code and identify the bugs and inefficiencies
    - Fix the implementation to make it work correctly
    - Consider error handling, validation, and user experience improvements

Common issues to look for:
    - Missing error handling
    - Inefficient file operations
    - Incorrect CSV parsing
    - Poor user feedback
"""

import csv
import sys


def filter_csv(input_file, output_file, filter_column, filter_value):
    """
    Filter rows of a CSV file based on a given column's matching value.

    # ISSUE #1 (HINT): Missing error handling and parameter validation
    """
    # Open the input and output files
    # ISSUE #2 (HINT): Not using context managers (with statements)
    infile = open(input_file, "r")
    outfile = open(output_file, "w")

    # Read the CSV
    # ISSUE #3 (HINT): Not handling CSV properly
    reader = csv.reader(infile)

    # Get the header row
    header = next(reader)

    # ISSUE #4 (HINT): No validation of filter_column

    # Find the index of the filter column
    # ISSUE #5 (HINT): Error-prone way to find column index
    filter_index = -1
    for i, column in enumerate(header):
        if column == filter_column:
            filter_index = i
            break

    # ISSUE #6 (HINT): What if the column is not found?

    # Write the header to the output file
    # ISSUE #7 (HINT): Not using csv.writer
    outfile.write(",".join(header) + "\n")

    # Filter and write matching rows
    for row in reader:
        # ISSUE #8 (HINT): Potential index error if row is too short
        if row[filter_index] == filter_value:
            outfile.write(",".join(row) + "\n")

    # Close the files
    # ISSUE #9 (HINT): Should use context managers instead
    infile.close()
    outfile.close()

    # ISSUE #10 (HINT): No feedback to the user about the operation


def main():
    """
    Main function to parse arguments and run the CSV filter.

    # ISSUE #11 (HINT): Inadequate command-line argument handling
    """
    # Check if we have the right number of arguments
    if len(sys.argv) != 5:
        print(
            "Usage: python filter_csv.py input_file output_file filter_column filter_value"
        )
        return 1

    # Get the arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    filter_column = sys.argv[3]
    filter_value = sys.argv[4]

    # ISSUE #12 (HINT): No checking if files exist or can be opened

    # Filter the CSV
    # ISSUE #13 (HINT): No error handling around function call
    filter_csv(input_file, output_file, filter_column, filter_value)

    # ISSUE #14 (HINT): No indication of success or failure
    print("Filtering complete.")

    return 0


if __name__ == "__main__":
    # ISSUE #15 (HINT): Not capturing or using the return value
    main()
