import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ.get("SPOTIPY_CLIEND_ID"), 
        client_secret=os.environ.get("SPOTIPY_CLIEND_SECRET"),
        scope=scope,
        redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
        show_dialog=True,
        cache_path = "./D46/token.txt",
        username="mekchou"
        )
    )
# print()
results = sp.current_user()["id"]
print(results)