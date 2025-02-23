import logging
import logging.config
import os
import yaml

def setup_logging(config_path="project_logging/config.yaml"):
    """Set up logging configuration from YAML file."""
    if not os.path.exists("logs"):
        os.makedirs("logs")  # Create logs directory if it doesn't exist

    # Load logging config from YAML
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        logging.config.dictConfig(config)

    # Ensure the root logger captures INFO level logs
    logging.getLogger().setLevel(logging.INFO)  # Make sure the root logger is set to INFO


def get_logger(name="appLogger"):
    """Get logger with the specified name."""
    return logging.getLogger(name)

