# Zillow rental webscraper

import os
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

FORM = os.environ["GOOGLE_FORM"]
LINK = os.environ["WEB_LINK"]

# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Webscraping

response = requests.get(LINK).text
soup = BeautifulSoup(response, "html.parser")
listing_links = [x.get("href") for x in soup.find_all(name="a", class_="property-card-link")]
listing_prices = [x.getText()[:6].strip("+") if "," in x.getText()[:6].strip("+") else "{}{}{}".format(x.getText()[:6].strip("+")[:2], ",", x.getText()[:6].strip("+")[2:]) 
                  for x in soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
listing_addresses = [x.getText().strip("\n").strip() if "|" not in x.getText().strip("\n").strip() else x.getText().strip("\n").strip().split("|")[1].strip() 
                     for x in soup.find_all(name="address")]

# Fill out the form
google_form = driver.get(FORM)
for i in range(len(listing_addresses)):
    time.sleep(3)
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')


    address_input.send_keys(listing_addresses[i])
    price_input.send_keys(listing_prices[i])
    link_input.send_keys(listing_links[i])
    submit_button.click()
    time.sleep(1)
    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

driver.quit()