from auth import get_spotify_client

class Playlist:
    def __init__(self):
        self.sp = get_spotify_client()
        self.current_playlist = None
        self.current_track_index = 0

    def get_playlists(self):
        playlists = self.sp.current_user_playlists()
        return playlists['items']

    def get_playlist_tracks(self, playlist_id):
        tracks = self.sp.playlist_tracks(playlist_id)
        return tracks['items']

    def set_playlist(self, playlist_id):
        self.current_playlist = self.get_playlist_tracks(playlist_id)
        self.current_track_index = 0

    def get_next_track(self):
        if self.current_playlist and self.current_track_index < len(self.current_playlist):
            track_info = self.current_playlist[self.current_track_index]['track']
            self.current_track_index += 1
            return {
                "uri": track_info['uri'],
                "name": track_info['name'],
                "artist": track_info['artists'][0]['name']
            }
        return None

    def get_next_track_info(self):
        if self.current_playlist and self.current_track_index < len(self.current_playlist):
            track_info = self.current_playlist[self.current_track_index]['track']
            return {
                "name": track_info['name'],
                "artist": track_info['artists'][0]['name']
            }
        return None

    def get_track_list(self):
        if not self.current_playlist:
            return []
        return [f"{track['track']['name']} by {track['track']['artists'][0]['name']}" for track in self.current_playlist]

    def get_track_info_by_index(self, index):
        if self.current_playlist and 0 <= index < len(self.current_playlist):
            track_info = self.current_playlist[index]['track']
            return {
                "uri": track_info['uri'],
                "name": track_info['name'],
                "artist": track_info['artists'][0]['name']
            }
        return None

