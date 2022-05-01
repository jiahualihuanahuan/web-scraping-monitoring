
# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
import smtplib
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "xxx@gmail.com"
    password = "xxx"

    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
 
my_email = "xxx@gmail.com"


# setting the URL you want to monitor
url = 'a website you want to monitor.html'
 
print("web monitoring script is running")

while True:
    try:
        
        # perform the get request and store it in a var
        r = requests.get(url)
        
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string) 

        print(r.status_code)
        soup = BeautifulSoup(r.content, features='lxml')
'''
customize details can vary from website to website

        t = soup.find_all('h2')[4] 
        text = []
        for x in t:
            text.append(str(x))

        # check if new hash is same as the previous hash
        if text == xxx:
            print("website has changed")
            time.sleep(30)
            continue
 '''
        # if something changed in the hashes
        else:

            email_alert("website has chanegd", "website has chanegd", "xxx@txt.wireless_service_provider.ca")
            # notify
            print("website has chanegd")
 
            # # again read the website
            # response = urlopen(url).read()
 
            # # create a hash
            # currentHash = hashlib.sha224(response).hexdigest()
 
            # wait for 30 seconds
            time.sleep(30)
            continue
             
    # To handle exceptions
    except Exception as e:
        print("error")
