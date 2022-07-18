from requests import get
from bs4 import BeautifulSoup as BS
import requests 

url = 'https://neptun.az/meyve-terevez-quru-meyveler/meyve'
result=requests.get(url)
doc=BS(result.text,'html.parser')

tags=doc.find_all(["div"],class_='caption')


for tag in tags:
    price=tag.find()
    print(tag)