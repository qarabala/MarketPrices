from requests import get
from bs4 import BeautifulSoup as BS
import requests 
import webbrowser

for mehsul_novu in ['fruits_vegetables/fresh_fruit/','fruits_vegetables/fruit1/','fruits_vegetables/vegetable1/','fruits_vegetables/dried_fruit/']:
    page=1
    dovr=True
    while dovr:
        url = 'https://bravomarket.online/catalog/'+mehsul_novu+'?PAGEN_1='+str(page)+'&SIZEN_1=12/'
        result=requests.get(url)
        soup=BS(result.text,'html.parser')

        #webbrowser.open(url)
        
        if(len(soup.find("div", class_="product_item_title"))):
            for tags in soup.find_all("div", class_="product_item_name_box"):
                print(tags.find("div", class_="name").text, tags.find("div",class_="price product-item-price-current").text)
            page+=1
            print(page,url)    
        else:
            dovr=False

        