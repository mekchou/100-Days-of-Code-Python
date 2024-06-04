import scraping






def main():
    selected_date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD\n")
    
    # print(selected_date)
    song_list = scraping.SongScraping(selected_date)
    song_list.top_songs()
    print(song_list.song_titles)


if __name__ == "__main__":
    main()