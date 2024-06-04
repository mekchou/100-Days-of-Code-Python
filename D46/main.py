import scraping
import spotify

# for idx, item in enumerate(results['items']):
    # track = item['track']
    # print(idx, track['artists'][0]['name'], " – ", track['name'])
# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)






def main():
    selected_date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD\n")
    year = selected_date.split("-")[0]
    # print(selected_date)
    song_list = scraping.SongScraping(selected_date)
    song_list.top_songs()
    # print(song_list.song_titles)

    sp = spotify.SpotifyAPI()
    sp.create_playlist(selected_date)
    for song in song_list.song_titles:
        sp.search(song, year)
    # print(sp.song_uri)
    # print(sp.playlist_id)
    sp.add_tracks()
    # print(sp.song_uri)

if __name__ == "__main__":
    main()
    # pass