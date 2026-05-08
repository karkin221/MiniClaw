import sqlite3
import json
import time
from pathlib import Path


class EventStore:

    DB = "events.db"

    @classmethod
    def init(cls):

        conn = sqlite3.connect(cls.DB)

        cursor = conn.cursor()

        # drop incompatible old schema
        cursor.execute(
            "DROP TABLE IF EXISTS events"
        )

        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS events (
                session_id TEXT,
                timestamp REAL,
                type TEXT,
                data TEXT
            )
            '''
        )

        conn.commit()

        conn.close()

    @classmethod
    def emit(cls, session_id, event_type, data):

        conn = sqlite3.connect(cls.DB)

        conn.execute(
            'INSERT INTO events VALUES (?, ?, ?, ?)',
            (
                session_id,
                time.time(),
                event_type,
                json.dumps(data)
            )
        )

        conn.commit()

        conn.close()

    @classmethod
    def replay(cls, session_id):

        conn = sqlite3.connect(cls.DB)

        rows = conn.execute(
            'SELECT * FROM events WHERE session_id=?',
            (session_id,)
        ).fetchall()

        conn.close()

        return rows