from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *
from botcity.plugins.files import *
import os
import shutil
import pytesseract
from PIL import Image
import cv2
import re
from watchdog.observers import *
from watchdog.events import *

class Bot:
    def bot(self):
        # Monitoring Folder Activity
        class MonitorFolderEventHandler(FileSystemEventHandler):
                def __init__(self, callback):
                        self.callback = callback

                def on_created(self, event):
                        self.callback(event.src_path)

        class MonitorFolder:
                def __init__(self, folder_path, recursive=False):
                        self.folder_path = folder_path
                        self.recursive = recursive

                def start_monitoring(self, callback):
                        event_handler = MonitorFolderEventHandler(callback)
                        observer = Observer()
                        observer.schedule(event_handler, self.folder_path, self.recursive)
                        observer.start()

                        try:
                                while True:
                                        time.sleep(2)
                        except KeyboardInterrupt:
                                observer.stop()
                        observer.join()

                def executeReturn(pathFile):
                    time.sleep(2)
                    # File Handler Activity - import os
                    fileName = os.path.basename(pathFile)
                    newPath = os.path.join("C:\\Users\\HP\\Downloads\\Identidades\\Concluidos", fileName)
                    shutil.move(pathFile, newPath)


        instanceMonitor = MonitorFolder("C:\\Users\\HP\\Downloads\\Identidades\\Recebidos")
        instanceMonitor.start_monitoring(MonitorFolder.executeReturn)

        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()