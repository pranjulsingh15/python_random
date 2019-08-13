import requests
from bs4 import BeautifulSoup
import time

def checkprice():
    URL='https://www.amazon.in/Test-Exclusive-606/dp/B07HGJK535/ref=sr_1_1?crid=39SBQQJ10EMFN&keywords=one+plus7+pro&qid' \
    '=1565672478&s=gateway&smid=A23AODI1X2CEAE&sprefix=one+plus%2Caps%2C332&sr=8-1 '
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 '
                         'Safari/537.36'}

    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content, 'html.parser')

    title=soup.find(id="productTitle").get_text()

    price=soup.find(id="priceblock_dealprice").get_text()

    converted_price=price[2:8]
    converted_price=converted_price.replace(',','')
    converted_price=float(converted_price)

    if converted_price<50000:
        print(" Price low")
    else:
        print('Price high')

    print(converted_price)
    print(price.strip())

    print(title.strip())

if __name__=='__main__':
    while(True):
        checkprice()
        time.sleep(10)