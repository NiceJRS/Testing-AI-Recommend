import os, sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".ui"):
            print("UI changed, restarting...")
            os.execv(sys.executable, ['python'] + sys.argv)


if __name__ == "__main__":
    from app import main

    observer = Observer()
    observer.schedule(ReloadHandler(), ".", recursive=True)
    observer.start()

    main()
