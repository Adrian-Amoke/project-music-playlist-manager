from lib.models.playlist import Playlist
from lib.models.song import Song
from lib.models.review import Review
from lib.helpers import get_input, print_error

def run_cli():
    playlist_model = Playlist()
    song_model = Song()
    review_model = Review()

    while True:
        print("\nWelcome To The Main Menu! Choose an option")
        print("1. Playlists")
        print("2. Songs")
        print("3. Reviews")
        print("4. Exit")
        choice = get_input("Choose an option: ")

        if choice == "1":
            manage_playlists(playlist_model)
        elif choice == "2":
            manage_songs(song_model)
        elif choice == "3":
            manage_reviews(review_model)
        elif choice == "4":
            print("Feel Free To Come Back!")
            break
        else:
            print_error("Invalid Choice! Choose a number in the choices given!")

def manage_playlists(model):
    while True:
        print("\nPlaylists")
        print("1. Create Playlist")
        print("2. View All Playlists")
        print("3. Update Playlist")
        print("4. Delete Playlist")
        print("5. Back")
        choice = get_input("Choose an option: ")

        if choice == "1":
            name = get_input("Playlist name: ")
            model.create(name)
            print("Playlist created.")
        elif choice == "2":
            playlists = model.get_all()
            for p in playlists:
                print(f"ID: {p[0]}, Name: {p[1]}")
        elif choice == "3":
            id_ = get_input("Playlist ID to update: ")
            new_name = get_input("New name: ")
            model.update(id_, new_name)
            print("Playlist updated.")
        elif choice == "4":
            id_ = get_input("Playlist ID to delete: ")
            model.delete(id_)
            print("Playlist deleted.")
        elif choice == "5":
            break
        else:
            print_error("Invalid Choice! Choose a number in the choices given!")

def manage_songs(model):
    while True:
        print("\nSongs")
        print("1. Create Song")
        print("2. View All Songs")
        print("3. Update Song")
        print("4. Delete Song")
        print("5. Back")
        choice = get_input("Choose an option: ")

        if choice == "1":
            title = get_input("Title: ")
            artist = get_input("Artist: ")
            playlist_id = get_input("Playlist ID: ")
            model.create(title, artist, playlist_id)
            print("Song created.")
        elif choice == "2":
            songs = model.get_all()
            for s in songs:
                print(f"ID: {s[0]}, Title: {s[1]}, Artist: {s[2]}, Playlist ID: {s[3]}")
        elif choice == "3":
            id_ = get_input("Song ID to update: ")
            new_title = get_input("New Title: ")
            new_artist = get_input("New Artist: ")
            model.update(id_, new_title, new_artist)
            print("Song updated.")
        elif choice == "4":
            id_ = get_input("Song ID to delete: ")
            model.delete(id_)
            print("Song deleted.")
        elif choice == "5":
            break
        else:
            print_error("Invalid Choice! Choose a number in the choices given!")

def manage_reviews(model):
    while True:
        print("\nReviews")
        print("1. Create Review")
        print("2. View All Reviews")
        print("3. Update Review")
        print("4. Delete Review")
        print("5. Back")
        choice = get_input("Choose an option: ")

        if choice == "1":
            review_text = get_input("Review text: ")
            rating = get_input("Rating (1-5): ")
            print("Review for:")
            print("1. Playlist")
            print("2. Song")
            review_type = get_input("Choose an option: ")
            playlist_id = None
            song_id = None
            if review_type == "1":
                playlist_id = get_input("Playlist ID: ")
            elif review_type == "2":
                song_id = get_input("Song ID: ")
            else:
                print_error("Invalid choice for review type.")
                continue
            model.create(review_text, int(rating), playlist_id, song_id)
            print("Review created.")
        elif choice == "2":
            reviews = model.get_all()
            for r in reviews:
                print(f"ID: {r[0]}, Review: {r[1]}, Rating: {r[2]}, Playlist ID: {r[3]}, Song ID: {r[4]}")
        elif choice == "3":
            id_ = get_input("Review ID to update: ")
            new_review_text = get_input("New review text: ")
            new_rating = get_input("New rating (1-5): ")
            model.update(id_, new_review_text, int(new_rating))
            print("Review updated.")
        elif choice == "4":
            id_ = get_input("Review ID to delete: ")
            model.delete(id_)
            print("Review deleted.")
        elif choice == "5":
            break
        else:
            print_error("Invalid Choice! Choose a number in the choices given!")
