import requests
from bs4 import BeautifulSoup
import os
import time

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


for page in range(3001, 3999):
    print(page)
    for indx in range(2, 999):
        print(indx)
        response = requests.get(f'https://www.meitu131.com/meinv/{page}/index_{indx}.html', headers = headers)
        print(response)
        
        if response.status_code == 200:
            #Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            try:
                title = soup.find('title').string.split('(')[0]
                print(title)
            except:
                print("title error")
            p = soup.find('div', class_="work-content")

            try:
                images = p.find_all('img')

                for image in images:
                    try:
                        image_url = image['src']
                        print(image_url)
                        response = requests.get(image_url, headers = headers)
                        print(f"downloading {image_url.split('/')[-1]}")

                        dir_name = f"D:/Media/nosql/meitu131/{title}/"
                        if not os.path.exists(dir_name):
                            os.makedirs(dir_name)
                        open(f"D:/Media/nosql/meitu131/{title}/{image_url.split('/')[-1]}", 'wb').write(response.content)
                        print(f"downloaded {image_url.split('/')[-1]}")
                    except:
                        print("error")
            except:
                print("error")
        else:
            break
