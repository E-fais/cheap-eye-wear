from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

link=f"https://jachiandmuchi.com/collections/men"
html_content=requests.get(link).text
# print(requests.get(link))

glass_data={
     'model':[],
     'price':[],
     'link':[],
}

def exact_price(price_str):
     number_price=re.findall(r'\d+\.*\d*',price_str)
     if number_price:
          return float(number_price[0])
     else:
          return None
     

def get_glasses():
    try:
      soup=BeautifulSoup(html_content,'lxml')
      pages=soup.find_all("span",class_='page') 
      glasses=soup.find_all('div',class_='product-grid-item')

      for index,glass in enumerate(glasses):
            model=glass.find('a',class_='product-grid-item__title').text
            price=glass.find('a',class_='product-grid-item__price').text.replace(',','.')
            link=glass.find('a',class_='product-grid-item__price')['href']
            glass_data['model'].append(model)
            glass_data['price'].append(price)
            glass_data['link'].append(link)
      
    except requests.exceptions.HTTPError:
          print('HTTP error')
    except Exception as err:
          print(err)
    
    #filter cheapest glasses
    df=pd.DataFrame(glass_data)
    df['price_numeric']=df['price'].apply(exact_price) # Apply extract_price function to 'price' column to create a numeric 'price_numeric' column
    
    min_price=df['price_numeric'].min()
    cheapeast_glasses=df[df['price_numeric']==min_price]
    # print(cheapeast_glasses)

    #no need to display price_numeric to the user
    final_chart=cheapeast_glasses.drop('price_numeric',axis=1)
    
    with open('glass_data.csv',"w") as f:
     f.write('CHEAPEST GLASSES FROM JACHI AND MUCHI\n')
     final_chart.to_csv(f,sep='\t',index=False)
get_glasses()
