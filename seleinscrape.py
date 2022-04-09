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

#define 
url = "https://450dsa.com/array"
dic={}

def link_dic():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    # Wait for the page to fully render before parsing it
    dom = htmldom.HtmlDom(url)  
    dom = dom.createDom()
    time.sleep(10)
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        dic[elem.text]=elem.get_attribute("href")
    driver.quit()
    return dic

# main function
if __name__ == '__main__':
    print(link_dic())






