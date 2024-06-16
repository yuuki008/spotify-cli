from player import Player
from playlist import Playlist
from commands.playlist import execute_playlist_command
from commands.pause import execute_pause_command
from commands.next import execute_next_command
from commands.help import execute_help_command
from commands.search import execute_search_command
from commands.artists import execute_artists_command

playlist_manager = Playlist()
player = Player()

commands = {
    "playlist": "Select and play a playlist",
    "pause": "Pause playback",
    "next": "Play next track",
    "search": "Search for tracks, artists, albums, or playlists",
    "artists": "Select or search for an artist to play their top tracks",
    "help": "Show this help message",
    "exit": "Exit the CLI"
}

def main():
    execute_help_command(commands)
    while True:
        command = input("Enter a command: ").strip().lower()

        if command == "exit":
            break
        elif command == "help":
            execute_help_command(commands)
        elif command == "playlist":
            execute_playlist_command(player, playlist_manager)
        elif command == "pause":
            execute_pause_command(player)
        elif command == "next":
            execute_next_command(player, playlist_manager)
        elif command == "search":
            execute_search_command(player, playlist_manager)
        elif command == "artists":
            execute_artists_command(player)
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()

