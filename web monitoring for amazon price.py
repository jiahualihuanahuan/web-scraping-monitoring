import time
import hashlib
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
from datetime import datetime

urls_dict = {
    "EVGA GeForce RTX 3090 FTW3 Ultra Gaming":"https://www.amazon.ca/EVGA-GeForce-Technology-Backplate-24G-P5-3987-KR/dp/B08J5F3G18/ref=sr_1_1?crid=IFAUG345QGKP&keywords=3090&qid=1651452996&sprefix=3090%2Caps%2C110&sr=8-1",
    "Keson RRT12 Top Reading Center Line Measuring Wheel":"https://www.amazon.ca/Keson-RRT12-Reading-Measuring-Graduations/dp/B004Y5EWN8/?_encoding=UTF8&pd_rd_w=vT2Vd&pf_rd_p=aa0eb9f1-1ea2-48b2-8ab1-b3859370648d&pf_rd_r=KDCJZ53A5FFKFSPPW11A&pd_rd_r=a528356d-6dde-4878-801e-da5cbecce608&pd_rd_wg=UVoBJ&ref_=pd_gw_ci_mcx_mi&th=1",
    "DEWALT 20V MAX* XR Leaf Blower":"https://www.amazon.ca/DEWALT-DCBL722B-Lithium-Ion-Brushless-Handheld/dp/B085DYPC1D/?_encoding=UTF8&pd_rd_w=SBkfd&pf_rd_p=65a883cc-2a99-4757-97c3-17282bb2b972&pf_rd_r=ZRGG0SXYT0TP0PCWMVFF&pd_rd_r=bbb9bfe5-28c4-41ce-b002-6acf4f611e23&pd_rd_wg=x5KdW&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
    "Hill's Science Diet Adult Large Breed Dry Dog Food, Lamb Meal & Brown Rice Recipe, 33 lb Bag":"https://www.amazon.ca/Hills-Science-Canine-Recipe-33-Pound/dp/B009B87PBY/ref=sr_1_2?crid=195DJ0QCBDQTC&keywords=hills%2Bscience%2Bdog%2Bfood&qid=1651461427&rdc=1&sprefix=hills%2Caps%2C91&sr=8-2&th=1"
}

def get_price_from_amazon(url, product_name):
    # perform the get request and store it in a var
    response = urlopen(url).read()
    soup = BeautifulSoup(response, features='lxml')
    whole = soup.find_all("span", {"class": "a-price-whole"})
    whole = whole[0].getText()
    fraction = soup.find_all("span", {"class": "a-price-fraction"})
    fraction = fraction[0].getText()
    price = f"{whole}{fraction}"
    print(f"{product_name} price is ${price}") 
    

while True:
    try:  
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        
        for key in urls_dict.keys():
            requested_url = Request(urls_dict[key],headers={'User-Agent': 'Mozilla/5.0'})
            get_price_from_amazon(requested_url, key)
        time.sleep(3600)
        continue
    # To handle exceptions
    except Exception as e:
        print("error")
