# Webscraping SteamDB to find 100 of the most played games and storing that into a CSV file

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# set a headless driver
chrome_options.add_argument('--headless') 
# set the user-agent back to chrome.
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.3112.50 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')


url = "https://steamdb.info/"
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1080, 800) # set the size of the window
driver.get(url)

time.sleep(1)
rows = ["Most Played Games, 24hr Peak(dot represents comma) \n"]

# Gets the top 15 Most Played Games and their respective 24hr peak
# Somehow managed to bypass the bot detection

for i in range(1, 16):
    rows.append((driver.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[3]/a").text) + ", " + \
                (driver.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[5]").text.replace(",", ".")) + "\n")

with open("games.csv", "w") as file:
    file.writelines(rows)