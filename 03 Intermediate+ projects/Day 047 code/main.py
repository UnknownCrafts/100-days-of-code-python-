# A web scraper that is able to send an email to you informing you if the price of a product has dropped under the threshold.

import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

URL = "Amazon-Product-Link" # Product to check the price of
THRESHHOLD_PRICE = 100 # Price of the product should be under this amount.

# At minimum add the User-Agent and Accept-Language. At most copy the full header from https://httpbin.org/headers (excluding the host and X-Amzn-Trace-id)
headers=""

response = requests.get(URL,headers=headers).text

soup = BeautifulSoup(response, "html.parser")

product_title = soup.find(name="span", id="productTitle").getText()
price_main = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()

price = float(f"{price_main}{price_fraction}")

if price < THRESHHOLD_PRICE:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"]) as connection:
                connection.starttls()
                connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
                connection.sendmail(
                    from_addr=os.environ["EMAIL_ADDRESS"], 
                    to_addrs=os.environ["EMAIL_ADDRESS"], 
                    msg=f"Subject: Amazon Price Alert!\n\n{product_title} is now ${price}\n{URL}"
            )