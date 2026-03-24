import logging 
import os
from datetime import datetime
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
log_file = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")


logging.basicConfig(
    filename=log_file,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO)

def get_logger(name):
    """Returns a logger instance with the specified name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger