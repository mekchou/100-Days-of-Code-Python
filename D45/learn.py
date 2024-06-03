from bs4 import BeautifulSoup
import requests
# import lmxl

# with open ("./D45/website.html") as file:
    # contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.li)
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# print(type(all_anchor_tags))

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    
    
    
# heading = soup.find(name="h1", id="name")
# print(heading.getText())

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# section_headings = soup.find_all(name="h3", class_="heading")
# print(section_headings)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# headings = soup.select(".heading")
# print(headings)


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")


# for titleline in titlelines:
titlelines = soup.find_all(name="span", class_="titleline")
article_points = soup.find_all(name="span", class_="score")
# print(len(titlelines))
# print(titlelines[0].find(name="a"))
article_texts = []
article_links = []
# for n in range(len(titlelines)):
for titleline in titlelines:
    article_tag = titleline.find(name="a", id=None)
    article_link = article_tag.get("href")
    article_text = article_tag.get_text()
    article_texts.append(article_text)
    article_links.append(article_link)
    # print(article_link)
    # print(article_text)
    # point = article_points[n].get_text()
    # print(point)

article_points = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_points)
# for article_point in article_points:
    # point = article_point.get_text()
    # print(point)
max_score = max(article_points)
max_index = article_points.index(max_score)
print(article_texts[max_index])
print(article_links[max_index])
print(article_points[max_index])