from bs4 import BeautifulSoup
import requests
import re

link=f"https://jachiandmuchi.com/collections/men"
html_content=requests.get(link).text
# print(requests.get(link))

class Glass:
    def __init__(self, model,price, link):
        self.model = model
        self.price = price
        self.link = link  
glasses=[]
try:
    soup=BeautifulSoup(html_content,'lxml')
    pages=soup.find_all("span",class_='page') 
    glasses=soup.find_all('div',class_='product-grid-item')
    for index,glass in enumerate(glasses):
            model=glass.find('a',class_='product-grid-item__title').text
            price=glass.find('a',class_='product-grid-item__price').text.replace(',','.')
            link=glass.find('a',class_='product-grid-item__price')['href']
            
            glass_obj=Glass(model,price,link)
            glasses.append(glass_obj)
except requests.exceptions.HTTPError:
    print('HTTP error')
except Exception as err:
    print(err)

temp_price=100

print('cheapest glasses are : ')
for glass in glasses:
  if glass.price:
     price_number=int(re.findall(r'\d+',glass.price)[0] ) #regular expression to find number sequnce in the "price" string,then converted to a number
     if temp_price>=price_number:
         temp_price=price_number
     if(price_number==temp_price) :
         print(glass.model)
         print(glass.price)
print(temp_price)
