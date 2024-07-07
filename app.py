from bs4 import BeautifulSoup
import requests
print('HACK JACHI AND MUCHI? ')
input(':') 
print('MUHAMMADEE MOONJII')
try:
    link="https://jachiandmuchi.com/collections/men"
    html_content=requests.get(link).text
    soup=BeautifulSoup(html_content,'lxml')
    glasses=soup.find_all('div',class_='product-grid-item')
    print(requests.get(link))
    for glass in glasses:
        title=glass.find('a',class_='product-grid-item__title').text
        price=glass.find('a',class_='product-grid-item__price').text
        link=glass.find('a',class_='product-grid-item__price')['href']
        print(f"product name :{title}")
        print(f"price :{price}")
        print(f"link :{link}")
        print('--------------------')
    
except requests.exceptions.HTTPError:
    print('HTTP error')
except Exception as err:
    print(err)
