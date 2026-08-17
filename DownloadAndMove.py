import time
import os
import shutil
from watchdog.observers import OBSERVER
from watchdog.events import FileSystemEventHandler

class FileMovementHandler(FileSystemEventHandler):
    pass

event_handler = FileMovementHandler()