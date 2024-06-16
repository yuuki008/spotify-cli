from InquirerPy import prompt
from player import get_playlists, get_playlist_tracks, play_track, pause_music

def select_playlist():
    playlists = get_playlists()
    choices = [{"name": playlist['name'], "value": playlist['id']} for playlist in playlists]

    questions = [
        {
            "type": "list",
            "message": "Select a playlist",
            "choices": choices,
        }
    ]

    answer = prompt(questions)
    return answer[0]

def select_track(playlist_id):
    tracks = get_playlist_tracks(playlist_id)
    choices = [{"name": f"{track['track']['name']} by {track['track']['artists'][0]['name']}", "value": track['track']['uri']} for track in tracks]

    questions = [
        {
            "type": "list",
            "message": "Select a track",
            "choices": choices,
        }
    ]

    answer = prompt(questions)
    return answer[0]

def main():
    while True:
        choices = [
            {"name": "Play a playlist", "value": "play"},
            {"name": "Pause playback", "value": "pause"},
            {"name": "Exit", "value": "exit"},
        ]

        questions = [
            {
                "type": "list",
                "message": "Enter a command",
                "choices": choices,
            }
        ]

        command = prompt(questions)[0]

        if command == "exit":
            break
        elif command == "play":
            playlist_id = select_playlist()
            track_uri = select_track(playlist_id)
            play_track(track_uri)
            print("Playback started")
        elif command == "pause":
            pause_music()
            print("Playback paused")

if __name__ == "__main__":
    main()

