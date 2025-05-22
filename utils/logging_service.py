import logging
import os


def setup_logger(name, function):

    os.makedirs("./logs", exist_ok=True)
    # Create a logger
    logger = logging.getLogger(function)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    file_handler = logging.FileHandler(f"logs/{name}.log")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)

    return logger
