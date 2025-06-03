from lib.models import CONN, CURSOR

class Review:
    def __init__(self):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                review_text TEXT NOT NULL,
                rating INTEGER NOT NULL,
                playlist_id INTEGER,
                song_id INTEGER,
                FOREIGN KEY (playlist_id) REFERENCES playlists(id),
                FOREIGN KEY (song_id) REFERENCES songs(id)
            )
        """)
        CONN.commit()

    def create(self, review_text, rating, playlist_id=None, song_id=None):
        CURSOR.execute("""
            INSERT INTO reviews (review_text, rating, playlist_id, song_id)
            VALUES (?, ?, ?, ?)
        """, (review_text, rating, playlist_id, song_id))
        CONN.commit()

    def get_all(self):
        CURSOR.execute("SELECT * FROM reviews")
        return CURSOR.fetchall()

    def update(self, review_id, new_review_text, new_rating):
        CURSOR.execute("""
            UPDATE reviews
            SET review_text = ?, rating = ?
            WHERE id = ?
        """, (new_review_text, new_rating, review_id))
        CONN.commit()

    def delete(self, review_id):
        CURSOR.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
        CONN.commit()

    def get_by_playlist(self, playlist_id):
        CURSOR.execute("SELECT * FROM reviews WHERE playlist_id = ?", (playlist_id,))
        return CURSOR.fetchall()

    def get_by_song(self, song_id):
        CURSOR.execute("SELECT * FROM reviews WHERE song_id = ?", (song_id,))
        return CURSOR.fetchall()
