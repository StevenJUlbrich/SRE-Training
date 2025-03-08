#!/usr/bin/env python3
"""
Environment Setup Script - Basic Scripting

This module provides functionality to set up a development or testing environment
by installing dependencies, configuring settings, and preparing the workspace.

Key Concepts:
    - Package installation and dependency management
    - Environment variable configuration
    - Directory structure creation
    - Error handling and logging
    - Cross-platform compatibility

Learning Objectives:
    - Understand how to automate environment setup tasks
    - Learn to manage dependencies with pip
    - Practice proper error handling techniques
    - Recognize the importance of logging during setup
"""

import argparse
import json
import logging
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class EnvironmentSetup:
    """
    A class to handle environment setup tasks.

    This class encapsulates all functionality related to setting up a development
    or testing environment, making it easier to organize and track setup steps.
    """

    def __init__(
        self,
        config_file: Optional[str] = None,
        requirements_file: Optional[str] = None,
        workspace_dir: Optional[str] = None,
        env_vars: Optional[Dict[str, str]] = None,
        verbose: bool = False,
    ):
        """
        Initialize the environment setup with configuration options.

        Args:
            config_file: Path to a JSON configuration file (optional)
            requirements_file: Path to a requirements.txt file (optional)
            workspace_dir: Directory to set up as the workspace (optional)
            env_vars: Dictionary of environment variables to set (optional)
            verbose: Whether to enable verbose output
        """
        self.config: Dict[str, Any] = {}
        self.requirements_file = requirements_file
        self.workspace_dir = workspace_dir
        self.env_vars = env_vars or {}

        # Set up logging level based on verbosity
        if verbose:
            logger.setLevel(logging.DEBUG)

        # Load configuration from file if provided
        if config_file:
            self._load_config(config_file)

    def _load_config(self, config_file: str) -> None:
        """
        Load configuration from a JSON file.

        Args:
            config_file: Path to the JSON configuration file

        Raises:
            FileNotFoundError: If the config file does not exist
            json.JSONDecodeError: If the config file is not valid JSON
        """
        try:
            with open(config_file, "r") as f:
                self.config = json.load(f)

            # Update instance variables with config values if not already set
            if not self.requirements_file and "requirements_file" in self.config:
                self.requirements_file = self.config["requirements_file"]

            if not self.workspace_dir and "workspace_dir" in self.config:
                self.workspace_dir = self.config["workspace_dir"]

            if "env_vars" in self.config:
                # Update env_vars, keeping any that were passed directly to __init__
                config_env_vars = self.config["env_vars"]
                for key, value in config_env_vars.items():
                    if key not in self.env_vars:
                        self.env_vars[key] = value

            logger.debug(f"Loaded configuration from {config_file}")

        except FileNotFoundError:
            logger.error(f"Config file not found: {config_file}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            raise

    def install_dependencies(self) -> bool:
        """
        Install Python dependencies using pip.

        Returns:
            bool: True if successful, False otherwise

        Raises:
            FileNotFoundError: If the requirements file does not exist
        """
        if not self.requirements_file:
            logger.warning(
                "No requirements file specified. Skipping dependency installation."
            )
            return True

        if not os.path.isfile(self.requirements_file):
            logger.error(f"Requirements file not found: {self.requirements_file}")
            raise FileNotFoundError(
                f"Requirements file not found: {self.requirements_file}"
            )

        logger.info(f"Installing dependencies from {self.requirements_file}...")

        try:
            # Use subprocess to run pip
            cmd = [sys.executable, "-m", "pip", "install", "-r", self.requirements_file]

            # Run the command and capture output
            process = subprocess.run(
                cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            # Log output
            logger.debug(process.stdout)

            logger.info("Successfully installed dependencies.")
            return True

        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install dependencies: {e}")
            logger.error(f"Error output: {e.stderr}")
            return False

    def setup_workspace(self) -> bool:
        """
        Set up the workspace directory structure.

        Returns:
            bool: True if successful, False otherwise
        """
        if not self.workspace_dir:
            logger.warning(
                "No workspace directory specified. Skipping workspace setup."
            )
            return True

        try:
            workspace_path = Path(self.workspace_dir)

            # Create the main workspace directory if it doesn't exist
            if not workspace_path.exists():
                workspace_path.mkdir(parents=True)
                logger.info(f"Created workspace directory: {workspace_path}")
            else:
                logger.info(f"Workspace directory already exists: {workspace_path}")

            # Create standard subdirectories from config or defaults
            subdirs = self.config.get(
                "workspace_subdirs", ["data", "logs", "config", "scripts"]
            )

            for subdir in subdirs:
                subdir_path = workspace_path / subdir
                if not subdir_path.exists():
                    subdir_path.mkdir(parents=True)
                    logger.info(f"Created subdirectory: {subdir_path}")

            # Copy template files if specified
            if "template_files" in self.config:
                for template in self.config["template_files"]:
                    src = template.get("src")
                    dest = template.get("dest")

                    if src and dest:
                        dest_path = workspace_path / dest

                        # Create parent directories if they don't exist
                        dest_path.parent.mkdir(parents=True, exist_ok=True)

                        # Copy the file
                        shutil.copy2(src, dest_path)
                        logger.info(f"Copied template file from {src} to {dest_path}")

            return True

        except (OSError, shutil.Error) as e:
            logger.error(f"Failed to set up workspace: {e}")
            return False

    def set_environment_variables(self) -> bool:
        """
        Set environment variables for the current process.

        Note: These variables only affect the current process and its children.
        They do not persist after the script ends.

        Returns:
            bool: True if successful, False otherwise
        """
        if not self.env_vars:
            logger.warning(
                "No environment variables specified. Skipping environment variable setup."
            )
            return True

        try:
            for key, value in self.env_vars.items():
                os.environ[key] = value
                logger.info(f"Set environment variable: {key}={value}")

            # Also log all environment variables in debug mode
            logger.debug("Current environment variables:")
            for key, value in sorted(os.environ.items()):
                logger.debug(f"  {key}={value}")

            return True

        except Exception as e:
            logger.error(f"Failed to set environment variables: {e}")
            return False

    def run_custom_commands(self) -> bool:
        """
        Run custom setup commands from the configuration.

        Returns:
            bool: True if all commands succeeded, False otherwise
        """
        if "custom_commands" not in self.config:
            logger.info(
                "No custom commands specified. Skipping custom command execution."
            )
            return True

        commands = self.config["custom_commands"]
        if not commands:
            return True

        success = True

        for i, cmd_config in enumerate(commands, 1):
            cmd = cmd_config.get("command")
            desc = cmd_config.get("description", f"Custom command {i}")
            ignore_errors = cmd_config.get("ignore_errors", False)

            if not cmd:
                logger.warning(f"Skipping empty command at position {i}")
                continue

            logger.info(f"Running: {desc}")

            try:
                # Use shell=True for complex commands with pipes, redirects, etc.
                shell = cmd_config.get("use_shell", False)

                process = subprocess.run(
                    cmd if shell else cmd.split(),
                    shell=shell,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )

                logger.info(f"Successfully executed: {desc}")
                logger.debug(process.stdout)

            except subprocess.CalledProcessError as e:
                logger.error(f"Command failed: {desc}")
                logger.error(f"Error output: {e.stderr}")

                if not ignore_errors:
                    success = False
                    if cmd_config.get("fail_fast", False):
                        logger.error(
                            "Stopping custom command execution due to fail_fast setting."
                        )
                        break

        return success

    def setup_all(self) -> bool:
        """
        Run all setup steps in sequence.

        Returns:
            bool: True if all steps succeeded, False otherwise
        """
        logger.info("Starting environment setup...")

        # Setup steps with their corresponding methods
        steps = [
            ("Installing dependencies", self.install_dependencies),
            ("Setting up workspace", self.setup_workspace),
            ("Setting environment variables", self.set_environment_variables),
            ("Running custom commands", self.run_custom_commands),
        ]

        success = True

        for step_name, step_func in steps:
            logger.info(f"Step: {step_name}")

            try:
                step_success = step_func()
                if not step_success:
                    logger.error(f"Step failed: {step_name}")
                    success = False

                    # Check if we should continue after errors
                    if self.config.get("fail_fast", False):
                        logger.error("Stopping setup due to fail_fast setting.")
                        break

            except Exception as e:
                logger.error(f"Error in step {step_name}: {e}")
                success = False

                if self.config.get("fail_fast", False):
                    logger.error("Stopping setup due to fail_fast setting.")
                    break

        status = "successfully" if success else "with errors"
        logger.info(f"Environment setup completed {status}.")

        return success


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments for the environment setup script.

    Returns:
        argparse.Namespace: Parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description="Set up a development or testing environment.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("--config", type=str, help="Path to a JSON configuration file")

    parser.add_argument(
        "--requirements", type=str, help="Path to a requirements.txt file"
    )

    parser.add_argument(
        "--workspace", type=str, help="Directory to set up as the workspace"
    )

    parser.add_argument(
        "--env",
        action="append",
        nargs=2,
        metavar=("KEY", "VALUE"),
        help="Environment variable to set (can be specified multiple times)",
    )

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )

    return parser.parse_args()


def main() -> int:
    """
    Main function to run the environment setup script.

    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    args = parse_arguments()

    # Convert environment variables list to dictionary
    env_vars = {}
    if args.env:
        for key, value in args.env:
            env_vars[key] = value

    try:
        # Display system information
        logger.info(f"System: {platform.system()} {platform.release()}")
        logger.info(f"Python: {platform.python_version()}")

        # Create environment setup instance
        setup = EnvironmentSetup(
            config_file=args.config,
            requirements_file=args.requirements,
            workspace_dir=args.workspace,
            env_vars=env_vars,
            verbose=args.verbose,
        )

        # Run all setup steps
        success = setup.setup_all()

        return 0 if success else 1

    except Exception as e:
        logger.error(f"Environment setup failed: {e}")
        if args.verbose:
            import traceback

            logger.error(traceback.format_exc())
        return 1


if __name__ == "__main__":
    sys.exit(main())
