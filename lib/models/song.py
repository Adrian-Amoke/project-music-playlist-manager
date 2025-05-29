from lib.models import CONN, CURSOR

class Song:
    def __init__(self):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                artist TEXT NOT NULL,
                playlist_id INTEGER,
                FOREIGN KEY (playlist_id) REFERENCES playlists(id)
            )
        """)
        CONN.commit()

    def create(self, title, artist, playlist_id):
        CURSOR.execute("INSERT INTO songs (title, artist, playlist_id) VALUES (?, ?, ?)", (title, artist, playlist_id))
        CONN.commit()

    def get_all(self):
        CURSOR.execute("SELECT * FROM songs")
        return CURSOR.fetchall()

    def update(self, song_id, new_title, new_artist):
        CURSOR.execute("UPDATE songs SET title = ?, artist = ? WHERE id = ?", (new_title, new_artist, song_id))
        CONN.commit()

    def delete(self, song_id):
        CURSOR.execute("DELETE FROM songs WHERE id = ?", (song_id,))
        CONN.commit()
