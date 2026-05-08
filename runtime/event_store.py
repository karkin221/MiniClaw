import sqlite3
import json
import time

class EventStore:

    DB = "events.db"

    @classmethod
    def init(cls):

        conn = sqlite3.connect(cls.DB)

        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS events (
                timestamp REAL,
                type TEXT,
                data TEXT
            )
            '''
        )

        conn.commit()
        conn.close()

    @classmethod
    def emit(cls, event_type, data):

        conn = sqlite3.connect(cls.DB)

        conn.execute(
            'INSERT INTO events VALUES (?, ?, ?)',
            (
                time.time(),
                event_type,
                json.dumps(data)
            )
        )

        conn.commit()
        conn.close()

    @classmethod
    def replay(cls):

        conn = sqlite3.connect(cls.DB)

        rows = conn.execute(
            'SELECT * FROM events'
        ).fetchall()

        conn.close()

        return rows
