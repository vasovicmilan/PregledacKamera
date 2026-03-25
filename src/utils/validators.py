import re
from models.camera import CameraStatus

class ValidationError(Exception):
    pass

def validate_camera(camera):
    errors = []

    # 🔴 REQUIRED
    if not camera.code or camera.code.strip() == "":
        errors.append("Kod kamere je obavezan.")

    if not camera.ip_address or camera.ip_address.strip() == "":
        errors.append("IP adresa je obavezna.")
    elif not _is_valid_ip(camera.ip_address):
        errors.append("IP adresa nije validna.")

    if not camera.location or camera.location.strip() == "":
        errors.append("Lokacija je obavezna.")

    if not isinstance(camera.health_status, CameraStatus):
        errors.append("Status kamere nije validan.")

    # 🔴 LOGIKA ZA END_DATE U ODNOSU NA STATUS
    if camera.health_status == CameraStatus.ACTIVE:
        if camera.end_date is not None:
            errors.append("Za aktivnu kameru ne može biti definisan krajnji datum.")
    else:
        # Za neaktivnu ili skinutu kameru, end_date je opcion, ali ako postoji mora biti nakon start_date
        if camera.end_date is not None:
            if camera.start_date and camera.start_date > camera.end_date:
                errors.append("End date ne može biti pre start date.")

    # 🔴 OPTIONAL (ako postoji → validiraj)
    if camera.retention_days is not None:
        if not isinstance(camera.retention_days, int) or camera.retention_days < 0:
            errors.append("Retencija mora biti pozitivan broj.")

    # 🔴 FINAL CHECK
    if errors:
        raise ValidationError("\n".join(errors))


# 🔧 HELPERI
def _is_valid_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if not re.match(pattern, ip):
        return False

    parts = ip.split(".")
    return all(0 <= int(part) <= 255 for part in parts)