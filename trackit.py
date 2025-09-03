import requests    # we can access an url to pull out data

from bs4 import BeautifulSoup

import smtplib

URL = 'https://www.amazon.in/Apple-MacBook-13-inch-Display-Dual-core/dp/B07KJQFNDQ/ref=asc_df_B07KJQFNDQ/?tag=googleshopdes-21&linkCode=df0&hvadid=397081131104&hvpos=1o4&hvnetw=g&hvrand=10860277668779493853&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007826&hvtargid=pla-614523065262&psc=1&ext_vrnc=hi'
headers = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36' }

def check_price():
    
    page = requests.get(URL, headers = headers) # returns all the data from the website

    soup = BeautifulSoup(page.content, 'html.parser') #pull out the information

    #print(soup.prettify())

    title = soup.find(id = 'productTitle').get_text()  # fetching the product title
    #print(title) # it will give all div's

    price = soup.find( id = 'priceblock_ourprice').get_text()  #it will return string
    converted_price = price[2:10]  #gives the value till 2-10 but in string

    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    a = locale.atof(converted_price)


    print(converted_price)
    print(title.strip())


    
check_price()

# or we can run it time to time 

# import time
# while(True):
#     check_price()
#     time.sleep(60*60*24)

