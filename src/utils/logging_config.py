import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],  # log to the console
)


def get_logger(name):
    return logging.getLogger(name)
