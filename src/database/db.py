import sqlite3
import os
import shutil
from config import settings


class CameraDatabase:
    def __init__(self):
        db_path = settings.DB_PATH
        db_dir = os.path.dirname(db_path)

        # 📁 Napravi folder ako ne postoji
        os.makedirs(db_dir, exist_ok=True)

        # 🔥 Ako baza ne postoji u korisničkom folderu, pokušaj da je kopiraš iz paketa
        if not os.path.exists(db_path):
            bundled_db = settings.resource_path("database/cameras.db")
            if os.path.exists(bundled_db):
                shutil.copy2(bundled_db, db_path)
            # Ako nema početne baze u paketu, nastaviće se sa kreiranjem prazne baze

        # 📁 Poveži se na bazu
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

        # 🔥 Kreiraj tabelu ako ne postoji (sigurnosno, u slučaju da je baza prazna)
        self.create_table()

    def get_connection(self):
        return self.conn

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS cameras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE,
            ip_address TEXT,
            rack_location TEXT,
            server TEXT,
            location TEXT,
            coverage TEXT,
            camera_type TEXT,
            purpose TEXT,
            function TEXT,
            model TEXT,
            retention_days INTEGER,
            health_status TEXT,
            note TEXT,
            action TEXT,
            image_path TEXT,
            start_date TEXT,
            end_date TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()
