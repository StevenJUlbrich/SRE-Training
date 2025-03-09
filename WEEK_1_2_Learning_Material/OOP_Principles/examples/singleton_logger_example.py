#!/usr/bin/env python3
"""
Singleton Logger Example - Object-Oriented Programming Principles

This module demonstrates the implementation of the Singleton design pattern
for a thread-safe logging system.

Key Concepts:
    - Singleton design pattern
    - Thread safety
    - Private class variables and methods
    - Class methods vs. instance methods
    - Preventing direct instantiation

Learning Objectives:
    - Understand the purpose and implementation of the Singleton pattern
    - Learn how to make a class thread-safe
    - Recognize when to use class methods
    - Practice controlling object instantiation
"""

import threading
import time
from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, Optional


class LogLevel(Enum):
    """Enumeration for log levels."""

    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()


class Logger:
    """
    A thread-safe Singleton logger class.

    The Singleton pattern ensures that only one instance of the Logger exists
    in the application, providing a global point of access to it.
    """

    # Private class variables
    _instance: Optional["Logger"] = None
    _lock = threading.Lock()

    def __init__(self):
        """
        Initialize a new Logger instance.

        This constructor is private and should not be called directly.
        Instead, use the get_logger() class method.

        Raises:
            RuntimeError: If the constructor is called directly
        """
        # Prevent direct instantiation
        if not hasattr(self, "_initialized"):
            raise RuntimeError(
                "Use Logger.get_logger() instead of direct instantiation"
            )

        # Instance variables
        self._log_entries: List[Dict] = []
        self._min_level = LogLevel.INFO

    @classmethod
    def get_logger(cls) -> "Logger":
        """
        Get the singleton instance of the Logger.

        This method ensures that only one instance of the Logger is created.
        If the instance doesn't exist, it creates one; otherwise, it returns the existing one.
        The method is thread-safe using a lock to prevent race conditions.

        Returns:
            Logger: The singleton Logger instance
        """
        # Double-checked locking pattern
        if cls._instance is None:
            with cls._lock:
                # Check again after acquiring the lock
                if cls._instance is None:
                    cls._instance = super(Logger, cls).__new__(cls)
                    cls._instance._initialized = True
                    cls._instance.__init__()

        return cls._instance

    def set_level(self, level: LogLevel) -> None:
        """
        Set the minimum log level to display.

        Args:
            level: The minimum log level
        """
        self._min_level = level

    def debug(self, message: str) -> None:
        """Log a debug message."""
        self._log(LogLevel.DEBUG, message)

    def info(self, message: str) -> None:
        """Log an info message."""
        self._log(LogLevel.INFO, message)

    def warning(self, message: str) -> None:
        """Log a warning message."""
        self._log(LogLevel.WARNING, message)

    def error(self, message: str) -> None:
        """Log an error message."""
        self._log(LogLevel.ERROR, message)

    def critical(self, message: str) -> None:
        """Log a critical message."""
        self._log(LogLevel.CRITICAL, message)

    def _log(self, level: LogLevel, message: str) -> None:
        """
        Internal method to log a message if its level meets the minimum threshold.

        Args:
            level: The log level of the message
            message: The message to log
        """
        if level.value >= self._min_level.value:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            thread_name = threading.current_thread().name

            log_entry = {
                "timestamp": timestamp,
                "level": level.name,
                "thread": thread_name,
                "message": message,
            }

            self._log_entries.append(log_entry)

            # Print the log entry
            print(f"[{timestamp}] [{level.name}] [{thread_name}] {message}")

    def get_logs(self) -> List[Dict]:
        """
        Get all logged entries.

        Returns:
            List[Dict]: A list of all log entries
        """
        return self._log_entries.copy()

    def clear_logs(self) -> None:
        """Clear all logged entries."""
        self._log_entries.clear()


def worker_function(worker_id: int) -> None:
    """
    A sample worker function that uses the logger.

    Args:
        worker_id: The ID of the worker
    """
    logger = Logger.get_logger()

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


def demonstrate_singleton_logger() -> None:
    """
    Demonstrate the Singleton Logger with multiple threads.
    """
    # Get the logger instance
    logger = Logger.get_logger()
    logger.set_level(LogLevel.DEBUG)  # Show all log levels

    logger.info("Starting the demonstration")

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

    logger.info("All workers have completed")

    # Show that we have a true singleton
    logger1 = Logger.get_logger()
    logger2 = Logger.get_logger()

    print("\nSingleton Check:")
    print(f"logger1 is logger2: {logger1 is logger2}")

    # Demonstrate direct instantiation prevention
    try:
        logger3 = Logger()
        print("Direct instantiation succeeded (this is wrong)")
    except RuntimeError as e:
        print(f"Direct instantiation prevented: {e}")

    # Explain the Singleton pattern
    print("\nSingleton Pattern Explanation:")
    print("1. Only one instance exists throughout the application")
    print("2. Global access point via the get_logger() class method")
    print("3. Thread-safe implementation using locks")
    print("4. Controlled instantiation (prevents direct constructor calls)")
    print("5. State is shared across all parts of the application")


if __name__ == "__main__":
    demonstrate_singleton_logger()
