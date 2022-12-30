# this code download images from sexinsex websites
# two loops going through different image categories and different pages under each category
# only go to the "版块主题" section to avoid downloading unnessassary contents
# get exact page title to properly store images into different folders
# only download ".jpg" format to avoid downloading unnessassary contents

import requests
from bs4 import BeautifulSoup
import os
import time

while True:
    for page in range(1,500):
        
        for i in [186,253,64,68]:    
		# 186 东方唯美图坊
    		# 253 西方唯美图坊
    		# 64 东方靓女集中营
    		# 68 西洋靓女骚妹
            # print current time on each iteration
            current_time = time.localtime()
            current_time = time.strftime("%H:%M:%S", current_time)
            print(f"start time is: {current_time} \n working on id={i}, page={page}")
            response = requests.get(f'http://www.sexinsex.net/bbs/forum-{i}-{page}.html')
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            section = soup.find_all('table', summary=f"forum_{i}")[-1]

            for css_class in ["new", "hot", "common"]: # "common", "lock", "hot"
        	# Find all the images on the page; change "class_=??" to "common", "new", "lock", hot" for various results
                tags = section.find_all('th', class_=css_class)

                for tag in tags:
                    tag.find_all('a')
                    link = tag.find('span').find('a')['href']
                    response = requests.get(f'http://www.sexinsex.net/bbs/{link}')

                    # Parse the HTML content of the page
                    soup = BeautifulSoup(response.content, 'html.parser')

                    title = soup.find('title').string.split('-')[0]
                    print(title)

                    # Find all the images on the page
                    images = soup.find_all('img')

                    dir_name = f"D:/Media/nosql/sexinsex/{title}/"
                    if not os.path.exists(dir_name):
                        os.makedirs(dir_name)

                    # Iterate over the images and download each one
                    for image in images:
                        try:
                            image_url = image['src']
                            if image_url.split(".")[-1] == "jpg":
                                response = requests.get(image_url)
                                print(f"downloading {image_url.split('/')[-1]}")

                                open(f"D:/Media/nosql/sexinsex/{title}/{image_url.split('/')[-1]}", 'wb').write(response.content)
                                print(f"downloaded {image_url.split('/')[-1]}")
                            else:
                                pass
                        except:
                            print("error")
	
	# print current time before sleep
	current_time = time.localtime()
	current_time = time.strftime("%H:%M:%S", current_time)
	print("job finished at {current_time} \n waiting for one hour before next job...")
	time.sleep(3600)
