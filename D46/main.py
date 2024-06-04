import scraping
import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="45c3f03776cd4347adf0d2cffec9e0bf", 
        client_secret="8b107bde5c5e413f9e16419dd8dca8d8",
        scope=scope,
        redirect_uri="http://127.0.0.1:8080",
        show_dialog=True,
        cache_path = "./D46/token.txt",
        username="mekchou"
        )
    )
# print()
results = sp.current_user()["id"]

# for idx, item in enumerate(results['items']):
    # track = item['track']
    # print(idx, track['artists'][0]['name'], " – ", track['name'])
# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)






def main():
    selected_date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD\n")
    
    # print(selected_date)
    song_list = scraping.SongScraping(selected_date)
    song_list.top_songs()
    print(song_list.song_titles)


if __name__ == "__main__":
    # main()
    pass