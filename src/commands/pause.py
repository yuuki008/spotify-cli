from player import Player

def execute_pause_command(player: Player):
    try:
        player.pause_music()
        print("Playback paused")
    except Exception as e:
        print(e)

