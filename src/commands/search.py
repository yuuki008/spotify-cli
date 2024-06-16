from InquirerPy import prompt
from player import Player
from playlist import Playlist

def execute_search_command(player: Player, playlist_manager: Playlist):
    categories = ["track", "artist", "album", "playlist"]
    questions = [
        {
            "type": "list",
            "name": "category",
            "message": "What do you want to search for?",
            "choices": categories,
        }
    ]

    category_answer = prompt(questions)
    category = category_answer['category']

    search_query = input(f"Enter the name of the {category} you want to search for: ").strip()

    search_results = playlist_manager.sp.search(q=search_query, type=category, limit=10)
    items = search_results[category+'s']['items']

    choices = []
    for idx, item in enumerate(items):
        if category == 'track':
            name = f"{item['name']} by {item['artists'][0]['name']}"
        elif category == 'artist':
            name = item['name']
        elif category == 'album':
            name = f"{item['name']} by {item['artists'][0]['name']}"
        elif category == 'playlist':
            name = item['name']
        choices.append({"name": name, "value": item['uri']})

    result_questions = [
        {
            "type": "list",
            "name": "result",
            "message": f"Select a {category} from the results",
            "choices": choices,
        }
    ]

    result_answer = prompt(result_questions)
    selected_uri = result_answer['result']

    if category == 'track':
        player.play_track(selected_uri, items[0]['name'], items[0]['artists'][0]['name'])
    elif category == 'playlist':
        playlist_manager.set_playlist(selected_uri.split(':')[-1])
        player.play_next(playlist_manager)
    else:
        print(f"Selected {category} URI: {selected_uri}")

