import requests
from bs4 import BeautifulSoup
import lxml
 
 
url = 'https://450dsa.com/'
reqs = requests.get(url).text
soup = BeautifulSoup(reqs, 'lxml')

data = soup.findAll('link')

    
print(data)