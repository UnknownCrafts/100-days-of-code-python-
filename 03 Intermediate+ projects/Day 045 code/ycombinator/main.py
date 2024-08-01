# Learning webscraping using beautiful soup, in this case scraping ycombinator (this works as of july 2024, no guarantee that this will work in the future)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_tag = soup.find_all(name="span", class_="titleline")
article_text = [x.getText() for x in article_tag]
article_link = [x.find(name="a").get("href") for x in article_tag]
article_upvote = [int(x.getText().strip(" points")) for x in soup.find_all(name="span", class_="score")]

max_index = article_upvote.index(max(article_upvote))

print(article_text[max_index])
print(article_link[max_index])
print(article_upvote[max_index])