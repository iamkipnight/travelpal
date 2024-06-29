 # file_watcher.py
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileWatcher(FileSystemEventHandler):
    def __init__(self, folder_to_watch):
        super().__init__()
        self.folder_to_watch = folder_to_watch

    def on_created(self, event):
        # Handle file creation event here
        print(f"New file created: {event.src_path}")

    def start(self):
        observer = Observer()
        observer.schedule(self, self.folder_to_watch, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()

if __name__ == "__main__":
    folder_to_watch = '/home/amigo/Desktop/mir/'
    file_watcher = FileWatcher(folder_to_watch)
    file_watcher.start()