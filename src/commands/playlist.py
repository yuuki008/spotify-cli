from InquirerPy import prompt
from playlist import Playlist
from player import Player

def execute_playlist_command(player: Player, playlist_manager: Playlist):
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
    playlist_id = answer['playlist']
    playlist_manager.set_playlist(playlist_id)
    print("Auto-playing the playlist...")
    player.play_next(playlist_manager)  # 1曲目を再生
    while True:
        track_command = input("Enter 'next' to play the next track, 'select' to choose a track, or 'exit' to exit: ").strip().lower()
        if track_command == "next":
            player.play_next(playlist_manager)
        elif track_command == "select":
            tracks = playlist_manager.get_track_list()
            track_choices = [{"name": track, "value": idx} for idx, track in enumerate(tracks)]
            track_questions = [
                {
                    "type": "list",
                    "name": "track",
                    "message": "Select a track to play",
                    "choices": track_choices,
                }
            ]
            track_answer = prompt(track_questions)
            track_info = playlist_manager.get_track_info_by_index(track_answer['track'])
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

