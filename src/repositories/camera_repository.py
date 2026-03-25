from models.camera import Camera, CameraStatus


class CameraRepository:
    def __init__(self, db):
        self.conn = db.get_connection()

    # ✅ CREATE (🔥 vraća ID)
    def add(self, camera: Camera):
        query = """
        INSERT INTO cameras (
            code, ip_address, rack_location, server,
            location, coverage, camera_type, purpose,
            function, model, retention_days, health_status,
            note, action, image_path, start_date, end_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor = self.conn.cursor()
        cursor.execute(query, (
            camera.code,
            camera.ip_address,
            camera.rack,
            camera.server,
            camera.location,
            camera.coverage,
            camera.camera_type,
            camera.purpose,
            camera.camera_function,
            camera.model,
            camera.retention_days,
            camera.health_status.value,
            camera.note,
            camera.action,
            camera.image_path,
            camera.start_date,
            camera.end_date
        ))
        self.conn.commit()

        return cursor.lastrowid  # 🔥 BITNO

    # 🔧 ORDER BY helper (🔥 FIX za numeric ID)
    def _build_order_clause(self, order_by, order_dir):
        allowed_columns = ["id", "code", "ip_address", "location", "health_status"]

        if order_by not in allowed_columns:
            order_by = "id"

        if order_dir not in ["ASC", "DESC"]:
            order_dir = "ASC"

        # 🔥 KLJUČNO: ID kao broj
        if order_by == "id":
            return f"ORDER BY CAST(id AS INTEGER) {order_dir}"

        return f"ORDER BY {order_by} {order_dir}"

    # ✅ LIST VIEW (SA SORTIRANJEM)
    def get_all_for_table(self, order_by="id", order_dir="ASC"):
        order_clause = self._build_order_clause(order_by, order_dir)

        query = f"""
        SELECT id, code, ip_address, location, health_status
        FROM cameras
        {order_clause}
        """

        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        return [self._map_to_table(row) for row in rows]

    # ✅ DETAIL VIEW
    def get_by_id(self, camera_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM cameras WHERE id = ?", (camera_id,))
        row = cursor.fetchone()

        return self._map_to_camera(row) if row else None

    # ✅ DELETE
    def delete(self, camera_id):
        self.conn.execute("DELETE FROM cameras WHERE id = ?", (camera_id,))
        self.conn.commit()

    # ✅ UPDATE
    def update(self, camera: Camera):
        query = """
        UPDATE cameras SET
            code=?, ip_address=?, rack_location=?, server=?,
            location=?, coverage=?, camera_type=?, purpose=?,
            function=?, model=?, retention_days=?, health_status=?,
            note=?, action=?, image_path=?, start_date=?, end_date=?
        WHERE id=?
        """

        self.conn.execute(query, (
            camera.code,
            camera.ip_address,
            camera.rack,
            camera.server,
            camera.location,
            camera.coverage,
            camera.camera_type,
            camera.purpose,
            camera.camera_function,
            camera.model,
            camera.retention_days,
            camera.health_status.value,
            camera.note,
            camera.action,
            camera.image_path,
            camera.start_date,
            camera.end_date,
            camera.id
        ))
        self.conn.commit()

    # ✅ SEARCH (TERM + STATUS + SORT)
    def search(self, term=None, status=None, order_by="id", order_dir="ASC"):
        order_clause = self._build_order_clause(order_by, order_dir)

        query = """
        SELECT id, code, ip_address, location, health_status
        FROM cameras
        WHERE 1=1
        """

        params = []

        # 🔍 TEXT SEARCH
        if term:
            query += """
            AND (
                code LIKE ? OR
                location LIKE ? OR
                ip_address LIKE ?
            )
            """
            like_term = f"%{term}%"
            params.extend([like_term, like_term, like_term])

        # 🎯 STATUS SEARCH
        if status:
            query += " AND health_status = ?"
            params.append(status)

        # 🔽 SORT
        query += f" {order_clause}"

        cursor = self.conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()

        return [self._map_to_table(row) for row in rows]

    # 🔹 TABLE MAPPER
    def _map_to_table(self, row):
        return {
            "id": row["id"],
            "code": row["code"],
            "ip_address": row["ip_address"],
            "location": row["location"],
            "status": CameraStatus(row["health_status"]).value
        }

    # 🔹 FULL MAPPER
    def _map_to_camera(self, row):
        return Camera(
            id=row["id"],
            code=row["code"],
            ip_address=row["ip_address"],
            rack=row["rack_location"],
            server=row["server"],
            location=row["location"],
            coverage=row["coverage"],
            camera_type=row["camera_type"],
            purpose=row["purpose"],
            camera_function=row["function"],
            model=row["model"],
            retention_days=row["retention_days"],
            health_status=CameraStatus(row["health_status"]),
            note=row["note"],
            action=row["action"],
            image_path=row["image_path"],
            start_date=row["start_date"],
            end_date=row["end_date"]
        )

    # ✅ EXISTS
    def exists_by_code(self, code):
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM cameras WHERE code = ?", (code,))
        return cursor.fetchone() is not None