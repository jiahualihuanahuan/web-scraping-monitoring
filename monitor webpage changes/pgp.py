# this code monitoring a specific section of a webpage at a random interval. If changes happened, will notify by mynotifier app.

# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
import smtplib
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random

# set headers value
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


# setting the URL you want to monitor
url = 'https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/family-sponsorship/sponsor-parents-grandparents/tell-us-you-want-sponsor-parent-grandparent.html'
 
print("web monitoring script is running")
try:
	r = requests.get(url, headers = headers)
	soup = BeautifulSoup(r.content, features='lxml')
	existing_text = soup.find_all('div', class_="mwsgeneric-base-html parbase section")
	# existing_hash = hashlib.sha224(existing_text).hexdigest()
except:
	print("error")

while True:
    try:
        
        # perform the get request and store it in a var
        r = requests.get(url)
        
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string) 

        print(r.status_code)
        soup = BeautifulSoup(r.content, features='lxml')


        current_text = soup.find_all('div', class_="mwsgeneric-base-html parbase section")
        # current_hash = hashlib.sha224(current_text).hexdigest()

        # check if new hash is same as the previous hash
        if current_text == existing_text:
            print("no change")
            time.sleep(random.randint(60, 360))
            continue

        # if something changed in the hashes
        else:

            # email_alert("website has chanegd", "website has chanegd", "xxx@txt.wireless_service_provider.ca")
            # notify
            print("website has changed")

            # 2ef010f8-f0ce-4628-a6d3-4b9ef219dda1

            requests.post('https://api.mynotifier.app', 
            	{"apiKey": '2ef010f8-f0ce-4628-a6d3-4b9ef219dda1',
                "message": "PGP Started!",
                "description": "Yeah",
                "type": "info", # info, error, warning or success
                })

            # po = Pushover("<your API token/key>")
			# po.user("ubiytmrmrfuareyrvwe18gvrjb22wj")

			# msg = po.msg("This is my first notification on iOS.")

			# msg.set("title", "Hello world:)")

			# po.send(msg)
 
            # wait for 30 seconds
            time.sleep(9999)
            continue
             
    # To handle exceptions
    except Exception as e:
        print("error")
