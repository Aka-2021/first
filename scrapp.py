from bs4 import BeautifulSoup
import pandas as pd
with open("xyz.txt",'r') as f:
    conetent = f.read()

soup = BeautifulSoup(conetent,"html.parser")
product = soup.find_all('div',attrs={"class":"styles__StyledProductCardBody-sc-mkgs8k-3 eZExoX"})
title=[]
price=[]
for pr in product:
    try:
        nm=pr.find('a',attrs={'class':'Link__StyledLink-sc-4b9qcv-0 styles__StyledTitleLink-sc-h3r0um-1 iBIqkb eQFZgH h-display-block h-text-bold h-text-bs'}).text
        title.append(nm)
    except:
        title.append("n/a")

    try:
        pric = pr.find('div',attrs={'class':'h-text-red'}).find('span').text
        price.append(pric)
    except:
        price.append('n/a')

df=pd.DataFrame({'Title':title,"Price":price})
print(df.head())
