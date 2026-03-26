from PySide6.QtWidgets import (
    QTableWidgetItem,
    QInputDialog,
    QFileDialog,
    QHeaderView
)

from PySide6.QtCore import Qt, QEvent, QObject, QDate, QDateTime

from PySide6.QtGui import QColor, QFont

from models.camera import Camera, CameraStatus
from utils.image_viewer import set_image_responsive
from utils.dialogs import show_info, show_error, show_warning, show_confirm
from utils.logger import log_info, log_warning, log_error
import config.settings as settings

from datetime import date


# 🔥 CUSTOM ITEM ZA NUMERIC SORT
class NumericTableWidgetItem(QTableWidgetItem):
    def __lt__(self, other):
        try:
            return int(self.text()) < int(other.text())
        except:
            return super().__lt__(other)


class CameraController(QObject):
    def __init__(self, window, ui, service):
        super().__init__()
        self.window = window
        self.ui = ui
        self.service = service

        self.edit_mode = False
        self.current_camera_id = None
        self.current_camera = None

        self._connect_signals()
        self.load_table()

        header = self.ui.cameraTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # 🔥 SORT ENABLE
        self.ui.cameraTable.setSortingEnabled(True)

        # 🔥 SAKRIJ REDNE BROJEVE
        self.ui.cameraTable.verticalHeader().setVisible(False)

        # 🔥 IMAGE LABEL - FULL FLEX
        self.ui.cameraImageLabel.setAlignment(Qt.AlignCenter)
        self.ui.cameraImageLabel.setMinimumSize(300, 300)
        self.ui.cameraImageLabel.setStyleSheet("border:1px solid #ccc;")

        # 🔥 PREVIEW
        self.ui.addCameraPreviewImageLabel.setMinimumSize(300, 300)
        self.ui.addCameraPreviewImageLabel.setMaximumSize(600, 600)
        self.ui.addCameraPreviewImageLabel.setAlignment(Qt.AlignCenter)
        self.ui.addCameraPreviewImageLabel.setStyleSheet("border:1px solid #ccc;")

        # 🔥 LISTEN NA RESIZE (KLJUČNO!)
        self.ui.cameraImageLabel.installEventFilter(self)

        # 🔥 Format datuma (srpski standard)
        self.ui.addCameraStartDateEdit.setDisplayFormat("dd.MM.yyyy")
        self.ui.addCameraEndDateEdit.setDisplayFormat("dd.MM.yyyy")
        self.ui.addCameraEndDateEdit.setSpecialValueText(" ")   # prazan tekst

        # 🖱️ Postavi kursor na ruku za datum pickere
        self.ui.addCameraStartDateEdit.setCursor(Qt.PointingHandCursor)
        self.ui.addCameraEndDateEdit.setCursor(Qt.PointingHandCursor)

        # 🔥 Dinamičko omogućavanje krajnjeg datuma u zavisnosti od statusa
        self.ui.addCameraActiveRadioButton.toggled.connect(self._update_end_date_state)
        self.ui.addCameraInactiveButton.toggled.connect(self._update_end_date_state)
        self.ui.addCameraDismantleRadioButton.toggled.connect(self._update_end_date_state)

        # 🔥 Postavi početno stanje: aktivna kamera, krajnji datum onemogućen
        self.reset_add_form()

        # ========== NOVI VIZUELNI DODACI ==========

        # 🖍️ Veći i podebljani font za ID i kod
        bold_font = QFont()
        bold_font.setPointSize(14)
        bold_font.setBold(True)
        self.ui.cameraIDLabel.setFont(bold_font)
        self.ui.cameraCodeLabel.setFont(bold_font)

        # 🎨 Naizmenične boje redova u tabeli i kursor na zaglavlju
        self.ui.cameraTable.setAlternatingRowColors(True)
        self.ui.cameraTable.setStyleSheet("""
            QTableWidget {
                alternate-background-color: #f2f2f2;
                selection-background-color: #cce5ff;
            }
            QHeaderView::section {
                background-color: #e0e0e0;
                padding: 4px;
                border: 1px solid #c0c0c0;
                font-weight: bold;
            }
        """)

        # Postavi kursor na zaglavlje
        header.setCursor(Qt.PointingHandCursor)

    # 🔥 EVENT FILTER → automatski resize slike
    def eventFilter(self, obj, event):
        if obj == self.ui.cameraImageLabel and event.type() == QEvent.Resize:
            if self.current_camera and self.current_camera.image_path:
                set_image_responsive(
                    self.ui.cameraImageLabel,
                    self.current_camera.image_path,
                    min_size=300,
                    max_size=2000  # 🔥 dozvoli veliki prikaz
                )
        return super().eventFilter(obj, event)

    # 🔥 Dinamičko omogućavanje/onemogućavanje polja za krajnji datum
    def _update_end_date_state(self):
        # Proveri da li je izabran status DISMANTLED
        if self.ui.addCameraDismantleRadioButton.isChecked():
            # Samo za skinutu kameru omogući polje
            self.ui.addCameraEndDateEdit.setEnabled(True)
        else:
            # Za aktivnu i neaktivnu onemogući polje i obriši vrednost
            self.ui.addCameraEndDateEdit.setEnabled(False)
            self.ui.addCameraEndDateEdit.setDateTime(QDateTime())

    # 🎨 STATUS BOJA
    def _get_status_color(self, status):
        status = status.lower()

        if status == "active":
            return QColor("#27ae60")
        elif status == "inactive":
            return QColor("#c0392b")
        elif status == "dismantled":
            return QColor("#2980b9")

        return QColor("#000000")

    # 🎯 STATUS FORMAT
    def _format_status(self, status):
        status = status.lower()

        if status == "active":
            return "✔ ACTIVE"
        elif status == "inactive":
            return "❌ INACTIVE"
        elif status == "dismantled":
            return "🔧 DISMANTLED"

        return status.upper()

    # 🔧 LABEL HELPER
    def _set_label_value(self, label, value):
        base = label.text()
        if ":" in base:
            base = base.split(":")[0]
        # Make the value bold and slightly larger (e.g., 12pt)
        label.setText(f"{base}: <b><span style='font-size: 16pt'>{value or ''}</span></b>")

    # 🔧 MODE
    def _set_mode(self, edit=False):
        if edit:
            self.ui.addCameraLabel.setText(settings.FORM_EDIT_TITLE)
            self.ui.addCameraButton.setText(settings.FORM_EDIT_BUTTON)
        else:
            self.ui.addCameraLabel.setText(settings.FORM_ADD_TITLE)
            self.ui.addCameraButton.setText(settings.FORM_ADD_BUTTON)

    # 🔗 SIGNALS
    def _connect_signals(self):
        self.ui.addCameraButton.clicked.connect(self.save_camera)

        self.ui.searchButton.clicked.connect(self.search_camera)
        self.ui.searchEdit.returnPressed.connect(self.search_camera)

        self.ui.cameraDeleteButton.clicked.connect(self.delete_camera)
        self.ui.cameraEditButton.clicked.connect(self.edit_camera)
        self.ui.cameraControllButton.clicked.connect(self.control_camera)
        self.ui.cameraTable.itemSelectionChanged.connect(self.load_selected_camera)

        self.ui.addCameraImageUploadButton.clicked.connect(self.select_image)
        self.ui.addCameraGoBackButton.clicked.connect(self.go_back_to_list)

    # 📊 LOAD
    def load_table(self):
        cameras = self.service.get_all_for_table()
        self._populate_table(cameras)

    # 🔍 SEARCH
    def search_camera(self):
        term = self.ui.searchEdit.text().strip()

        if not term:
            self.load_table()
            return

        try:
            status = None

            if term.lower() in settings.STATUS_OPTIONS:
                status = term.lower()
                term = None

            cameras = self.service.search(term=term, status=status)

            if not cameras:
                show_warning("Nema rezultata za pretragu.", parent=self.window)
                self.ui.cameraTable.setRowCount(0)
                self._clear_details()
                log_info(f"Pretraga bez rezultata: term='{term}', status='{status}'")
                return

            self._populate_table(cameras)
            log_info(f"Pretraga uspešna: pronađeno {len(cameras)} kamera, term='{term}', status='{status}'")

        except Exception as e:
            show_error(str(e), parent=self.window)
            log_error(f"Greška pri pretrazi: {e}")

    # 📋 TABLE
    def _populate_table(self, cameras):
        table = self.ui.cameraTable

        table.setSortingEnabled(False)

        table.setRowCount(0)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["ID", "Kod", "IP", "Lokacija", "Status"])

        if not cameras:
            table.setSortingEnabled(True)
            self._clear_details()
            return

        for row_idx, cam in enumerate(cameras):
            table.insertRow(row_idx)

            id_item = NumericTableWidgetItem(str(cam["id"]))
            table.setItem(row_idx, 0, id_item)

            table.setItem(row_idx, 1, QTableWidgetItem(cam["code"]))
            table.setItem(row_idx, 2, QTableWidgetItem(cam["ip_address"]))
            table.setItem(row_idx, 3, QTableWidgetItem(cam["location"]))

            status_text = cam["status"]
            formatted = self._format_status(status_text)

            status_item = QTableWidgetItem(formatted)

            color = self._get_status_color(status_text)
            status_item.setForeground(color)

            font = QFont()
            font.setBold(True)
            status_item.setFont(font)

            table.setItem(row_idx, 4, status_item)

        table.setSortingEnabled(True)

    # 🧹 ČIŠĆENJE DETALJA KAMERE
    def _clear_details(self):
        """Resetuje sve detalje kamere na prazno i briše sliku."""
        self.current_camera = None
        self._set_label_value(self.ui.cameraIDLabel, "")
        self._set_label_value(self.ui.cameraCodeLabel, "")
        self._set_label_value(self.ui.cameraTypeLabel, "")
        self._set_label_value(self.ui.cameraLocationLabel, "")
        self._set_label_value(self.ui.cameraPurposeLabel, "")
        self._set_label_value(self.ui.cameraFunctioLabel, "")
        self._set_label_value(self.ui.cameraCoverageLabel, "")
        self._set_label_value(self.ui.cameraServerLabel, "")
        self._set_label_value(self.ui.cameraIPaddressLabel, "")
        self._set_label_value(self.ui.cameraRackLabel, "")
        self._set_label_value(self.ui.cameraRetentionLabel, "")
        self._set_label_value(self.ui.cameraModelLabel, "")
        self._set_label_value(self.ui.cameraStartDateLabel, "")
        self._set_label_value(self.ui.cameraEndDateLabel, "")
        self._set_label_value(self.ui.cameraStatusLabel, "")
        self._set_label_value(self.ui.cameraNoteLabel, "")
        self._set_label_value(self.ui.cameraActionLabel, "")
        self.ui.cameraImageLabel.clear()
        self.ui.cameraImageLabel.setText("Slika")

    # 📄 SELECT
    def load_selected_camera(self):
        selected = self.ui.cameraTable.selectedItems()
        if not selected:
            self._clear_details()
            return

        row = selected[0].row()
        item = self.ui.cameraTable.item(row, 0)

        if not item:
            return

        try:
            camera_id = int(item.text())
        except:
            return

        camera = self.service.get_by_id(camera_id)
        if camera:
            self._fill_details(camera)

    # 🧾 DETAILS
    def _fill_details(self, camera: Camera):
        self.current_camera = camera

        self._set_label_value(self.ui.cameraIDLabel, camera.id)
        self._set_label_value(self.ui.cameraCodeLabel, camera.code)
        self._set_label_value(self.ui.cameraTypeLabel, camera.camera_type)
        self._set_label_value(self.ui.cameraLocationLabel, camera.location)
        self._set_label_value(self.ui.cameraPurposeLabel, camera.purpose)
        self._set_label_value(self.ui.cameraFunctioLabel, camera.camera_function)
        self._set_label_value(self.ui.cameraCoverageLabel, camera.coverage)

        self._set_label_value(self.ui.cameraServerLabel, camera.server)
        self._set_label_value(self.ui.cameraIPaddressLabel, camera.ip_address)
        self._set_label_value(self.ui.cameraRackLabel, camera.rack)
        self._set_label_value(self.ui.cameraRetentionLabel, camera.retention_days)
        self._set_label_value(self.ui.cameraModelLabel, camera.model)

        self._set_label_value(self.ui.cameraStartDateLabel, camera.start_date)
        self._set_label_value(self.ui.cameraEndDateLabel, camera.end_date)

        status = camera.health_status.value
        formatted = self._format_status(status)

        self._set_label_value(self.ui.cameraStatusLabel, formatted)

        color = self._get_status_color(status)

        self.ui.cameraStatusLabel.setStyleSheet(f"""
            color: {color.name()};
            font-weight: bold;
        """)

        self._set_label_value(self.ui.cameraNoteLabel, camera.note)
        self._set_label_value(self.ui.cameraActionLabel, camera.action)

        # 🔥 GLAVNA SLIKA (MAX SPACE)
        set_image_responsive(
            self.ui.cameraImageLabel,
            camera.image_path,
            min_size=300,
            max_size=2000
        )

    # 🔥 SELECT AFTER SAVE
    def _select_camera_in_table(self, camera_id):
        table = self.ui.cameraTable

        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item and int(item.text()) == camera_id:
                table.selectRow(row)
                return

    # 🧹 GO BACK TO CAMERA LIST (RESET AND SWITCH)
    def go_back_to_list(self):
        self.reset_add_form()
        self.ui.stackedWidget.setCurrentWidget(self.ui.cameraList)

    # ➕ SAVE
    def save_camera(self):
        try:
            camera = self._get_camera_from_form()

            saved_id = None

            if self.edit_mode:
                camera.id = self.current_camera_id
                self.service.update_camera(camera)
                saved_id = camera.id
                show_info(settings.MSG_CAMERA_UPDATED, parent=self.window)
            else:
                saved_id = self.service.create_camera(camera)
                show_info(settings.MSG_CAMERA_ADDED, parent=self.window)

            self.edit_mode = False
            self.current_camera_id = None

            self.load_table()

            if saved_id:
                self._select_camera_in_table(saved_id)

            self._clear_form()
            self._set_mode(False)

            self.ui.stackedWidget.setCurrentWidget(self.ui.cameraList)

        except Exception as e:
            show_error(str(e), parent=self.window)
            log_error(f"Greška pri čuvanju kamere: {e}")

    # ✏️ EDIT
    def edit_camera(self):
        selected = self.ui.cameraTable.selectedItems()

        if not selected:
            show_warning(settings.MSG_SELECT_CAMERA, parent=self.window)
            log_warning("Pokušaj izmene kamere bez selektovanog reda.")
            return

        row = selected[0].row()
        item = self.ui.cameraTable.item(row, 0)

        if not item:
            return

        camera_id = int(item.text())

        camera = self.service.get_by_id(camera_id)
        if not camera:
            log_warning(f"Pokušaj izmene nepostojeće kamere ID {camera_id}")
            return

        self.edit_mode = True
        self.current_camera_id = camera_id

        self._fill_form(camera)
        self._set_mode(True)

        self.ui.stackedWidget.setCurrentWidget(self.ui.addCamera)

    # 📷 IMAGE
    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.window,
            "Izaberi sliku",
            "",
            settings.IMAGE_FILTER
        )

        if file_path:
            self.ui.addCameraImageLineEdit.setText(file_path)

            set_image_responsive(
                self.ui.addCameraPreviewImageLabel,
                file_path,
                min_size=300,
                max_size=600
            )

    # ⚙️ STATUS
    def control_camera(self):
        selected = self.ui.cameraTable.selectedItems()

        if not selected:
            show_warning(settings.MSG_SELECT_CAMERA, parent=self.window)
            log_warning("Pokušaj promene statusa bez selektovane kamere.")
            return

        row = selected[0].row()
        camera_id = int(self.ui.cameraTable.item(row, 0).text())

        # Display names in Serbian, mapped to actual status values
        status_display = ["Aktivna", "Neaktivna", "Skinuta"]
        actual_statuses = settings.STATUS_OPTIONS  # ["active", "inactive", "dismantled"]

        selected_display, ok = QInputDialog.getItem(
            self.window,
            "Promena statusa",
            "Izaberite status:",
            status_display,
            0,
            False
        )

        if ok:
            # Find the index of the selected display name and get the actual status
            index = status_display.index(selected_display)
            actual_status = actual_statuses[index]
            self.service.update_status(camera_id, actual_status)
            self.load_table()

    # ❌ DELETE
    def delete_camera(self):
        selected = self.ui.cameraTable.selectedItems()

        if not selected:
            show_warning(settings.MSG_SELECT_CAMERA, parent=self.window)
            log_warning("Pokušaj brisanja kamere bez selektovanog reda.")
            return

        row = selected[0].row()
        camera_id = int(self.ui.cameraTable.item(row, 0).text())

        # 🔥 Prilagođena potvrda sa dugmadima "Izbriši" i "Odustani"
        confirm = show_confirm(
            settings.MSG_DELETE_CONFIRM,
            yes_text="Izbriši",
            no_text="Odustani",
            parent=self.window
        )

        if confirm:
            self.service.delete(camera_id)
            self.load_table()   # load_table će pozvati _populate_table, koja ako nema kamera čisti detalje

    # 🧾 FORM
    def _fill_form(self, camera):
        self.ui.addCameraCodeLineEdit.setText(camera.code)
        self.ui.addCameraIPAddressLineEdit.setText(camera.ip_address)
        self.ui.addCameraRackLineEdit.setText(camera.rack or "")
        self.ui.addCameraServerLineEdit.setText(camera.server or "")
        self.ui.addCameraLocationLineEdit.setText(camera.location or "")
        self.ui.addCameraCoverageLineEdit.setText(camera.coverage or "")
        self.ui.addCameraTypeLineEdit.setText(camera.camera_type or "")
        self.ui.addCameraPurposeLineEdit.setText(camera.purpose or "")
        self.ui.addCameraFunctionLineEdit.setText(camera.camera_function or "")
        self.ui.addCameraModelLineEdit.setText(camera.model or "")
        self.ui.addCameraRetentionLineEdit.setText(str(camera.retention_days or ""))
        self.ui.addCameraNoteEdit.setText(camera.note or "")
        self.ui.addCameraActionTextEdit.setText(camera.action or "")
        self.ui.addCameraImageLineEdit.setText(camera.image_path or "")

        # ✅ Start date – postavi iz kamere ili danas ako je prazno
        if camera.start_date:
            start_qdate = QDate.fromString(camera.start_date, "yyyy-MM-dd")
            if start_qdate.isValid():
                self.ui.addCameraStartDateEdit.setDate(start_qdate)
            else:
                self.ui.addCameraStartDateEdit.setDate(QDate.currentDate())
        else:
            self.ui.addCameraStartDateEdit.setDate(QDate.currentDate())

        # ✅ End date – postavi iz kamere ili ostavi prazno (invalid)
        if camera.end_date:
            end_qdate = QDate.fromString(camera.end_date, "yyyy-MM-dd")
            if end_qdate.isValid():
                self.ui.addCameraEndDateEdit.setDate(end_qdate)
            else:
                self.ui.addCameraEndDateEdit.setDateTime(QDateTime())
        else:
            self.ui.addCameraEndDateEdit.setDateTime(QDateTime())

        # ✅ Postavi status radio dugmad
        if camera.health_status == CameraStatus.ACTIVE:
            self.ui.addCameraActiveRadioButton.setChecked(True)
        elif camera.health_status == CameraStatus.INACTIVE:
            self.ui.addCameraInactiveButton.setChecked(True)
        elif camera.health_status == CameraStatus.DISMANTLED:
            self.ui.addCameraDismantleRadioButton.setChecked(True)

        # ✅ Nakon što su radio dugmad postavljena, ažuriraj stanje end_date polja
        self._update_end_date_state()

        set_image_responsive(
            self.ui.addCameraPreviewImageLabel,
            camera.image_path,
            min_size=300,
            max_size=600
        )

    # 🧠 MODEL
    def _get_camera_from_form(self):
        # Start date: uzmi iz widgeta ili postavi danas ako je prazan
        start_qdate = self.ui.addCameraStartDateEdit.date()
        if start_qdate.isValid():
            start_date = start_qdate.toString("yyyy-MM-dd")
        else:
            start_date = date.today().strftime("%Y-%m-%d")

        # Odredi status
        status = self._get_status()

        # End date: ako je status ACTIVE ili INACTIVE, uvek None; samo DISMANTLED sme imati end_date
        if status in (CameraStatus.ACTIVE, CameraStatus.INACTIVE):
            end_date = None
        else:
            end_qdate = self.ui.addCameraEndDateEdit.date()
            if end_qdate.isValid():
                end_date = end_qdate.toString("yyyy-MM-dd")
            else:
                end_date = None

        return Camera(
            code=self.ui.addCameraCodeLineEdit.text(),
            ip_address=self.ui.addCameraIPAddressLineEdit.text(),
            rack=self.ui.addCameraRackLineEdit.text(),
            server=self.ui.addCameraServerLineEdit.text(),
            location=self.ui.addCameraLocationLineEdit.text(),
            coverage=self.ui.addCameraCoverageLineEdit.text(),
            camera_type=self.ui.addCameraTypeLineEdit.text(),
            purpose=self.ui.addCameraPurposeLineEdit.text(),
            camera_function=self.ui.addCameraFunctionLineEdit.text(),
            model=self.ui.addCameraModelLineEdit.text(),
            retention_days=self._parse_int(self.ui.addCameraRetentionLineEdit.text()),
            health_status=status,
            note=self.ui.addCameraNoteEdit.toPlainText(),
            action=self.ui.addCameraActionTextEdit.toPlainText(),
            image_path=self.ui.addCameraImageLineEdit.text(),
            start_date=start_date,
            end_date=end_date
        )

    def _get_status(self):
        if self.ui.addCameraActiveRadioButton.isChecked():
            return CameraStatus.ACTIVE
        elif self.ui.addCameraInactiveButton.isChecked():
            return CameraStatus.INACTIVE
        elif self.ui.addCameraDismantleRadioButton.isChecked():
            return CameraStatus.DISMANTLED
        return None

    def _parse_int(self, value):
        try:
            return int(value)
        except:
            return None

    # 🧹 CLEAR
    def _clear_form(self):
        self.ui.addCameraCodeLineEdit.clear()
        self.ui.addCameraIPAddressLineEdit.clear()
        self.ui.addCameraRackLineEdit.clear()
        self.ui.addCameraServerLineEdit.clear()
        self.ui.addCameraLocationLineEdit.clear()
        self.ui.addCameraCoverageLineEdit.clear()
        self.ui.addCameraTypeLineEdit.clear()
        self.ui.addCameraPurposeLineEdit.clear()
        self.ui.addCameraFunctionLineEdit.clear()
        self.ui.addCameraModelLineEdit.clear()
        self.ui.addCameraRetentionLineEdit.clear()
        self.ui.addCameraNoteEdit.clear()
        self.ui.addCameraActionTextEdit.clear()
        self.ui.addCameraImageLineEdit.clear()

        # ✅ Start date → današnji datum
        self.ui.addCameraStartDateEdit.setDate(QDate.currentDate())

        # ✅ End date → invalid (prazno)
        self.ui.addCameraEndDateEdit.setDateTime(QDateTime())

        self.ui.addCameraPreviewImageLabel.clear()

        # ✅ Postavi status "Aktivna" kao podrazumevani
        self.ui.addCameraActiveRadioButton.setChecked(True)
        # Ova linija automatski poziva _update_end_date_state jer je signal povezan

    def reset_add_form(self):
        self.edit_mode = False
        self.current_camera_id = None
        self.current_camera = None
        self._clear_form()
        self._set_mode(False)