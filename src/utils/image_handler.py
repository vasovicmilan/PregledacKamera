import os
import uuid
from PIL import Image, ImageOps

import config.settings as settings
from utils.logger import log_error, log_info


IMAGES_FOLDER = settings.IMAGES_DIR
os.makedirs(IMAGES_FOLDER, exist_ok=True)


def process_image(image_path, camera_code):
    """
    Obrada slike:
    - auto rotate (EXIF)
    - resize (max 1400px)
    - JPG konverzija
    - kvalitetnija kompresija
    """

    if not image_path or not os.path.exists(image_path):
        log_info(f"Preskakanje obrade slike za kameru {camera_code}: putanja ne postoji ili je prazna")
        return None

    try:
        img = Image.open(image_path)

        # 🔄 ispravi rotaciju (telefon slike)
        img = ImageOps.exif_transpose(img)

        # 🎨 RGB fix
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # 🔽 resize (VEĆE nego pre)
        img.thumbnail((1400, 1400))

        # 🆕 ime
        unique_name = f"{camera_code}_{uuid.uuid4().hex}.jpg"
        new_path = os.path.join(IMAGES_FOLDER, unique_name)

        # 💾 save (bolji kvalitet)
        img.save(
            new_path,
            "JPEG",
            quality=92,
            optimize=True,
            subsampling=0  # 🔥 bolji kvalitet (manje gubitka)
        )

        log_info(f"Slika uspešno obrađena za kameru {camera_code}: {new_path}")
        return new_path

    except Exception as e:
        log_error(f"[IMAGE_PROCESS_ERROR] Greška pri obradi slike za kameru {camera_code}: {str(e)}")
        return None