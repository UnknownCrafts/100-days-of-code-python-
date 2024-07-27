from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Webscraping 

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Printing out the total articles number in wikipedia
print(driver.find_element(By.XPATH, value="//*[@id='articlecount']/a[1]").text)

driver.quit()