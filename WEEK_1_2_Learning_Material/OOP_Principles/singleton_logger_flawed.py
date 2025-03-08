#!/usr/bin/env python3
"""
Flawed Singleton Logger Implementation - Object-Oriented Programming Principles

This module contains a flawed implementation of the Singleton design pattern
for a logging system. There are several issues with the Singleton implementation
and other OOP principles that need to be identified and fixed.

TASK:
    - Review the code and identify issues with the Singleton implementation
    - Fix the implementation to create a proper thread-safe Singleton
    - Improve encapsulation and class design

Common issues to look for:
    - Incorrect Singleton implementation
    - Thread-safety problems
    - Poor encapsulation
    - Inefficient code
"""

import threading
import time
from datetime import datetime

# ISSUE #1 (HINT): Missing proper level management
# Should use an enum or constants for log levels


class Logger:
    """
    A flawed implementation of a Singleton logger.

    # ISSUE #2 (HINT): This implementation of Singleton has problems
    """

    # Class variable to store the instance
    instance = None

    # ISSUE #3 (HINT): Missing lock for thread safety

    def __init__(self):
        """Initialize a new Logger instance."""
        # ISSUE #4 (HINT): This allows creating multiple instances
        # Should check if an instance already exists

        # Initialize instance variables
        self.log_entries = []
        self.min_level = 1  # 0=DEBUG, 1=INFO, 2=WARNING, 3=ERROR, 4=CRITICAL

    @staticmethod
    def get_instance():
        """
        Get the singleton instance of the Logger.

        # ISSUE #5 (HINT): This method doesn't ensure thread safety
        """
        if Logger.instance is None:
            # ISSUE: Not thread-safe - race condition possible here
            Logger.instance = Logger()
        return Logger.instance

    # ISSUE #6 (HINT): Missing proper log level methods

    def log(self, level, message):
        """
        Log a message at the specified level.

        # ISSUE #7 (HINT): Level handling is numeric and error-prone
        """
        level_names = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

        if level >= self.min_level:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # ISSUE #8 (HINT): Thread name isn't captured

            # Create log entry
            log_entry = {
                "timestamp": timestamp,
                "level": level_names[level],
                "message": message,
            }

            # Add to log entries
            self.log_entries.append(log_entry)

            # Print the log entry
            print(f"[{timestamp}] [{level_names[level]}] {message}")

    def debug(self, message):
        """Log a debug message."""
        self.log(0, message)

    def info(self, message):
        """Log an info message."""
        self.log(1, message)

    def warning(self, message):
        """Log a warning message."""
        self.log(2, message)

    def error(self, message):
        """Log an error message."""
        self.log(3, message)

    def critical(self, message):
        """Log a critical message."""
        self.log(4, message)

    # ISSUE #9 (HINT): Logs are publicly accessible
    # No encapsulation of log_entries


def worker_function(worker_id):
    """
    A sample worker function that uses the logger.

    # ISSUE #10 (HINT): This might not use the logger correctly
    """
    # ISSUE: Creating a new logger each time (doesn't use get_instance)
    logger = Logger()

    logger.info(f"Worker {worker_id} started")

    # Simulate some work
    time.sleep(0.1 * worker_id)

    # Log based on worker id
    if worker_id % 2 == 0:
        logger.debug(f"Worker {worker_id} is doing even-numbered work")
    else:
        logger.warning(f"Worker {worker_id} encountered an odd number")

    # Simulate an error for one worker
    if worker_id == 3:
        logger.error(f"Worker {worker_id} encountered an error")

    logger.info(f"Worker {worker_id} finished")


def demonstrate_singleton_logger():
    """
    Demonstrate the flawed Singleton Logger with multiple threads.
    """
    # Get the logger instance
    # ISSUE #11 (HINT): Not using the get_instance method consistently
    logger = Logger()
    logger.min_level = 0  # Show all log levels

    logger.info("Starting the demonstration")

    # Create some threads to simulate concurrent access
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker_function, args=(i,))
        threads.append(thread)

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    logger.info("All workers have completed")

    # ISSUE #12 (HINT): No demonstration of singleton property
    # Should show that multiple calls to get_instance() return the same object

    # Show log entries
    print("\nLog Entries:")
    for entry in logger.log_entries:
        print(f"[{entry['timestamp']}] [{entry['level']}] {entry['message']}")

    # ISSUE #13 (HINT): This will show incorrect results
    # Due to thread safety issues and not using get_instance consistently


if __name__ == "__main__":
    demonstrate_singleton_logger()
