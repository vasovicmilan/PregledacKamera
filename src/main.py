import sys
import traceback
import os

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

# UI
from ui.ui_mainwindow import Ui_MainWindow

# DB
from database.db import CameraDatabase

# REPOSITORY
from repositories.camera_repository import CameraRepository

# SERVICE
from services.camera_service import CameraService

# CONTROLLERS
from controllers.camera_controller import CameraController
from controllers.navigation_controller import NavigationController

# LOGGER
from utils.logger import log_error, log_info

# SETTINGS
from config import settings

# ✅ NOVO (umesto ui_helpers)
from utils.dialogs import show_error


# 🔥 GLOBAL ERROR HANDLER
def global_exception_handler(exc_type, exc_value, exc_traceback):
    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    # 📁 log
    log_error(error_msg)

    # 🪟 popup – pokušaj da centrira na glavni prozor ako postoji
    parent = None
    app = QApplication.instance()
    if app:
        for widget in app.topLevelWidgets():
            if isinstance(widget, QMainWindow):
                parent = widget
                break
    show_error("Došlo je do neočekivane greške.\nProveri log fajl.", parent=parent)


sys.excepthook = global_exception_handler


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 🔧 UI INIT
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 🗄 DB
        self.db = CameraDatabase()

        # 📦 LAYERS
        self.repository = CameraRepository(self.db)
        self.service = CameraService(self.repository)

        # 📊 Logovanje pokretanja i broja kamera
        camera_count = self.service.count()
        log_info(f"Aplikacija pokrenuta. Broj kamera u bazi: {camera_count}")

        # 🎮 CONTROLLERS
        self.camera_controller = CameraController(self, self.ui, self.service)
        self.navigation_controller = NavigationController(self.ui, self.camera_controller)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # naziv aplikacije
    app.setApplicationName(settings.APP_NAME)

    # 🔥 Postavi ikonicu aplikacije (ako postoji)
    icon_path = settings.resource_path("app.ico")
    if os.path.exists(icon_path):
        app_icon = QIcon(icon_path)
        app.setWindowIcon(app_icon)

    window = MainWindow()

    # Postavi ikonicu i za glavni prozor
    if os.path.exists(icon_path):
        window.setWindowIcon(app_icon)

    # fullscreen
    window.showMaximized()

    sys.exit(app.exec())