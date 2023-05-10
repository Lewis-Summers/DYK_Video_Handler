import time

import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

# initialize the webdriver
driver = webdriver.Chrome()

# navigate to the website
driver.get("https://www.thefactsite.com/1000-interesting-facts/")
time.sleep(14)
# find all elements with class "list" and <p> tag size
elements = driver.find_elements(By.XPATH, "//p[@class='list']")

# loop through the elements and print their text
for element in elements:
    with open('/unused scripts/factsSifter/xtraFacts.txt', 'a', encoding="utf-8") as file:
        file.write(element.text+"\n")

# close the webdriver
driver.quit()
