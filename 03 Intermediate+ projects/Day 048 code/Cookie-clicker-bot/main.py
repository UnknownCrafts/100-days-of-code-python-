from selenium import webdriver
from selenium.webdriver.common.by import By

# helper functions
def buy_something():
    
    try:
        total_money = int(driver.find_element(By.XPATH, value='//*[@id="money"]').text.replace(",", ""))
        cursor_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyCursor"]/b').text.split()[-1].replace(",", ""))
        grandma_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]/b').text.split()[-1].replace(",", ""))
        factory_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyFactory"]/b').text.split()[-1].replace(",", ""))
        mine_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyMine"]/b').text.split()[-1].replace(",", ""))
        shipment_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyShipment"]/b').text.split()[-1].replace(",", ""))
        alchemy_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text.split()[-1].replace(",", ""))
        portal_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyPortal"]/b').text.split()[-1].replace(",", ""))
        time_machine_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b').text.split()[-1].replace(",", ""))
        
        cursor_buy_button = driver.find_element(By.ID, value='buyCursor')
        grandma_buy_button = driver.find_element(By.ID, value='buyGrandma')
        factory_buy_button = driver.find_element(By.ID, value='buyFactory')
        mine_buy_button = driver.find_element(By.ID, value='buyMine')
        shipment_buy_button = driver.find_element(By.ID, value='buyShipment')
        alchemy_buy_button = driver.find_element(By.ID, value='buyAlchemy lab')
        portal_buy_button = driver.find_element(By.ID, value='buyPortal')
        time_machine_buy_button = driver.find_element(By.ID, value='buyTime machine') 
        
        if total_money >= time_machine_cost:
            time_machine_buy_button.click()
        elif total_money >= portal_cost:
            portal_buy_button.click()
        elif total_money >= alchemy_cost:
            alchemy_buy_button.click()
        elif total_money >= shipment_cost:
            shipment_buy_button.click()
        elif total_money >= mine_cost:
            mine_buy_button.click()
        elif total_money >= factory_cost:
            factory_buy_button.click()
        elif total_money >= grandma_cost:
            grandma_buy_button.click()
        elif total_money >= cursor_cost:
            cursor_buy_button.click()
    except:
        pass


# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#Webscraping 

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value='cookie')

count = 0

while True:
    cookie.click()
    if count >= 500: # buy something every half a second
        buy_something()
        count = 0
    count += 1

