# Emails inspirational quotes every Monday

import datetime
import smtplib
import random

quotes = []
email = ""
password = ""
smtp_service = ""


if datetime.datetime.now().strftime("%A") == "Monday":
    with open("quotes.txt") as file:
        quotes = file.readlines()
    
    chosen_quote = random.choice(quotes)
    
    with smtplib.SMTP(smtp_service) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email, 
            to_addrs=email, 
            msg=f"Subject: Monday Motivation\n\n{chosen_quote}"
        )
    