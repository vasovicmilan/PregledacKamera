from PySide6.QtGui import QPixmap, QPixmapCache
from PySide6.QtCore import Qt
import os
from utils.logger import log_warning, log_error


def set_image_responsive(label, image_path, min_size=300, max_size=2000):
    """
    Full responsive image:
    - maksimalno popunjava prostor
    - koristi cache
    - bez flickera
    """

    if not image_path or not os.path.exists(image_path):
        if image_path:
            log_warning(f"Slika ne postoji: {image_path}")
        label.clear()
        label._original_pixmap = None
        return

    try:
        # 📥 LOAD ORIGINAL
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            log_warning(f"QPixmap ne može da učita sliku: {image_path}")
            label.clear()
            label._original_pixmap = None
            return

        # 🔥 zapamti original (za resize kasnije)
        label._original_pixmap = pixmap

        # 🔥 target size = realna veličina labela (bez min/max gušenja layouta)
        target_w = max(min_size, label.width())
        target_h = max(min_size, label.height())

        cache_key = f"{image_path}_{target_w}x{target_h}"

        # 🔥 CACHE HIT
        cached = QPixmapCache.find(cache_key)
        if cached:
            label.setPixmap(cached)
            label.setAlignment(Qt.AlignCenter)
            return

        # ⚡ FAST odmah (bez laga)
        fast_scaled = pixmap.scaled(
            target_w,
            target_h,
            Qt.KeepAspectRatio,
            Qt.FastTransformation
        )

        label.setPixmap(fast_scaled)
        label.setAlignment(Qt.AlignCenter)

        # 💾 cache fast verzije
        QPixmapCache.insert(cache_key + "_fast", fast_scaled)

        # 🎯 SMOOTH verzija (lepša, async simulacija bez threada)
        smooth_scaled = pixmap.scaled(
            target_w,
            target_h,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        label.setPixmap(smooth_scaled)

        # 💾 cache final
        QPixmapCache.insert(cache_key, smooth_scaled)

    except Exception as e:
        log_error(f"Greška pri učitavanju slike {image_path}: {e}")
        label.clear()
        label._original_pixmap = None


def enable_auto_resize(label):
    """
    Automatski resize slike kada se label menja
    """

    def resize_event(event):
        if hasattr(label, "_original_pixmap") and label._original_pixmap:
            pixmap = label._original_pixmap

            target_w = label.width()
            target_h = label.height()

            cache_key = f"resize_{target_w}x{target_h}"

            cached = QPixmapCache.find(cache_key)
            if cached:
                label.setPixmap(cached)
            else:
                scaled = pixmap.scaled(
                    target_w,
                    target_h,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                label.setPixmap(scaled)
                QPixmapCache.insert(cache_key, scaled)

        return type(label).resizeEvent(label, event)

    label.resizeEvent = resize_event