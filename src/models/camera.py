from enum import Enum

class CameraStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DISMANTLED = "dismantled"

class Camera:
    def __init__(
        self,
        code,
        ip_address,
        rack,
        server,
        location,
        coverage,
        camera_type,
        purpose,
        camera_function,
        model,
        retention_days,
        health_status: CameraStatus,
        note,
        action,
        image_path,
        start_date=None,
        end_date=None,
        id=None
    ):
        self.id = id
        self.code = code
        self.ip_address = ip_address
        self.rack = rack
        self.server = server
        self.location = location
        self.coverage = coverage
        self.camera_type = camera_type
        self.purpose = purpose
        self.camera_function = camera_function
        self.model = model
        self.retention_days = retention_days
        self.health_status = health_status
        self.note = note
        self.action = action
        self.image_path = image_path
        self.start_date = start_date
        self.end_date = end_date