#!/usr/bin/env python3
"""
Flawed Environment Setup Script - Basic Scripting

This module contains a flawed implementation of an environment setup script.
There are several errors and inefficiencies that need to be identified and fixed.

TASK:
    - Review the code and identify the bugs and inefficiencies
    - Fix the implementation to make it work correctly
    - Consider error handling, validation, and code organization improvements

Common issues to look for:
    - Missing error handling
    - Inefficient code
    - Security issues
    - Poor code organization
"""

import os
import subprocess
import sys


def install_dependencies(requirements_file):
    """
    Install Python dependencies using pip.

    # ISSUE #1 (HINT): Missing error handling and validation
    """
    # ISSUE #2 (HINT): No check if the file exists

    print(f"Installing dependencies from {requirements_file}...")

    # Run pip command
    # ISSUE #3 (HINT): Using os.system is less secure and provides little control
    os.system(f"pip install -r {requirements_file}")

    # ISSUE #4 (HINT): No verification of successful installation

    print("Dependencies installed.")


def setup_environment_variables(env_vars):
    """
    Set environment variables for the application.

    # ISSUE #5 (HINT): Limited scope of environment variables
    """
    # ISSUE #6 (HINT): No validation of env_vars

    print("Setting environment variables...")

    # Set each environment variable
    for key, value in env_vars.items():
        # ISSUE #7 (HINT): This only sets variables for the current process
        os.environ[key] = value
        print(f"Set {key}={value}")

    # ISSUE #8 (HINT): No warning about the limited scope of these variables


def create_directories(directories):
    """
    Create directories for the application.

    # ISSUE #9 (HINT): Missing error handling
    """
    # ISSUE #10 (HINT): No validation of directories parameter

    print("Creating directories...")

    # Create each directory
    for directory in directories:
        # ISSUE #11 (HINT): Doesn't handle existing directories well
        os.mkdir(directory)
        print(f"Created directory: {directory}")

    # ISSUE #12 (HINT): No recursive directory creation (parents)


def run_setup_commands(commands):
    """
    Run a list of setup commands.

    # ISSUE #13 (HINT): Poor error handling and security concerns
    """
    # ISSUE #14 (HINT): No validation of commands parameter

    print("Running setup commands...")

    # Run each command
    for command in commands:
        print(f"Running: {command}")

        # ISSUE #15 (HINT): Using os.system is less secure and provides little control
        result = os.system(command)

        # ISSUE #16 (HINT): Insufficient error checking
        if result != 0:
            print(f"Command failed with code {result}")

    print("Setup commands completed.")


def setup_environment():
    """
    Set up the environment by installing dependencies, setting env variables,
    creating directories, and running setup commands.

    # ISSUE #17 (HINT): Hardcoded configuration
    """
    print("Starting environment setup...")

    # Define the configuration
    # ISSUE #18 (HINT): Hardcoded configuration should be in a separate config file
    config = {
        "requirements_file": "requirements.txt",
        "env_vars": {
            "APP_ENV": "development",
            "DEBUG": "true",
            "API_KEY": "secret_key_12345",  # ISSUE #19 (HINT): Hardcoded sensitive information
        },
        "directories": ["data", "logs", "config"],
        "commands": [
            "echo 'Setup starting...'",
            "python --version",
            "echo 'APP_ENV=' + os.environ.get('APP_ENV', '')",  # ISSUE #20 (HINT): This won't interpolate in the shell command
        ],
    }

    # Run the setup steps
    # ISSUE #21 (HINT): No error handling around function calls
    install_dependencies(config["requirements_file"])
    setup_environment_variables(config["env_vars"])
    create_directories(config["directories"])
    run_setup_commands(config["commands"])

    print("Environment setup complete.")


def main():
    """
    Main function to run the environment setup script.

    # ISSUE #22 (HINT): Poor command-line handling and configuration options
    """
    # ISSUE #23 (HINT): No command-line arguments for configuration

    # Run the setup
    # ISSUE #24 (HINT): No error handling
    setup_environment()

    # ISSUE #25 (HINT): No return value to indicate success/failure


if __name__ == "__main__":
    # ISSUE #26 (HINT): Not using the return value from main
    main()
