import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIEND_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIEND_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
scope = "playlist-modify-private"


class SpotifyAPI():
    def __init__(self) -> None:
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            scope=scope,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            show_dialog=True,
            cache_path = "./D46/token.txt",
            username="mekchou"
            )
        )
        self.user_id = self.sp.current_user()["id"]
        self.song_uri = []

    def search(self, song, year):
        try:
            uri = self.sp.search(q=f"track: {song} year: {year}", type="track")["tracks"]["items"][0]["uri"]
            self.song_uri.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
        # return song_uri
        