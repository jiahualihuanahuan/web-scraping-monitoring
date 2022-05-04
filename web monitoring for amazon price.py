import time
import hashlib
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
from datetime import datetime

urls_dict = {
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "ZIWI Peak Wet Dog Food Beef":"https://www.amazon.ca/ZiwiPeak-Beef-Canned-Cuisine-Pack/dp/B00XQYZVY2/ref=sr_1_12?crid=KHOFYDCOQ8KR&keywords=ziwi&qid=1651623990&sprefix=ziwi%2Caps%2C90&sr=8-12&th=1",
    "ZiwiPeak Lamb Canned Dog Cuisine":"https://www.amazon.ca/ZiwiPeak-Beef-Canned-Cuisine-Pack/dp/B06W2MM9GK/ref=sr_1_12?crid=KHOFYDCOQ8KR&keywords=ziwi&qid=1651623990&sprefix=ziwi%2Caps%2C90&sr=8-12&th=1",
    "VIVO Dual LCD LED Monitor Desk Mount Stand Heavy Duty Fully Adjustable, Fits 2 Screens up to 27, STAND-V002":"https://www.amazon.ca/dp/B009S750LA?tag=camelcamelcam-20&linkCode=ogi&th=1&psc=1&language=en_CA",
    "WD_Black SN750 2TB NVMe Internal Gaming SSD":"https://www.amazon.ca/dp/B07M9VXSXG?tag=camelcamelcam-20&linkCode=ogi&th=1&psc=1&language=en_CA",
    "Business Analysis For Dummies Paperback – July 22 2013":"https://www.amazon.ca/dp/1118510585?tag=camelcamelcam-20&linkCode=ogi&th=1&psc=1&language=en_CA",
    "Mobil 1 (120758) Synthetic Motor Oil 0W-20 (Advanced Fuel Economy), 5 Quart, Pack of 3":"https://www.amazon.ca/Mobil-120758-Synthetic-Advanced-Economy/dp/B014G1ZBBG/ref=sr_1_26?crid=30J7HKT4O88G3&keywords=engine%2Boil%2B0w20&qid=1651512810&sprefix=engine%2Boil%2B0w20%2Caps%2C81&sr=8-26&th=1",
    "Mobil 1 Advanced Full Synthetic Motor Oil 0W-20 5 U.S. QTS/4.73L":"https://www.amazon.ca/Mobil-Advanced-Synthetic-Motor-4-73L/dp/B00J00X5YO/ref=sr_1_4?crid=30J7HKT4O88G3&keywords=engine+oil+0w20&qid=1651512779&sprefix=engine+oil+0w20%2Caps%2C81&sr=8-4",
    "Mobil 1 M1-110A Extended Performance Oil Filter":"https://www.amazon.ca/Mobil-M1-110A-Extended-Performance-Filter/dp/B0727SCP22/ref=sr_1_1?qid=1651512714&s=automotive&sr=1-1&vehicle=2019-59-756-113--40-6-5-22693-4171-1-1-5742-173-2&vehicleName=2019+Honda+Odyssey",
    "TCE AT83006U Torin Hydraulic Trolley Service/Floor Jack with Extra Saddle":"https://www.amazon.ca/TCE-AT83006U-Hydraulic-Trolley-Service/dp/B087DW4GNL/ref=sr_1_6?crid=34Q64VAPD2U96&keywords=floor+jack&qid=1651512662&sprefix=%2Caps%2C64&sr=8-6",
    "Norpur Pig Ears All-Natural Dog Treats (100-Count)":"https://www.amazon.ca/All-Natural-100-Count-Slow-Roasted-Oven-Baked-Boneless/dp/B00SYWARPO/ref=sxts_rp_s1_0?cv_ct_cx=Norpur&keywords=Norpur&pd_rd_i=B00SYWARPO&pd_rd_r=9abe8722-41bb-4ddd-a046-221f47ef4054&pd_rd_w=Ym5xh&pd_rd_wg=CwIRg&pf_rd_p=f246b130-b2b7-478c-84a3-51d0c82e2da1&pf_rd_r=KDDVTBGJ78HBHSQXJ8CG&psc=1&qid=1651512555&sr=1-1-f0029781-b79b-4b60-9cb0-eeda4dea34d6",
    "K9 Natural Freeze Dried Dog Food":"https://www.amazon.ca/Natural-Perfect-Healthy-Hypoallergenic-Ingredients/dp/B07P24GG7L/?_encoding=UTF8&pd_rd_w=TLuQR&pf_rd_p=07ba691b-0556-46f1-afa7-1adb1aa83156&pf_rd_r=D8NKHZY8SGPXE85PJFFS&pd_rd_r=316e6beb-b02f-473e-92fb-8422e2abed5d&pd_rd_wg=VAyQp&ref_=pd_gw_ci_mcx_mr_hp_d&th=1",
    "EVGA GeForce RTX 3090 FTW3 Ultra Gaming":"https://www.amazon.ca/EVGA-GeForce-Technology-Backplate-24G-P5-3987-KR/dp/B08J5F3G18/ref=sr_1_1?crid=IFAUG345QGKP&keywords=3090&qid=1651452996&sprefix=3090%2Caps%2C110&sr=8-1",
    "Keson RRT12 Top Reading Center Line Measuring Wheel":"https://www.amazon.ca/Keson-RRT12-Reading-Measuring-Graduations/dp/B004Y5EWN8/?_encoding=UTF8&pd_rd_w=vT2Vd&pf_rd_p=aa0eb9f1-1ea2-48b2-8ab1-b3859370648d&pf_rd_r=KDCJZ53A5FFKFSPPW11A&pd_rd_r=a528356d-6dde-4878-801e-da5cbecce608&pd_rd_wg=UVoBJ&ref_=pd_gw_ci_mcx_mi&th=1",
    "DEWALT 20V MAX* XR Leaf Blower":"https://www.amazon.ca/DEWALT-DCBL722B-Lithium-Ion-Brushless-Handheld/dp/B085DYPC1D/?_encoding=UTF8&pd_rd_w=SBkfd&pf_rd_p=65a883cc-2a99-4757-97c3-17282bb2b972&pf_rd_r=ZRGG0SXYT0TP0PCWMVFF&pd_rd_r=bbb9bfe5-28c4-41ce-b002-6acf4f611e23&pd_rd_wg=x5KdW&ref_=pd_gw_ci_mcx_mr_hp_atf_m",
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
