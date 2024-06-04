from bs4 import BeautifulSoup
import requests

class SongScraping():
    def __init__(self, date):
        self.url = f"https://www.billboard.com/charts/hot-100/{date}/"
        self.song_titles = []
    
    def top_songs(self):
        response = requests.get(self.url)
        billboard_page = response.text
        soup = BeautifulSoup(billboard_page, "html.parser")
        # lists = soup.find_all(name = "li", class_ = "o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
        lists = soup.find_all(name = "ul", class_ = "lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")
        for list in lists:
            song = list.find(name = "h3", id = "title-of-a-story")
            title = song.get_text().strip()
            self.song_titles.append(title)