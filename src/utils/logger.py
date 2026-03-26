import logging
import os
from config import settings

# Map string log levels to logging constants
LEVEL_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

# Get the desired log level from settings (default INFO)
log_level_name = getattr(settings, 'LOG_LEVEL', 'INFO').upper()
log_level = LEVEL_MAP.get(log_level_name, logging.INFO)

# Ensure log directory exists
log_dir = os.path.dirname(settings.LOG_FILE)
if log_dir and not os.path.exists(log_dir):
    try:
        os.makedirs(log_dir, exist_ok=True)
    except OSError:
        # Fallback to current directory if we can't create the configured folder
        settings.LOG_FILE = os.path.join(os.getcwd(), 'app.log')
        log_dir = os.getcwd()
        print(f"Warning: Could not create log directory {log_dir}. Using {log_dir}")

# Create the logger
logger = logging.getLogger("app_logger")
logger.setLevel(log_level)

# Remove any existing handlers to avoid duplication
if logger.hasHandlers():
    logger.handlers.clear()

# File handler – log everything to file (DEBUG and above)
try:
    file_handler = logging.FileHandler(settings.LOG_FILE, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # Capture all messages (logger will filter)
    file_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s"))
    logger.addHandler(file_handler)
except Exception as e:
    print(f"Error creating log file {settings.LOG_FILE}: {e}. Logging to console only.")

# Console handler – output to terminal (DEBUG and above)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s"))
logger.addHandler(console_handler)

# Helper functions
def log_debug(message):
    logger.debug(message)

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message, exc: Exception = None):
    if exc:
        logger.error(f"{message} | Exception: {str(exc)}", exc_info=True)
    else:
        logger.error(message)

def log_critical(message, exc: Exception = None):
    if exc:
        logger.critical(f"{message} | Exception: {str(exc)}", exc_info=True)
    else:
        logger.critical(message)