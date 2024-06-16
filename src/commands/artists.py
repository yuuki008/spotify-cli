from InquirerPy import prompt, inquirer
from player import Player

def execute_artists_command(player: Player):
    choices = ["Select from favorite artists", "Search for an artist"]
    questions = [
        {
            "type": "list",
            "name": "choice",
            "message": "How would you like to find an artist?",
            "choices": choices,
        }
    ]

    choice_answer = prompt(questions)
    choice = choice_answer['choice']

    if choice == "Select from favorite artists":
        favorite_artists = player.get_favorite_artists()
        if not favorite_artists:
            print("No favorite artists found.")
            return

        artist_choices = [{"name": artist['name'], "value": artist['uri']} for artist in favorite_artists]
        artist_questions = [
            {
                "type": "list",
                "name": "artist",
                "message": "Select an artist",
                "choices": artist_choices,
            }
        ]
        artist_answer = prompt(artist_questions)
        selected_artist_uri = artist_answer['artist']
        artist_id = selected_artist_uri.split(':')[-1]
        play_artist_tracks_loop(player, artist_id)
    elif choice == "Search for an artist":
        search_query = input("Enter the name of the artist you want to search for: ").strip()
        search_results = player.sp.search(q=search_query, type='artist', limit=10)
        artists = search_results['artists']['items']
        artist_choices = [{"name": artist['name'], "value": artist['uri']} for artist in artists]

        artist_questions = [
            {
                "type": "list",
                "name": "artist",
                "message": "Select an artist from the search results",
                "choices": artist_choices,
            }
        ]

        artist_answer = prompt(artist_questions)
        selected_artist_uri = artist_answer['artist']
        artist_id = selected_artist_uri.split(':')[-1]
        play_artist_tracks_loop(player, artist_id)

def play_artist_tracks_loop(player, artist_id):
    top_tracks = player.get_artist_top_tracks(artist_id)
    albums = player.get_artist_albums(artist_id)
    all_tracks = top_tracks

    for album in albums:
        album_tracks = player.get_album_tracks(album['id'])
        all_tracks.extend(album_tracks)

    all_tracks = all_tracks[:100]  # Max 100 tracks

    current_track_uri = None

    while True:
        track_choices = []
        for track in all_tracks:
            album_name = track['album']['name'] if 'album' in track else 'Unknown Album'
            release_date = track['album']['release_date'] if 'album' in track else 'Unknown Date'
            display_name = f"{track['name']} by {track['artists'][0]['name']} - {album_name} ({release_date})"
            if track['uri'] == current_track_uri:
                display_name = f"> {display_name}"
            track_choices.append({"name": display_name, "value": track['uri']})

        track_choices.append({"name": "Exit", "value": "exit"})

        track_question = inquirer.select(
            message="Select a track to play (currently playing is bolded):",
            choices=track_choices,
            default=current_track_uri
        )

        selected_track_uri = track_question.execute()

        if selected_track_uri == "exit":
            break

        track_info = next(track for track in all_tracks if track['uri'] == selected_track_uri)
        player.play_track(selected_track_uri, track_info['name'], track_info['artists'][0]['name'])
        current_track_uri = selected_track_uri

        while player.is_playing():
            pass  # Wait until the current track finishes

        print(f"Finished playing: {track_info['name']} by {track_info['artists'][0]['name']}")

