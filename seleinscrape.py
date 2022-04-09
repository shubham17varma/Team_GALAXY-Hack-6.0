from asyncio import sleep
import os
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from htmldom import htmldom

url = "https://450dsa.com/array"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
# Wait for the page to fully render before parsing it
dom = htmldom.HtmlDom(url)  
dom = dom.createDom()
time.sleep(10)

# traverse list
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))
    





driver.quit()