import logging.config
import yaml
import os

def setup_logging(config_path="project_logging/config.yaml"):
    """Set up logging configuration from YAML file."""
    if not os.path.exists("logs"):
        os.makedirs("logs")  # Create logs directory if not exists

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        logging.config.dictConfig(config)

def get_logger(name="appLogger"):
    """Get logger with the specified name."""
    return logging.getLogger(name)
