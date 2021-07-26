import requests
from bs4 import BeautifulSoup

prod_to_track = [
    {
        "prod_url" : "https://www.amazon.in/ASIAN-Mens-Blue-Running-Shoes/dp/B085BNG4D1/ref=sr_1_2_sspa?crid=1M6LR9VZ90VWR&dchild=1&keywords=shoes+mens&qid=1626432399&sprefix=shoes%2Caps%2C409&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRDFMUTQ3SkxaN1U0JmVuY3J5cHRlZElkPUEwNzQ5ODk5MjRYUTUzN0FTUjA5TSZlbmNyeXB0ZWRBZElkPUEwMjIxMDkwMU82MjZCMkIwT05HWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name" : "APPLE"
    },
    {
       "prod_url" : "https://www.amazon.in/TECNO-Spark-Storage-Battery-Camera/dp/B096LS7N6Z/ref=sr_1_1_sspa?crid=1VTM24CGEOWF8&dchild=1&keywords=mobile+phones+under+10000%2B&qid=1626431384&sprefix=mobile+ph%2Caps%2C663&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNU9QUlA4NklITkROJmVuY3J5cHRlZElkPUEwMTA3MjI2MTNUVzhTRFdLNVc0QiZlbmNyeXB0ZWRBZElkPUEwMzAwNDI2MVBaU1NBSjlLUkFLMCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name" : "Samsung"
    }
]


def give_prod_price(URL):
    browser = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    page = requests.get(URL, headers=browser)
    soup = BeautifulSoup(page.content, 'html.parser')

    prod_price = soup.find(id="priceblock_ourprice")

    if (prod_price == None):
        prod_price = soup.find(id="priceblock_dealprice")

    return prod_price.getText()



for every_prod in prod_to_track:
    prod_price_returned = give_prod_price(every_prod.get("prod_url"))
    prod_price_returned=prod_price_returned.replace(",","")
    prod_price_returned=prod_price_returned[1:]

    print(prod_price_returned + "-" + every_prod.get("name"))

if prod_price_returned > 500:
    print("available at your price")
else:
    print("not in your range")