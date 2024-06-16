from player import Player
from playlist import Playlist

def execute_next_command(player: Player, playlist_manager: Playlist):
    player.play_next(playlist_manager)

