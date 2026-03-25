import sqlite3
import os
from config import settings


class CameraDatabase:
    def __init__(self):
        # 📁 koristi globalni path iz settings
        db_path = settings.DB_PATH

        # 📁 napravi folder ako treba (ako ikad prebaciš DB u folder)
        db_dir = os.path.dirname(db_path)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)

        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

        # 🔥 kreiranje tabele
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