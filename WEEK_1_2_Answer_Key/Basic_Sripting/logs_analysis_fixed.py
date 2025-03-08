#!/usr/bin/env python3
"""
Working Log Analysis Script

This script analyzes a log file to extract and count error messages,
and then generates a summary report. It is based on the structured flawed
version, with improvements for safe file handling, memory efficiency, and
clear user feedback.

Possible Variations:
  - For very large log files, consider processing the file in chunks or using generators.
  - Use Python's logging module for robust logging instead of printing to stdout.
  - Integrate with monitoring tools for real-time error tracking.
"""

import argparse
import os
import re
import sys
from collections import Counter
from datetime import datetime


def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Analyze log files for error messages and generate a summary report."
    )
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument(
        "--search", type=str, help="Optional term to search for in the log"
    )
    parser.add_argument(
        "--top", type=int, default=5, help="Number of top errors to display"
    )
    # Possible Variation: Add an '--output' option to save the report to a file.
    return parser.parse_args()


def analyze_log_file(log_file_path):
    """
    Analyze the log file to count error messages.

    Args:
        log_file_path (str): Path to the log file.

    Returns:
        Counter: A Counter mapping error messages to their occurrence counts.
    """
    # Ensure the file exists
    if not os.path.isfile(log_file_path):
        raise FileNotFoundError(f"Log file '{log_file_path}' not found.")

    # Precompile the regex for performance
    error_pattern = re.compile(r"ERROR: (.+)")
    errors = Counter()

    # Use a context manager for safe file handling and iterate line by line.
    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = error_pattern.search(line)
            if match:
                error_message = match.group(1).strip()
                errors[error_message] += 1
    return errors


def search_log_file(log_file_path, term):
    """
    Search the log file for lines containing a specific term (case-insensitive).

    Args:
        log_file_path (str): Path to the log file.
        term (str): Term to search for.

    Returns:
        list: A list of matching lines.
    """
    if not os.path.isfile(log_file_path):
        raise FileNotFoundError(f"Log file '{log_file_path}' not found.")

    results = []
    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            # Using case-insensitive search by converting both term and line to lower case.
            if term.lower() in line.lower():
                results.append(line.strip())
    return results


def generate_summary_report(errors, top_n):
    """
    Generate a formatted summary report from error counts.

    Args:
        errors (Counter): Counter with error messages and their counts.
        top_n (int): Number of top errors to include.

    Returns:
        str: A formatted report string.
    """
    total_errors = sum(errors.values())
    report_lines = []
    report_lines.append("=== Log Analysis Summary Report ===")
    report_lines.append(
        f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    report_lines.append(f"Total Errors: {total_errors}")
    report_lines.append("")
    report_lines.append(f"Top {top_n} Errors:")

    # Possible Variation: Directly use errors.most_common(top_n) if using Counter.
    for i, (err, count) in enumerate(errors.most_common(top_n), start=1):
        report_lines.append(f"{i}. {err} - {count} occurrence(s)")
    return "\n".join(report_lines)


def main():
    args = parse_args()

    try:
        errors = analyze_log_file(args.log_file)

        # If a search term is provided, perform the search and display results.
        if args.search:
            results = search_log_file(args.log_file, args.search)
            print(f"Search results for '{args.search}' ({len(results)} match(es)):")
            for line in results:
                print(line)
            print("")  # Add a blank line after search results

        report = generate_summary_report(errors, args.top)
        print(report)

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
