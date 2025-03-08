#!/usr/bin/env python3
"""
Flawed Service Deployment Environment Setup - SRE Practice

This script is intended to set up an environment for deploying microservices,
but contains numerous flaws, anti-patterns, and reliability issues.

Learning Task:
    - Identify and fix reliability, security, and maintainability issues
    - Improve error handling, logging, and resource management
    - Implement proper configuration and validation

Common SRE issues demonstrated:
    - Insufficient logging
    - Poor error handling
    - Resource leaks
    - Security vulnerabilities
    - Configuration problems
"""

import json
import os
import random
import socket
import subprocess
import sys
import time

# Global variables
DB_PASSWORD = "password123"  # Hardcoded credentials
SERVICES = ["api", "database", "cache", "worker"]
DEBUG = True  # Hardcoded debug flag

# Create a log file
LOG_FILE = open("deployment.log", "w")  # Resource leak: never closed


def log_message(message):
    """Log a message to the console and log file."""
    print(message)

    # Write to log file without any error handling
    LOG_FILE.write(message + "\n")
    # No flush - potential for lost logs


def check_system_requirements():
    """Check if the system meets the deployment requirements."""
    log_message("Checking system requirements...")

    # Check Python version (incomplete check)
    if sys.version_info.major < 3:
        log_message("ERROR: Python 3 is required")
        return False

    # Check disk space (using shell=True which is a security risk)
    if os.name == "posix":
        df_output = subprocess.check_output("df -h /", shell=True).decode()
        available = df_output.split("\n")[1].split()[3]
        log_message(f"Available disk space: {available}")

    # Always return True even if checks fail
    log_message("System requirements check passed")
    return True


def load_configuration(config_file="config.json"):
    """Load configuration from a JSON file."""
    log_message(f"Loading configuration from {config_file}...")

    # No check if the file exists before trying to open it
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
            log_message("Configuration loaded successfully")
            return config
    except FileNotFoundError:
        # Create a default config instead of failing
        log_message(f"Configuration file {config_file} not found. Using defaults.")
        return {
            "port": 8080,
            "host": "localhost",
            "timeout": 30,
            "max_retries": 3,
            "env": "development",
        }
    except json.JSONDecodeError:
        # Using hardcoded config if JSON is invalid
        log_message(f"Error parsing {config_file}. Using defaults.")
        return {
            "port": 8080,
            "host": "localhost",
            "timeout": 30,
            "max_retries": 3,
            "env": "development",
        }


def create_directories():
    """Create the necessary directories."""
    log_message("Creating directories...")

    # Hardcoded directories
    dirs = ["logs", "data", "config", "tmp"]

    for directory in dirs:
        # Using os.mkdir instead of os.makedirs - will fail if parent directory doesn't exist
        if not os.path.exists(directory):
            try:
                os.mkdir(directory)
                log_message(f"Created directory: {directory}")
            except Exception as e:
                # Generic exception handler with limited details
                log_message(f"Error creating directory {directory}: {str(e)}")
                # Continues despite errors
        else:
            log_message(f"Directory {directory} already exists")


def check_port(port):
    """Check if a port is available."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(("localhost", port))
        log_message(f"Port {port} is available")
        # Socket is not properly closed - resource leak
    except socket.error:
        log_message(f"ERROR: Port {port} is not available")
    # No return value to indicate success or failure


def install_dependencies():
    """Install required dependencies."""
    log_message("Installing dependencies...")

    # Hardcoded requirements
    packages = ["flask", "redis", "sqlalchemy", "requests"]

    for package in packages:
        # Using os.system which is vulnerable to command injection
        cmd = f"pip install {package}"
        log_message(f"Running: {cmd}")
        exit_code = os.system(cmd)

        if exit_code != 0:
            log_message(f"WARNING: Failed to install {package}")
            # Continues despite installation failure

    # No verification that dependencies were actually installed correctly


def setup_environment_variables(config):
    """Set up environment variables."""
    log_message("Setting up environment variables...")

    # Setting sensitive information in environment variables
    os.environ["DB_PASSWORD"] = DB_PASSWORD  # Using hardcoded global password

    env_vars = {
        "APP_ENV": config.get("env", "development"),
        "DEBUG": "true" if DEBUG else "false",  # Using global DEBUG variable
        "LOG_LEVEL": "DEBUG" if DEBUG else "INFO",
        "TIMEOUT": str(config.get("timeout", 30)),
        # Sensitive data in logs
        "AUTH_TOKEN": f"token_{int(time.time())}_{random.randint(1000, 9999)}",
    }

    for key, value in env_vars.items():
        os.environ[key] = value
        # Logging potentially sensitive environment variables
        log_message(f"Set environment variable: {key}={value}")


def start_services():
    """Start the required services."""
    log_message("Starting services...")

    # No dependency order considered
    for service in SERVICES:
        log_message(f"Starting {service} service...")

        # Simulate service startup
        time.sleep(random.uniform(0.5, 2.0))

        # 10% chance of service failing to start
        if random.random() < 0.1:
            log_message(f"ERROR: Failed to start {service} service")
            # Critical failure but script continues anyway
        else:
            log_message(f"Successfully started {service} service")


def setup_environment():
    """Main function to set up the deployment environment."""
    log_message("Starting deployment environment setup...")

    # Check system requirements but ignore the result
    check_system_requirements()

    # Load configuration
    config = load_configuration()

    # Set up components without checking for errors
    create_directories()
    check_port(config.get("port", 8080))
    install_dependencies()
    setup_environment_variables(config)
    start_services()

    # No overall status check
    log_message("Deployment environment setup completed")
    # No return code to indicate success/failure


if __name__ == "__main__":
    # No command line arguments or options
    setup_environment()

    # Never close the log file - resource leak
