from InquirerPy import prompt
from playlist import Playlist
from player import Player

playlist_manager = Playlist()
player = Player()

commands = {
    "playlist": "Select and play a playlist",
    "pause": "Pause playback",
    "next": "Play next track",
    "help": "Show this help message",
    "exit": "Exit the CLI"
}

def show_help():
    print("\nAvailable commands:")
    for command, description in commands.items():
        print(f"  {command:<8} - {description}")
    print("")

def select_playlist():
    playlists = playlist_manager.get_playlists()
    choices = [{"name": playlist['name'], "value": playlist['id']} for playlist in playlists]

    questions = [
        {
            "type": "list",
            "name": "playlist",
            "message": "Select a playlist",
            "choices": choices,
        }
    ]

    answer = prompt(questions)
    return answer['playlist']

def select_track_from_playlist():
    tracks = playlist_manager.get_track_list()
    choices = [{"name": track, "value": idx} for idx, track in enumerate(tracks)]

    questions = [
        {
            "type": "list",
            "name": "track",
            "message": "Select a track to play",
            "choices": choices,
        }
    ]

    answer = prompt(questions)
    track_choice = answer['track']
    return playlist_manager.get_track_info_by_index(track_choice)

def main():
    show_help()
    while True:
        command = input("Enter a command: ").strip().lower()

        if command == "exit":
            break
        elif command == "help":
            show_help()
        elif command == "playlist":
            playlist_id = select_playlist()
            playlist_manager.set_playlist(playlist_id)
            print("Auto-playing the playlist...")
            player.play_next(playlist_manager)  # 1曲目を再生
            while True:
                track_command = input("Enter 'next' to play the next track, 'select' to choose a track, or 'exit' to exit: ").strip().lower()
                if track_command == "next":
                    player.play_next(playlist_manager)
                elif track_command == "select":
                    track_info = select_track_from_playlist()
                    if track_info:
                        next_track_info = playlist_manager.get_next_track_info()
                        player.play_track(
                            track_info['uri'],
                            track_info['name'],
                            track_info['artist'],
                            next_track_info['name'] if next_track_info else None,
                            next_track_info['artist'] if next_track_info else None
                        )
                elif track_command == "exit":
                    break
                else:
                    print("Unknown command. Type 'next', 'select', or 'exit'.")
        elif command == "pause":
            try:
                player.pause_music()
                print("Playback paused")
            except Exception as e:
                print(e)
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()

