from auth import get_spotify_client, refresh_token
from utils import handle_no_active_device
import spotipy

class Player:
    def __init__(self):
        self.sp = get_spotify_client()

    def get_active_device(self):
        devices = self.sp.devices()
        active_device = None
        for device in devices['devices']:
            if device['is_active']:
                active_device = device
                break
        return active_device

    def is_playing(self):
        playback = self.sp.current_playback()
        return playback and playback['is_playing']

    def play_track(self, track_uri, track_name, artist_name, next_track_name=None, next_artist_name=None):
        active_device = self.get_active_device()
        if not active_device:
            handle_no_active_device()

        if self.is_playing():
            try:
                self.sp.pause_playback(device_id=active_device['id'])
            except spotipy.exceptions.SpotifyException as e:
                if e.http_status == 403:
                    self.sp.auth_manager.get_access_token(as_dict=False)
                    self.sp.pause_playback(device_id=active_device['id'])

        try:
            self.sp.start_playback(device_id=active_device['id'], uris=[track_uri])
        except spotipy.exceptions.SpotifyException as e:
            if e.http_status == 403:
                self.sp.auth_manager.get_access_token(as_dict=False)
                self.sp.start_playback(device_id=active_device['id'], uris=[track_uri])

        print(f"Playing: {track_name} by {artist_name}")
        if next_track_name and next_artist_name:
            print(f"Next: {next_track_name} by {next_artist_name}")

    def pause_music(self):
        active_device = self.get_active_device()
        if not active_device:
            handle_no_active_device()

        if self.is_playing():
            try:
                self.sp.pause_playback(device_id=active_device['id'])
            except spotipy.exceptions.SpotifyException as e:
                if e.http_status == 403:
                    self.sp.auth_manager.get_access_token(as_dict=False)
                    self.sp.pause_playback(device_id=active_device['id'])
        else:
            print("No track is currently playing.")

    def play_next(self, playlist):
        next_track = playlist.get_next_track()
        if next_track:
            next_next_track = playlist.get_next_track_info()
            self.play_track(
                next_track['uri'],
                next_track['name'],
                next_track['artist'],
                next_next_track['name'] if next_next_track else None,
                next_next_track['artist'] if next_next_track else None
            )
        else:
            print("End of playlist reached.")

    def get_artist_top_tracks(self, artist_id):
        results = self.sp.artist_top_tracks(artist_id)
        return results['tracks']

    def get_album_tracks(self, album_id):
        results = self.sp.album_tracks(album_id)
        return results['items']

    def get_artist_albums(self, artist_id):
        results = self.sp.artist_albums(artist_id, album_type='album')
        return results['items']

    def play_tracks(self, track_uris):
        active_device = self.get_active_device()
        if not active_device:
            handle_no_active_device()

        try:
            self.sp.start_playback(device_id=active_device['id'], uris=track_uris)
        except spotipy.exceptions.SpotifyException as e:
            if e.http_status == 403:
                self.sp.auth_manager.get_access_token(as_dict=False)
                self.sp.start_playback(device_id=active_device['id'], uris=track_uris)

    def get_favorite_artists(self):
        results = self.sp.current_user_top_artists()
        return results['items']

