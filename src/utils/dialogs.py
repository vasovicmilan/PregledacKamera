from PySide6.QtWidgets import QMessageBox, QApplication
from PySide6.QtCore import Qt
import config.settings as settings


def _create_box(icon, title, message, parent=None):
    msg_box = QMessageBox(parent)  # 📌 roditelj (glavni prozor) za pravilno centriranje
    msg_box.setIcon(icon)
    msg_box.setWindowTitle(title)
    msg_box.setWindowFlag(Qt.WindowStaysOnTopHint)
    msg_box.setText(message)

    # Standardni Ok dugme sa srpskim tekstom
    msg_box.setStandardButtons(QMessageBox.Ok)
    ok_button = msg_box.button(QMessageBox.Ok)
    ok_button.setText("U redu")

    return msg_box


def show_info(message, title=None, parent=None):
    box = _create_box(QMessageBox.Information, title or settings.TITLE_SUCCESS, message, parent)
    box.exec()


def show_error(message, title=None, parent=None):
    box = _create_box(QMessageBox.Critical, title or settings.TITLE_ERROR, message, parent)
    box.exec()


def show_warning(message, title=None, parent=None):
    box = _create_box(QMessageBox.Warning, title or settings.TITLE_ERROR, message, parent)
    box.exec()


def show_confirm(message, title=None, yes_text="Da", no_text="Ne", parent=None):
    """
    Prikazuje dijalog potvrde sa prilagođenim dugmadima.
    Vraća True ako je kliknuto na dugme 'yes', inače False.
    """
    box = QMessageBox(parent)  # 📌 roditelj za centriranje
    box.setIcon(QMessageBox.Question)
    box.setWindowTitle(title or settings.TITLE_CONFIRM)
    box.setText(message)

    # Standardna Yes/No dugmad sa srpskim tekstom
    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    yes_button = box.button(QMessageBox.Yes)
    no_button = box.button(QMessageBox.No)
    yes_button.setText(yes_text)
    no_button.setText(no_text)
    box.setDefaultButton(no_button)

    box.setWindowFlag(Qt.WindowStaysOnTopHint)

    result = box.exec()
    return result == QMessageBox.Yes