from auth import get_spotify_client
from utils import handle_no_active_device

def get_active_device():
    sp = get_spotify_client()
    devices = sp.devices()
    active_device = None
    for device in devices['devices']:
        if device['is_active']:
            active_device = device
            break
    return active_device

def get_playlists():
    sp = get_spotify_client()
    playlists = sp.current_user_playlists()
    return playlists['items']

def get_playlist_tracks(playlist_id):
    sp = get_spotify_client()
    tracks = sp.playlist_tracks(playlist_id)
    return tracks['items']

def play_track(track_uri):
    sp = get_spotify_client()
    active_device = get_active_device()
    if not active_device:
        handle_no_active_device()
    sp.start_playback(device_id=active_device['id'], uris=[track_uri])

def pause_music():
    sp = get_spotify_client()
    active_device = get_active_device()
    if not active_device:
        handle_no_active_device()
    sp.pause_playback(device_id=active_device['id'])

