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
import csv

#define 
url = "https://450dsa.com/array"
dic={}
field_names= ['Title', 'Links']





def link_dic():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    # Wait for the page to fully render before parsing it
    dom = htmldom.HtmlDom(url)  
    dom = dom.createDom()
    time.sleep(7)
    elems = driver.find_elements(by=By.XPATH,value="//a[@href]")
    for elem in elems:
        dic[elem.text]=elem.get_attribute("href")
    driver.quit()
    return dic

# main function
if __name__ == '__main__':
    flist=link_dic()
    imp = {k: flist[k] for k in list(flist)[2:]}
    with open('donewl.txt', 'w') as f:
        for key, value in imp.items(): 
            f.write('%s:%s\n' % (key, value))







