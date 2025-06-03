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
        print("3. View Songs in Playlist")
        print("4. Update Playlist")
        print("5. Delete Playlist")
        print("6. Back")
        choice = get_input("Choose an option: ")

        if choice == "1":
            name = get_input("Playlist name: ")
            model.create(name)
            print("Playlist created.")
        elif choice == "2":
            playlists = model.get_all()
            print(f"{'ID':<5} {'Name':<40} {'Reviews':<60}")
            print("-" * 110)
            from lib.models.review import Review
            review_model = Review()
            for p in playlists:
                reviews = review_model.get_by_playlist(p[0])
                review_texts = ", ".join([r[1] for r in reviews]) if reviews else "No reviews"
                print(f"{p[0]:<5} {p[1]:<40} {review_texts:<60}")
        elif choice == "3":
            playlist_name = get_input("Enter Playlist name to view songs: ")
            from lib.models.playlist import Playlist
            playlist_model = Playlist()
            playlist_id = playlist_model.get_id_by_name(playlist_name)
            if playlist_id is None:
                print_error(f"Playlist '{playlist_name}' not found.")
                continue
            from lib.models.song import Song
            song_model = Song()
            songs = song_model.get_by_playlist(playlist_id)
            if songs:
                print(f"Songs in Playlist '{playlist_name}':")
                print(f"{'ID':<5} {'Title':<40} {'Artist':<30}")
                print("-" * 75)
                for s in songs:
                    print(f"{s[0]:<5} {s[1]:<40} {s[2]:<30}")
            else:
                print("No songs found in this playlist.")
        elif choice == "4":
            id_ = get_input("Playlist ID to update: ")
            new_name = get_input("New name: ")
            model.update(id_, new_name)
            print("Playlist updated.")
        elif choice == "5":
            id_ = get_input("Playlist ID to delete: ")
            model.delete(id_)
            print("Playlist deleted.")
        elif choice == "6":
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
            playlist_name = get_input("Playlist name: ")
            from lib.models.playlist import Playlist
            playlist_model = Playlist()
            playlist_id = playlist_model.get_id_by_name(playlist_name)
            if playlist_id is None:
                print_error(f"Playlist '{playlist_name}' not found.")
                continue
            model.create(title, artist, playlist_id)
            print("Song created.")
        elif choice == "2":
            songs = model.get_all()
            from lib.models.playlist import Playlist
            from lib.models.review import Review
            playlist_model = Playlist()
            review_model = Review()
            print(f"{'ID':<5} {'Title':<40} {'Artist':<30} {'Playlist':<40} {'Reviews':<60}")
            print("-" * 220)
            for s in songs:
                playlist_name = playlist_model.get_name_by_id(s[3]) if s[3] else "No Playlist"
                reviews = review_model.get_by_song(s[0])
                review_texts = ", ".join([r[1] for r in reviews]) if reviews else "No reviews"
                print(f"{s[0]:<5} {s[1]:<40} {s[2]:<30} {playlist_name:<40} {review_texts:<60}")
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
                playlist_name = get_input("Playlist name: ")
                from lib.models.playlist import Playlist
                playlist_model = Playlist()
                playlist_id = playlist_model.get_id_by_name(playlist_name)
                if playlist_id is None:
                    print_error(f"Playlist '{playlist_name}' not found.")
                    continue
            elif review_type == "2":
                song_id = get_input("Song ID: ")
            else:
                print_error("Invalid choice for review type.")
                continue
            model.create(review_text, int(rating), playlist_id, song_id)
            print("Review created.")
        elif choice == "2":
            reviews = model.get_all()
            print(f"{'ID':<5} {'Review':<70} {'Rating/5':<7} {'Playlist ID':<12} {'Song ID':<8}")
            print("-" * 110)
            for r in reviews:
                print(f"{r[0]:<5} {r[1]:<70} {r[2]:<7} {str(r[3]):<12} {str(r[4]):<8}")
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

