# Using open weather map to see if it will rain today, also uses twillio rest API to communicate via sms

import requests
from twilio.rest import Client

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "" # Your api key here
twilio_account_id = "" # Your twillio account id
twillio_auth_token = "" # Your twillio auth token
twillio_number = "+" # Your twillio number, numbers start with the country code, you could also use twillio whastapp number here
your_number = "+" # Your personal phone number, numbers start with the country code, you could also use your whastapp number here if twillio is sending via whatsapp


params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

request = requests.get(OWM_endpoint, params=params)
request.raise_for_status()

will_rain = False
for i in range(4):
    current_weather = request.json()["list"][i]["weather"][0]["id"]
    if int(current_weather) < 700:
        will_rain = True

if will_rain:
    client = Client(twilio_account_id, twillio_auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔",
            from=twillio_number,
            to=your_number
        )
    # Use the code below if you want to use whatsapp instead of sms and comment the code above
    # message = client.messages \
    #     .create(
    #         body="It's going to rain today. Remember to bring an ☔",
    #         from="whatsapp:"+twillio_number,
    #         to="whatsapp:"+your_number
    #     )
    print(message.status)