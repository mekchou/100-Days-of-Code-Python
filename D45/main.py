import requests
from bs4 import BeautifulSoup
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
best_movies_page = response.text

soup = BeautifulSoup(best_movies_page, "html.parser")

movie_sections = soup.find_all(name= "h3", class_="title")

pattern = r"\)\s|\:\s"

movie_list = [re.split(pattern,movie_section.get_text())[1] for movie_section in movie_sections]
# use reverse

movie_list.reverse()
with open ("./D45/movies.txt", "w") as file:
    for index, movie in enumerate(movie_list):
        file.write(f"{index + 1}) {movie}\n")


# use pop
# with open ("./D45/movies.txt", "w") as file:
    # for n in range(len(movie_list)):
        # file.write(f"{n + 1}) {movie_list.pop()}\n")
        
        