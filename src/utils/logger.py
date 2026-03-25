import logging
import os
from config.settings import LOG_FILE, LOG_LEVEL

# 🔹 mapiranje string -> logging level
LEVEL_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

# 🔹 napravi logs folder ako ne postoji
log_dir = os.path.dirname(LOG_FILE)
if log_dir and not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 🔹 kreiraj logger
logger = logging.getLogger("app_logger")
logger.setLevel(LEVEL_MAP.get(LOG_LEVEL, logging.ERROR))

# ❗ sprečava duplo logovanje (bitno kad se više puta importuje)
if not logger.handlers:

    # 📁 FILE HANDLER
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(LEVEL_MAP.get(LOG_LEVEL, logging.ERROR))

    # 🖥 CONSOLE HANDLER (za debug tokom razvoja)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 🎨 FORMAT
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # ➕ dodaj handlere
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# =========================
# 🔹 HELPER FUNKCIJE
# =========================

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