from bs4 import BeautifulSoup
import requests

#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_a_tags = soup.find_all(name="a")
#
# for tag in all_a_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

response = requests.get("https://news.ycombinator.com/")

yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")

article_texts = []
article_links = []

for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


# print(article_texts)
# print(article_links)
print(article_upvote)

index_of_max_value = article_upvote.index(max(article_upvote))
max_value_text = article_texts[index_of_max_value]
max_value_link = article_links[index_of_max_value]
print(max_value_text)
print(max_value_link)