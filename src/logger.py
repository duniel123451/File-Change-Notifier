import logging
from logging.handlers import TimedRotatingFileHandler
import os

log_dir = os.path.join(os.path.dirname(__file__), "../logs")
os.makedirs(log_dir, exist_ok=True)

log_path = os.path.join(log_dir, "watcher.log")

logger = logging.getLogger("watcher")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(
    log_path,
    when="midnight",
    interval=1,
    backupCount=3,
    encoding="utf-8"
)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Service started")
