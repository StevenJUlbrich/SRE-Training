#!/usr/bin/env python3
"""
Structured Flawed Log Analysis Script

This script is designed to analyze a log file and produce a summary of error messages.
It follows a structured approach with functions for argument parsing, analysis, searching,
and reporting. However, certain subtleties have been intentionally overlooked.
Examine the hints in the comments to identify potential improvements.
"""

import argparse
import re
import sys


def parse_args():
    # Hint: argparse is used appropriately, but consider validating inputs further.
    parser = argparse.ArgumentParser(
        description="Analyze log files for error messages and generate a summary."
    )
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument(
        "--search", type=str, help="Optional term to search for in the log"
    )
    parser.add_argument(
        "--top", type=int, default=5, help="Number of top errors to display"
    )
    return parser.parse_args()


def analyze_log_file(log_file_path):
    """
    Analyze the log file to count error messages.

    Hints:
    - Consider verifying that the file exists before opening.
    - Using readlines() may not be optimal for very large files.
    - File handles should ideally be managed with context managers.
    """
    # Flaw: No check for file existence and not using a context manager.
    f = open(log_file_path, "r")
    errors = {}
    error_pattern = re.compile("ERROR: (.+)")
    # Flaw: readlines() loads the entire file into memory.
    lines = f.readlines()
    f.close()

    for line in lines:
        match = error_pattern.search(line)
        if match:
            error_msg = match.group(1).strip()
            if error_msg in errors:
                errors[error_msg] += 1
            else:
                errors[error_msg] = 1
    return errors


def search_log_file(log_file_path, term):
    """
    Search the log file for lines containing a specific term.

    Hints:
    - Consider using a context manager to handle file operations.
    - Reflect on whether a case-insensitive search might be more useful.
    """
    f = open(log_file_path, "r")
    results = []
    for line in f:
        # Flaw: This search is case-sensitive.
        if term in line:
            results.append(line.strip())
    f.close()
    return results


def generate_summary_report(errors, top_n):
    """
    Generate a formatted summary report of error counts.

    Hints:
    - The report should clearly list the most frequent errors.
    """
    report_lines = []
    report_lines.append("=== Log Analysis Summary Report ===")
    total_errors = sum(errors.values())
    report_lines.append(f"Total Errors: {total_errors}")
    report_lines.append("")
    report_lines.append(f"Top {top_n} Errors:")
    # Flaw: Sorting is done manually; consider more efficient approaches if scaling.
    sorted_errors = sorted(errors.items(), key=lambda x: x[1], reverse=True)
    for i, (err, count) in enumerate(sorted_errors[:top_n], 1):
        report_lines.append(f"{i}. {err} - {count} occurrence(s)")
    return "\n".join(report_lines)


def main():
    args = parse_args()

    # Flaw: No error handling for file I/O; this could crash if the file is missing.
    error_counts = analyze_log_file(args.log_file)

    # If a search term is provided, perform the search.
    if args.search:
        search_results = search_log_file(args.log_file, args.search)
        print(f"Search results for '{args.search}':")
        for result in search_results:
            print(result)
        print("")

    report = generate_summary_report(error_counts, args.top)
    print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
