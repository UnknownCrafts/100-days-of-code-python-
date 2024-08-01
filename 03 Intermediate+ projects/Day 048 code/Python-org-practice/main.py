from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#Webscraping 

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_links = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for i in range(len(event_links) - 1):
    events[i] = {'time': event_times[i].text,
                'name': event_links[i].text}
print(events)
driver.quit()