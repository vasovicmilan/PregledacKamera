from utils.validators import validate_camera, ValidationError
from utils.image_handler import process_image
from models.camera import Camera, CameraStatus
from utils.logger import log_warning
import os


class CameraService:
    def __init__(self, repository):
        self.repository = repository

    # ➕ CREATE
    def create_camera(self, camera):
        if self.repository.exists_by_code(camera.code):
            raise ValidationError("Kamera sa ovim kodom već postoji.")

        self._normalize(camera)

        processed_path = process_image(camera.image_path, camera.code)
        camera.image_path = processed_path

        validate_camera(camera)

        # 🔥 repo mora da vrati lastrowid
        new_id = self.repository.add(camera)
        return new_id

    # ✏️ UPDATE
    def update_camera(self, camera):
        existing = self.repository.get_by_id(camera.id)

        if not existing:
            raise ValidationError("Kamera ne postoji.")

        if camera.code != existing.code:
            if self.repository.exists_by_code(camera.code):
                raise ValidationError("Kamera sa ovim kodom već postoji.")

        self._normalize(camera)

        # 📷 SLIKA
        if camera.image_path and camera.image_path != existing.image_path:

            new_path = process_image(camera.image_path, camera.code)

            if new_path:
                if existing.image_path and os.path.isfile(existing.image_path):
                    try:
                        os.remove(existing.image_path)
                    except Exception as e:
                        log_warning(f"Greška pri brisanju stare slike: {e}")

                camera.image_path = new_path
            else:
                camera.image_path = existing.image_path
        else:
            camera.image_path = existing.image_path

        validate_camera(camera)

        self.repository.update(camera)
        return camera.id

    # 📊 LIST (SORTIRANJE)
    def get_all_for_table(self, order_by="id", order_dir="ASC"):
        order_by = self._sanitize_order_by(order_by)
        order_dir = self._sanitize_order_dir(order_dir)

        return self.repository.get_all_for_table(order_by, order_dir)

    # 📄 DETAIL
    def get_by_id(self, camera_id):
        return self.repository.get_by_id(camera_id)

    # 🔍 SEARCH (TERM + STATUS + SORT)
    def search(self, term=None, status=None, order_by="id", order_dir="ASC"):
        order_by = self._sanitize_order_by(order_by)
        order_dir = self._sanitize_order_dir(order_dir)

        return self.repository.search(term, status, order_by, order_dir)

    # ❌ DELETE
    def delete(self, camera_id):
        camera = self.repository.get_by_id(camera_id)

        if not camera:
            raise ValidationError("Kamera ne postoji.")

        if camera.image_path and os.path.isfile(camera.image_path):
            try:
                os.remove(camera.image_path)
            except Exception as e:
                log_warning(f"Greška pri brisanju slike: {e}")

        self.repository.delete(camera_id)

    # ⚙️ STATUS
    def update_status(self, camera_id, status):
        camera = self.repository.get_by_id(camera_id)

        if not camera:
            raise ValidationError("Kamera ne postoji.")

        try:
            new_status = CameraStatus(status.lower())
        except Exception:
            raise ValidationError("Nevalidan status.")

        # Ako se menja status u ACTIVE, obavezno obriši end_date
        if new_status == CameraStatus.ACTIVE:
            camera.end_date = None

        camera.health_status = new_status

        # Validacija pre čuvanja (proveriće da li je end_date None za ACTIVE)
        validate_camera(camera)

        self.repository.update(camera)

    # 🧠 NORMALIZACIJA
    def _normalize(self, camera):
        camera.code = (camera.code or "").strip().upper()
        camera.ip_address = (camera.ip_address or "").strip()
        camera.location = (camera.location or "").strip()

        if camera.server:
            camera.server = camera.server.strip()

        if camera.camera_type:
            camera.camera_type = camera.camera_type.strip()

        if camera.purpose:
            camera.purpose = camera.purpose.strip()

        if camera.camera_function:
            camera.camera_function = camera.camera_function.strip()

        if camera.model:
            camera.model = camera.model.strip()

        if camera.note:
            camera.note = camera.note.strip()

    # 📥 BULK CREATE
    def create_many(self, cameras_data: list):
        inserted = 0
        skipped = 0

        for item in cameras_data:
            try:
                if isinstance(item, dict):
                    camera = self._dict_to_camera(item)
                else:
                    camera = item

                if self.repository.exists_by_code(camera.code):
                    skipped += 1
                    continue

                self._normalize(camera)

                try:
                    validate_camera(camera)
                except ValidationError:
                    skipped += 1
                    continue

                self.repository.add(camera)
                inserted += 1

            except Exception as e:
                log_warning(f"Bulk insert skip: {e}")
                skipped += 1

        return {
            "inserted": inserted,
            "skipped": skipped
        }

    # 🔧 DICT → MODEL
    def _dict_to_camera(self, data: dict):
        status_value = (data.get("health_status") or "inactive").lower()

        try:
            status = CameraStatus(status_value)
        except Exception:
            status = CameraStatus.INACTIVE

        return Camera(
            id=data.get("id"),
            code=data.get("code"),
            ip_address=data.get("ip_address"),
            rack=data.get("rack"),
            server=data.get("server"),
            location=data.get("location"),
            coverage=data.get("coverage"),
            camera_type=data.get("camera_type"),
            purpose=data.get("purpose"),
            camera_function=data.get("camera_function"),
            model=data.get("model"),
            retention_days=data.get("retention_days"),
            health_status=status,
            note=data.get("note"),
            action=data.get("action"),
            image_path=data.get("image_path"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
        )

    # 🔒 SECURITY (ORDER BY PROTECTION + NUMERIC SORT FIX)
    def _sanitize_order_by(self, order_by):
        allowed = {
            "id",
            "code",
            "ip_address",
            "location",
            "health_status"
        }

        if order_by not in allowed:
            return "id"

        return order_by

    def _sanitize_order_dir(self, order_dir):
        if str(order_dir).upper() not in ("ASC", "DESC"):
            return "ASC"

        return order_dir.upper()