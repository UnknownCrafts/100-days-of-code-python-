# Making a spotify playlist after webscraping billboard 100

import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

# user-input, webscraping
date = input("Which year do you want to travel to? Type the date in this format YYYY-MH-DD: ").strip()

URL = f"https://www.billboard.com/charts/hot-100/{date}"

date = date.split("-")
year = date[0]
month = date[1]
day = date[2]

response = requests.get(URL).text

soup = BeautifulSoup(response, "html.parser")

song_titles = [x.getText().replace("\n", "").replace("\t", "") for x in soup.select("li h3[id='title-of-a-story']")]

# spotify auth

auth_manager = SpotifyOAuth(scope="playlist-modify-private", 
                            client_secret=os.environ["CLIENT_SECRET"],
                            redirect_uri="http://localhost:4304/auth/spotify/callback", 
                            client_id=os.environ["CLIENT_ID"],  
                            show_dialog=True, 
                            cache_path="token.txt", 
                            username=os.environ["username"])

sp = spotipy.Spotify(auth_manager=auth_manager)

# Search for the songs on spotify

user_id = sp.current_user()["id"]
uris = []

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a playlist
playlist_name = f"{'-'.join(date)} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

# Adding songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=uris)