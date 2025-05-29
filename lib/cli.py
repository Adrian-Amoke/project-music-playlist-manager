from lib.models.playlist import Playlist
from lib.models.song import Song
from lib.helpers import get_input, print_error

def run_cli():
    playlist_model = Playlist()
    song_model = Song()

    while True:
        print("\nWelcome To The Main Menu! Choose an option")
        print("1. Playlists")
        print("2. Songs")
        print("3. Exit")
        choice = get_input("Choose an option: ")

        if choice == "1":
            manage_playlists(playlist_model)
        elif choice == "2":
            manage_songs(song_model)
        elif choice == "3":
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
