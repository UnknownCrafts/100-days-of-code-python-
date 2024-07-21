# More webscraping practice

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movie_titles = [f"{x.getText()}\n" for x in soup.find_all(name="h3", class_="title")][::-1]

with open("movies.txt", "w") as file:
    file.writelines(movie_titles)