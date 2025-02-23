import sys
import os
from project_logging import setup_logging, get_logger

# Initialize logging
setup_logging()

# Get logger
logger = get_logger()

def main():
    logger.debug("Starting the main function.")
    logger.info("Application started.")
    logger.warning("This is a warning from main.")
    logger.error("This is an error from main.")
    logger.critical("This is a critical message from main.")
    logger.info("Application finished.")

if __name__ == "__main__":
    main()
