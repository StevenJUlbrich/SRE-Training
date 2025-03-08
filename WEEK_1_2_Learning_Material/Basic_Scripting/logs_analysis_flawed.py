#!/usr/bin/env python3
"""
Flawed Log Analysis Script - Basic Scripting

This module contains a flawed implementation of a log file analyzer.
There are several errors and inefficiencies that need to be identified and fixed.

TASK:
    - Review the code and identify the bugs and inefficiencies
    - Fix the implementation to make it work correctly
    - Consider error handling, validation, and output formatting improvements

Common issues to look for:
    - Missing error handling
    - Inefficient code
    - Incorrect pattern matching
    - Poor code organization
"""

import re
import sys


def analyze_logs(log_file):
    """
    Analyze a log file and print the count of each error.

    # ISSUE #1 (HINT): Missing error handling for file operations
    """
    # Pattern to match error messages
    # ISSUE #2 (HINT): Pattern may not be optimal or correct
    pattern = re.compile("ERROR: (.*)")

    # Dictionary to store error counts
    # ISSUE #3 (HINT): Could use a more efficient data structure
    error_count = {}

    # Open and read the log file
    # ISSUE #4 (HINT): Not using context manager (with statement)
    log_file = open(log_file, "r")

    # ISSUE #5 (HINT): Reading the entire file at once could be memory-intensive
    lines = log_file.readlines()

    # Close the file
    log_file.close()

    # Iterate through each line
    for line in lines:
        # Check for error messages
        match = pattern.search(line)
        if match:
            error_msg = match.group(1)

            # Increment error count
            # ISSUE #6 (HINT): Inefficient way to count occurrences
            if error_msg in error_count:
                error_count[error_msg] += 1
            else:
                error_count[error_msg] = 1

    # Print the results
    # ISSUE #7 (HINT): Output formatting could be improved
    print("Error Count:")
    for error_msg, count in error_count.items():
        print(f"{error_msg} occurred {count} times.")

    # ISSUE #8 (HINT): No return value or summary information


def search_errors(log_file, search_term):
    """
    Search for errors containing a specific term.

    # ISSUE #9 (HINT): Function has duplicate code from analyze_logs
    """
    # Pattern to match error messages
    pattern = re.compile("ERROR: (.*)")

    # List to store matching errors
    # ISSUE #10 (HINT): No deduplication of errors
    matching_errors = []

    # Open and read the log file
    log_file = open(log_file, "r")

    # Iterate through each line
    for line in log_file:
        # Check for error messages
        match = pattern.search(line)
        if match:
            error_msg = match.group(1)

            # Check if the error contains the search term
            # ISSUE #11 (HINT): Case-sensitive search might not be desired
            if search_term in error_msg:
                matching_errors.append(error_msg)

    # Close the file
    log_file.close()

    # Print the results
    print(f"Errors containing '{search_term}':")
    for error_msg in matching_errors:
        print(f"- {error_msg}")

    # ISSUE #12 (HINT): No return value


def get_error_timestamps(log_file):
    """
    Get timestamps of errors in the log file.

    # ISSUE #13 (HINT): Incomplete implementation
    """
    # Pattern to match timestamps and errors
    # ISSUE #14 (HINT): The pattern might miss some formats or be too restrictive
    timestamp_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*ERROR")

    # ISSUE #15 (HINT): Function is just a stub, not implemented


def main():
    """
    Main function to parse arguments and run the log analyzer.

    # ISSUE #16 (HINT): Poor command-line argument handling
    """
    # Check arguments
    if len(sys.argv) < 2:
        print("Usage: python logs_analysis.py log_file [search_term]")
        return 1

    log_file = sys.argv[1]

    # ISSUE #17 (HINT): No file existence check

    # If we have a search term, search for matching errors
    if len(sys.argv) > 2:
        search_term = sys.argv[2]
        search_errors(log_file, search_term)
    else:
        # Otherwise, analyze all errors
        analyze_logs(log_file)

    # ISSUE #18 (HINT): No error handling for function calls

    return 0


if __name__ == "__main__":
    # ISSUE #19 (HINT): Not using the return value from main
    main()
