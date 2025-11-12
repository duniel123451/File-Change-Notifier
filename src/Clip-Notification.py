import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import playsound
from dotenv import load_dotenv
import sys
import os
from logger import logger

load_dotenv()

soundPath = os.getenv("SOUND_PATH")
watchingDirPath = os.getenv("WATCHING_DIR_PATH")

if not soundPath or not os.path.isfile(soundPath):
    logger.error("❌ SOUND_PATH not set or invalid.")
    sys.exit(1)
if not watchingDirPath or not os.path.isdir(watchingDirPath):
    logger.error("❌ WATCHING_DIR_PATH not set or invalid.")
    sys.exit(1)

logger.info(f"🎧 Watching folder: {watchingDirPath}")
logger.info(f"🔊 Using sound: {soundPath}")

class Watcher(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"📂 found new file: {event.src_path}")
            try:
                playsound.playsound(soundPath)
                logger.info("played sound!")
            except Exception as e:
                logger.warning(f"⚠️ error while trying to play the sound: {e}")

observer = Observer()
observer.schedule(Watcher(), watchingDirPath, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
