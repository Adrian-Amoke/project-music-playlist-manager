from lib.models import CONN, CURSOR

class Playlist:
    def __init__(self):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS playlists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        CONN.commit()

    def create(self, name):
        CURSOR.execute("INSERT INTO playlists (name) VALUES (?)", (name,))
        CONN.commit()

    def get_all(self):
        CURSOR.execute("SELECT * FROM playlists")
        return CURSOR.fetchall()

    def update(self, playlist_id, new_name):
        CURSOR.execute("UPDATE playlists SET name = ? WHERE id = ?", (new_name, playlist_id))
        CONN.commit()

    def delete(self, playlist_id):
        CURSOR.execute("DELETE FROM playlists WHERE id = ?", (playlist_id,))
        CONN.commit()

    def get_name_by_id(self, playlist_id):
        CURSOR.execute("SELECT name FROM playlists WHERE id = ?", (playlist_id,))
        result = CURSOR.fetchone()
        return result[0] if result else None

    def get_id_by_name(self, playlist_name):
        CURSOR.execute("SELECT id FROM playlists WHERE name = ?", (playlist_name,))
        result = CURSOR.fetchone()
        return result[0] if result else None
