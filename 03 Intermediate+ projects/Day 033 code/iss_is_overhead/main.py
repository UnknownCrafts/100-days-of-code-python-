#Checks for the position of the ISS and emails you if its right above you.


import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
email = "" # put your email here
password = "" # put the password for the email here
smtp_service = "" # generated smtp token from email service

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5):
        return True
    return False
        

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if (time_now > sunset):
        return True
    return False


while True:
    
    if (is_night() and is_iss_overhead()):
        with smtplib.SMTP(smtp_service) as connection:
                connection.starttls()
                connection.login(email, password)
                connection.sendmail(
                    from_addr=email, 
                    to_addrs=email, 
                    msg=f"Subject: iss position\n\nLook Up!"
                )
    time.sleep(60) #makes it so the code runs the check every minute


