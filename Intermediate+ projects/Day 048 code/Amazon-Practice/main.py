from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Webscraping 

driver.get("https://www.amazon.ca/iRobot-Vacuum-Wi-Fi-Connectivity-Self-Charging-Charcoal/dp/B085D4MFS8?pd_rd_w=4z2xU&content-id=amzn1.sym.39526d57-066e-456c-bc01-eab1026394a8&pf_rd_p=39526d57-066e-456c-bc01-eab1026394a8&pf_rd_r=REMDK99KH9QFMN91KD5W&pd_rd_wg=1avGN&pd_rd_r=a83976be-9f7e-4a68-9708-0a3889255128&pd_rd_i=B085D4MFS8&ref_=pd_hp_d_btf_unk_B085D4MFS8")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(f"The price is ${price_dollar}.{price_cent}")

driver.quit()