# Zillow rental webscraper

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Keep Chrome browser open after program finishes

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)

# Webscraping

response = requests.get("https://www.zillow.com/san-francisco-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-122.90505496386719%2C%22east%22%3A-122.10167971972656%2C%22south%22%3A37.488443902551765%2C%22north%22%3A37.93603850036717%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D").text
soup = BeautifulSoup(response, "html.parser")
listing_links = [x.get("href") for x in soup.find_all(name="a", class_="property-card-link")]
listing_prices = [x.getText()[:6].strip("+") if "," in x.getText()[:6].strip("+") else "{}{}{}".format(x.getText()[:6].strip("+")[:2], ",", x.getText()[:6].strip("+")[2:]) 
                  for x in soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
listing_addresses = [x.getText().strip("\n").strip() if "|" not in x.getText().strip("\n").strip() else x.getText().strip("\n").strip().split("|")[1].strip() 
                     for x in soup.find_all(name="address")]
print(listing_addresses)