import time
from functools import wraps
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


def log_execution(func):
    """Logs the start and end of a method execution."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finished {func.__name__}")
        return result

    return wrapper


def handle_exceptions(func):
    """Logs exceptions and re-raises them."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise

    return wrapper


def measure_time(func):
    """Measures and logs the execution time of a method."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"It took {end_time - start_time:.4f} seconds")
        return result

    return wrapper
