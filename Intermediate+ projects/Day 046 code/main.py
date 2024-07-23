import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

# user-input, webscraping
user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MH-DD: ").strip()

URL = f"https://www.billboard.com/charts/hot-100/{user_input}"

response = requests.get(URL).text

soup = BeautifulSoup(response, "html.parser")

song_titles = [x.getText().replace("\n", "").replace("\t", "") for x in soup.select("li h3[id='title-of-a-story']")]

# spotify auth

auth_manager = SpotifyClientCredentials(client_secret=os.environ["CLIENT_SECRET"], client_id=os.environ["CLIENT_ID"])
sp = spotipy.Spotify(auth_manager=auth_manager)

print(song_titles)