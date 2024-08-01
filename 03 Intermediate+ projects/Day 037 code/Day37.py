# Habit tracker by using pixela

import requests
from datetime import datetime

USERNAME = "" # choose a username
TOKEN = "" # generate your own token here
graph_id = "graph1" # you could choose a different id


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Code below is used to create a new user on the pixela site
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()

# Graph creation code
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": graph_id,
    "name": "Coding Time", # you could choose a different name
    "unit": "ns", # you could choose a different unit 
    "type": "int", # you could choose a different type
    "color": "ajisai", # you could choose a different color from the documentation
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Use the lines below to make a new graph in pixela
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response.raise_for_status()

# Updating a pixel on the graph
date = datetime.now().strftime("%Y%m%d")
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

pixel_params = {
    "date": date,
    "quantity": "1",
}

# Use the code below to update a new pixel
# response = requests.post(url=pixel_update_endpoint, json=pixel_params, headers=headers)
# response.raise_for_status()

# Updating a previous pixel
pixel_previous_update_endpoint = f"{pixel_update_endpoint}/{date}" # change the date variable as necessary

update_previous_params = {
    "quantity": "11",
}

# Use the code below to update an old pixel
# response = requests.put(url=pixel_previous_update_endpoint, json=update_previous_params, headers=headers)
# response.raise_for_status()

# The code below will delete data from a pixel depending on the inputted date
# response = requests.delete(url=pixel_previous_update_endpoint, headers=headers)
# response.raise_for_status()