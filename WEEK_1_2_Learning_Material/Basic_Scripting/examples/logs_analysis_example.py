#!/usr/bin/env python3
"""
Log Analysis Script - Basic Scripting

This module provides functionality to analyze log files, extract error messages,
and generate error frequency reports.

Key Concepts:
    - Log file parsing and analysis
    - Regular expressions for pattern matching
    - Data aggregation and reporting
    - File I/O with context managers
    - Command-line argument parsing

Learning Objectives:
    - Understand how to work with log files in Python
    - Learn to use regular expressions for text extraction
    - Practice aggregating and summarizing data
    - Recognize patterns in log files
"""

import argparse
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from typing import Any, Dict, List, Optional, Pattern, Tuple


class LogAnalyzer:
    """
    A class for analyzing log files and extracting error information.

    This class demonstrates object-oriented approach to log analysis.
    """

    def __init__(self, log_file: str):
        """
        Initialize the log analyzer with the path to a log file.

        Args:
            log_file: Path to the log file to analyze

        Raises:
            FileNotFoundError: If the log file does not exist
        """
        if not os.path.isfile(log_file):
            raise FileNotFoundError(f"Log file not found: {log_file}")

        self.log_file = log_file
        self.error_pattern = re.compile(r"ERROR: (.*)")
        self.error_count: Dict[str, int] = Counter()
        self.timestamp_pattern = re.compile(
            r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*?(ERROR|INFO|WARN)"
        )
        self.errors_by_hour: Dict[str, int] = defaultdict(int)

    def analyze(self) -> Dict[str, int]:
        """
        Analyze the log file and count errors.

        Returns:
            Dict[str, int]: A dictionary mapping error messages to their occurrence count
        """
        self.error_count = Counter()
        self.errors_by_hour = defaultdict(int)

        with open(self.log_file, "r", encoding="utf-8") as log_file:
            for line in log_file:
                # Extract error messages
                error_match = self.error_pattern.search(line)
                if error_match:
                    error_msg = error_match.group(1)
                    self.error_count[error_msg] += 1

                # Extract timestamps for time-based analysis
                timestamp_match = self.timestamp_pattern.search(line)
                if timestamp_match and timestamp_match.group(2) == "ERROR":
                    try:
                        timestamp_str = timestamp_match.group(1)
                        timestamp = datetime.strptime(
                            timestamp_str, "%Y-%m-%d %H:%M:%S"
                        )
                        hour_key = timestamp.strftime("%Y-%m-%d %H")
                        self.errors_by_hour[hour_key] += 1
                    except ValueError:
                        # Skip lines with invalid timestamps
                        continue

        return dict(self.error_count)

    def get_most_common_errors(self, n: int = 5) -> List[Tuple[str, int]]:
        """
        Get the most common error messages.

        Args:
            n: Number of top errors to return (default: 5)

        Returns:
            List[Tuple[str, int]]: A list of tuples (error_message, count) for the most frequent errors
        """
        return self.error_count.most_common(n)

    def get_error_count(self) -> int:
        """
        Get the total number of errors.

        Returns:
            int: The total count of all errors
        """
        return sum(self.error_count.values())

    def get_errors_by_hour(self) -> Dict[str, int]:
        """
        Get error counts grouped by hour.

        Returns:
            Dict[str, int]: A dictionary mapping hour strings to error counts
        """
        return dict(self.errors_by_hour)

    def get_peak_error_time(self) -> Optional[Tuple[str, int]]:
        """
        Get the hour with the highest number of errors.

        Returns:
            Optional[Tuple[str, int]]: A tuple (hour, count) for the peak error hour, or None if no errors
        """
        if not self.errors_by_hour:
            return None

        peak_hour = max(self.errors_by_hour.items(), key=lambda x: x[1])
        return peak_hour

    def search_logs(self, pattern: str) -> List[str]:
        """
        Search the log file for lines matching a specific pattern.

        Args:
            pattern: Regular expression pattern to search for

        Returns:
            List[str]: List of matching log lines
        """
        compiled_pattern: Pattern[str] = re.compile(pattern)
        matching_lines: List[str] = []

        with open(self.log_file, "r", encoding="utf-8") as log_file:
            for line in log_file:
                if compiled_pattern.search(line):
                    matching_lines.append(line.strip())

        return matching_lines


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments for the log analysis script.

    Returns:
        argparse.Namespace: Parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description="Analyze log files to extract error information.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("log_file", help="Path to the log file to analyze")

    parser.add_argument(
        "--top", type=int, default=5, help="Number of top errors to display"
    )

    parser.add_argument(
        "--search", type=str, help="Search for a specific pattern in the logs"
    )

    parser.add_argument(
        "--output", type=str, help="Path to save the analysis report (optional)"
    )

    return parser.parse_args()


def format_report(
    analyzer: LogAnalyzer, top_n: int, search_results: Optional[List[str]] = None
) -> str:
    """
    Format the log analysis results into a report.

    Args:
        analyzer: The LogAnalyzer instance with analysis results
        top_n: Number of top errors to include
        search_results: Optional list of search results

    Returns:
        str: Formatted report as a string
    """
    # Get analysis data
    total_errors = analyzer.get_error_count()
    most_common_errors = analyzer.get_most_common_errors(top_n)
    peak_error_time = analyzer.get_peak_error_time()

    # Format the report
    report = []
    report.append("=== Log Analysis Report ===")
    report.append(f"Log File: {analyzer.log_file}")
    report.append(f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")

    report.append(f"Total Errors Found: {total_errors}")

    if peak_error_time:
        report.append(
            f"Peak Error Hour: {peak_error_time[0]} ({peak_error_time[1]} errors)"
        )

    report.append("")
    report.append(f"Top {min(top_n, len(most_common_errors))} Most Frequent Errors:")

    for i, (error, count) in enumerate(most_common_errors, 1):
        report.append(f'{i}. "{error}" - {count} occurrences')

    if search_results:
        report.append("")
        report.append(f"Search Results ({len(search_results)} matches):")
        for i, line in enumerate(search_results[:10], 1):
            report.append(f"{i}. {line}")

        if len(search_results) > 10:
            report.append(f"... and {len(search_results) - 10} more matches")

    return "\n".join(report)


def main() -> int:
    """
    Main function to run the log analysis script.

    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    args = parse_arguments()

    try:
        # Create analyzer and analyze logs
        analyzer = LogAnalyzer(args.log_file)
        analyzer.analyze()

        # Search for pattern if specified
        search_results = None
        if args.search:
            search_results = analyzer.search_logs(args.search)

        # Format report
        report = format_report(analyzer, args.top, search_results)

        # Output report
        if args.output:
            with open(args.output, "w", encoding="utf-8") as output_file:
                output_file.write(report)
            print(f"Analysis report saved to: {args.output}")
        else:
            print(report)

        return 0

    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return 1
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
