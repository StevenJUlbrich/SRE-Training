#!/usr/bin/env python3
"""
Flawed Singleton Logger Implementation - Learning Exercise

This module contains a flawed implementation of the Singleton design pattern
for a logging system. It demonstrates common mistakes and misunderstandings
when implementing this pattern.

Learning Task:
    - Identify and fix issues with the Singleton implementation
    - Improve thread safety
    - Correct object instantiation control
    - Address potential memory leaks and performance issues
    - Implement proper encapsulation

Common issues demonstrated:
    - Improper Singleton implementation
    - Thread safety problems
    - Incorrect class vs instance methods
    - Poor encapsulation
    - Inefficient log storage
"""

import threading
import time
from datetime import datetime

# No proper enum usage for log levels - using strings instead
LOG_LEVEL_DEBUG = "DEBUG"
LOG_LEVEL_INFO = "INFO"
LOG_LEVEL_WARNING = "WARNING"
LOG_LEVEL_ERROR = "ERROR"
LOG_LEVEL_CRITICAL = "CRITICAL"

# Global dictionary to map string levels to numeric values
# This approach is error-prone and hard to maintain
LOG_LEVEL_VALUES = {
    LOG_LEVEL_DEBUG: 1,
    LOG_LEVEL_INFO: 2,
    LOG_LEVEL_WARNING: 3,
    LOG_LEVEL_ERROR: 4,
    LOG_LEVEL_CRITICAL: 5,
}


class Logger:
    """
    A flawed implementation of a Singleton logger.

    This implementation has several issues that prevent it from being
    a proper Singleton and thread-safe logger.
    """

    # Class variable but not properly protected
    instance = None

    # Missing proper thread lock for synchronization

    def __init__(self, name="DefaultLogger"):
        """Initialize a new Logger instance."""
        # No prevention of direct instantiation

        # Poor encapsulation - using public attributes
        self.name = name
        self.logs = []
        self.level = LOG_LEVEL_INFO

    # Flawed Singleton implementation - doesn't use classmethod decorator
    def get_instance(self, name="DefaultLogger"):
        """
        Get the singleton instance of the Logger.

        This method is flawed as it's an instance method, not a class method.
        """
        # Not thread-safe without a lock
        if Logger.instance is None:
            Logger.instance = Logger(name)
        return Logger.instance

    # Incorrect setter method - missing validation
    def set_level(self, level):
        """Set the minimum log level to display."""
        # No validation if level is a valid log level
        self.level = level

    # Log methods that don't properly use the internal _log method
    def debug(self, message):
        """Log a debug message."""
        # Direct implementation instead of reusing _log
        if LOG_LEVEL_VALUES[LOG_LEVEL_DEBUG] >= LOG_LEVEL_VALUES[self.level]:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            thread_name = threading.current_thread().name

            # Inconsistent log format compared to other levels
            log_entry = f"{timestamp} - DEBUG - {message}"
            self.logs.append(log_entry)

            print(f"[{timestamp}] [DEBUG] [{thread_name}] {message}")

    def info(self, message):
        """Log an info message."""
        self._log(LOG_LEVEL_INFO, message)

    def warning(self, message):
        """Log a warning message."""
        self._log(LOG_LEVEL_WARNING, message)

    def error(self, message):
        """Log an error message."""
        self._log(LOG_LEVEL_ERROR, message)

    def critical(self, message):
        """Log a critical message."""
        self._log(LOG_LEVEL_CRITICAL, message)

    def _log(self, level, message):
        """Internal method to log a message."""
        # Improper level check using hardcoded dictionary
        if LOG_LEVEL_VALUES[level] >= LOG_LEVEL_VALUES[self.level]:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            thread_name = threading.current_thread().name

            # Inconsistent log entry format (different from debug)
            log_entry = {
                "timestamp": timestamp,
                "level": level,
                "thread": thread_name,
                "message": message,
            }

            # Direct list manipulation - not thread-safe
            self.logs.append(log_entry)

            print(f"[{timestamp}] [{level}] [{thread_name}] {message}")

    # No method to safely retrieve logs

    def clear_logs(self):
        """Clear all logged entries."""
        # Not thread-safe
        self.logs = []


# Global logger instance - breaks the Singleton pattern
global_logger = None


def get_logger(name="DefaultLogger"):
    """
    A global function to get the logger instance.

    This approach undermines the Singleton pattern and creates confusion
    about how to access the logger.
    """
    global global_logger
    if global_logger is None:
        global_logger = Logger(name)
    return global_logger


def worker_function(worker_id):
    """
    A sample worker function that uses the logger.

    This function demonstrates incorrect access to the logger singleton.
    """
    # Inconsistent way to access the logger - sometimes using the global function,
    # sometimes using the class method
    if worker_id % 2 == 0:
        logger = get_logger()
    else:
        # This creates a new logger instance, not getting the singleton
        logger = Logger()
        logger = logger.get_instance()

    logger.info(f"Worker {worker_id} started")

    # Simulate some work
    time.sleep(0.1 * worker_id)

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
    Demonstrate the Singleton Logger with multiple threads.
    """
    # Inconsistent logger access - not using the Singleton properly
    main_logger = Logger("MainLogger")
    main_logger.set_level(LOG_LEVEL_DEBUG)

    main_logger.info("Starting the demonstration")

    # Create some threads to simulate concurrent access
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker_function, args=(i,), name=f"Worker-{i}")
        threads.append(thread)

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    main_logger.info("All workers have completed")

    # This will show that we don't have a true Singleton
    logger1 = Logger("Logger1")
    logger2 = Logger("Logger2")

    print("\nSingleton Check:")
    print(f"logger1 is logger2: {logger1 is logger2}")  # Will be False

    # No demonstration of direct instantiation prevention since it's not implemented

    # Brief explanation of the intended pattern
    print("\nSingleton Pattern (As Intended):")
    print("1. Only one instance should exist throughout the application")
    print("2. Global access point via a class method or global function")
    print("3. Thread-safe implementation (not in this flawed version)")


if __name__ == "__main__":
    demonstrate_singleton_logger()
