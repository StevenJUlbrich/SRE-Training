#!/usr/bin/env python3
"""
Fixed Service Deployment Environment Setup - SRE Best Practices

This script demonstrates proper SRE practices for setting up a microservice
deployment environment with proper error handling, logging, security,
and reliability features.

Key Improvements:
    - Structured logging
    - Proper error handling
    - Resource management
    - Secure configuration
    - Command-line options
"""

import argparse
import json
import logging
import os
import socket
import subprocess
import sys
import time
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("service-setup")

# Default services in dependency order
DEFAULT_SERVICES = ["database", "cache", "api", "worker"]


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Set up an environment for service deployment."
    )

    parser.add_argument(
        "--config", "-c", help="Path to configuration file", default="config.json"
    )

    parser.add_argument(
        "--log-file", "-l", help="Path to log file", default="deployment.log"
    )

    parser.add_argument(
        "--debug", "-d", action="store_true", help="Enable debug logging"
    )

    return parser.parse_args()


def setup_logging(log_file=None, debug=False):
    """Configure logging with file and console handlers."""
    log_level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(log_level)

    # Add file handler if specified
    if log_file:
        try:
            # Create parent directories if they don't exist
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(
                logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            )
            logger.addHandler(file_handler)
            logger.info(f"Logging to file: {log_file}")
            return file_handler
        except (OSError, PermissionError) as e:
            logger.error(f"Failed to set up file logging to {log_file}: {e}")
            logger.warning("Continuing with console logging only")

    return None


def load_configuration(config_file):
    """Load configuration from a JSON file."""
    logger.info(f"Loading configuration from {config_file}")

    # Check if config file exists
    if not os.path.exists(config_file):
        logger.error(f"Configuration file not found: {config_file}")
        return None

    try:
        with open(config_file, "r") as f:
            config = json.load(f)
        logger.info("Configuration loaded successfully")
        return config
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in configuration file: {e}")
        return None
    except OSError as e:
        logger.error(f"Failed to read configuration file: {e}")
        return None


def check_system_requirements():
    """Check if the system meets the deployment requirements."""
    logger.info("Checking system requirements...")

    # Check Python version
    python_version = sys.version_info
    min_python_version = (3, 7)
    logger.info(
        f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}"
    )

    if (python_version.major, python_version.minor) < min_python_version:
        min_ver_str = ".".join(map(str, min_python_version))
        logger.error(f"Python {min_ver_str} or higher is required")
        return False

    # Check disk space (simplified)
    try:
        if os.name == "posix":
            result = subprocess.run(
                ["df", "-h", "/"], check=True, capture_output=True, text=True
            )
            logger.info(f"Disk space check: {result.stdout.splitlines()[1]}")
    except subprocess.SubprocessError as e:
        logger.warning(f"Failed to check disk space: {e}")

    logger.info("System requirements check passed")
    return True


def create_directories(directories=None):
    """Create the necessary directories for deployment."""
    if directories is None:
        directories = ["logs", "data", "config", "tmp"]

    logger.info(f"Creating directories: {', '.join(directories)}")

    success = True
    for directory in directories:
        dir_path = Path(directory)
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {dir_path}")
        except OSError as e:
            logger.error(f"Failed to create directory {dir_path}: {e}")
            success = False

    return success


def check_port_availability(port):
    """Check if a port is available."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("localhost", port))
            logger.info(f"Port {port} is available")
            return True
    except socket.error:
        logger.error(f"Port {port} is not available")
        return False


def install_dependencies(packages=None):
    """Install required dependencies."""
    if packages is None:
        packages = ["flask", "redis", "sqlalchemy", "requests"]

    logger.info(f"Installing packages: {', '.join(packages)}")

    success = True
    for package in packages:
        try:
            # Use subprocess with list arguments for security
            logger.info(f"Installing package: {package}")
            process = subprocess.run(
                [sys.executable, "-m", "pip", "install", package],
                check=True,
                capture_output=True,
                text=True,
            )
            logger.info(f"Successfully installed {package}")
        except subprocess.SubprocessError as e:
            logger.error(f"Failed to install {package}: {e}")
            success = False

    return success


def setup_environment_variables(config):
    """Set up environment variables securely."""
    logger.info("Setting up environment variables")

    env_vars = config.get("env_vars", {})

    # Add standard variables
    env_vars.update(
        {
            "APP_ENV": config.get("env", "development"),
            "LOG_LEVEL": "DEBUG" if config.get("debug") else "INFO",
        }
    )

    # Set each environment variable
    for key, value in env_vars.items():
        os.environ[key] = str(value)

        # Don't log sensitive values
        if any(
            sensitive in key.lower()
            for sensitive in ["password", "secret", "key", "token"]
        ):
            logger.info(f"Set environment variable: {key}=********")
        else:
            logger.info(f"Set environment variable: {key}={value}")

    # Warn about environment variable scope
    logger.warning(
        "Note: Environment variables are only set for this process and its children. "
        "They will not persist after the script ends."
    )


def start_services(services=None, config=None):
    """Start the required services."""
    if services is None:
        services = DEFAULT_SERVICES

    if config is None:
        config = {}

    logger.info(f"Starting services: {', '.join(services)}")

    for service in services:
        logger.info(f"Starting {service} service...")

        # Get service-specific configuration
        port = config.get("port", 8080)

        # Check port availability
        if not check_port_availability(port):
            logger.error(f"Cannot start {service}: port {port} is not available")
            continue

        # Simulate service startup (in a real script, this would execute the actual service)
        time.sleep(1)
        logger.info(f"Successfully started {service} service")


def cleanup_resources(log_handler=None):
    """Clean up resources properly."""
    logger.info("Cleaning up resources...")

    # Close log file if it's open
    if log_handler:
        log_handler.close()
        logger.removeHandler(log_handler)
        logger.info("Closed log file")


def setup_environment():
    """Main function to set up the deployment environment."""
    # Parse command-line arguments
    args = parse_arguments()

    # Set up logging
    log_handler = setup_logging(args.log_file, args.debug)

    try:
        logger.info("Starting deployment environment setup...")

        # Check system requirements
        if not check_system_requirements():
            logger.error("System requirements check failed")
            return False

        # Load configuration
        config = load_configuration(args.config)
        if config is None:
            logger.error("Failed to load configuration")
            return False

        # Create necessary directories
        directories = config.get("directories", ["logs", "data", "config", "tmp"])
        if not create_directories(directories):
            logger.warning("Some directories could not be created")

        # Install dependencies
        packages = config.get("packages", ["flask", "redis", "sqlalchemy", "requests"])
        if not install_dependencies(packages):
            logger.warning("Some dependencies could not be installed")

        # Set up environment variables
        setup_environment_variables(config)

        # Start services
        services = config.get("services", DEFAULT_SERVICES)
        start_services(services, config)

        logger.info("Deployment environment setup completed successfully")
        return True

    except Exception as e:
        logger.error(f"Environment setup failed: {e}")
        return False

    finally:
        # Always clean up resources
        cleanup_resources(log_handler)


if __name__ == "__main__":
    success = setup_environment()
    sys.exit(0 if success else 1)
