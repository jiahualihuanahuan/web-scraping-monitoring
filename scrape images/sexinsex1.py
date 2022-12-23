# this code will download all images from a website/category
# it will iterate through all the pages
# it will get the link of children pages
# it will go to those children pages and scrape all images

import requests
from bs4 import BeautifulSoup

for id in range(523): # specify number of pages you wan to scrape
    response = requests.get(f'http://www.sexinsex.net/bbs/forum-252-{id}.html') # change 252 to other numbers to change the categories of images you want to download
    print(f"we are at page {id}")
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the images on the page
    tags = soup.find_all('th', class_='lock/common/new')

    for tag in tags:
        tag.find_all('a')
        link = tag.find('span').find('a')['href']
        response = requests.get(f'http://www.sexinsex.net/bbs/{link}')

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the images on the page
        images = soup.find_all('img')

        # Iterate over the images and download each one
        for image in images:
            try:
                image_url = image['src']
                response = requests.get(image_url)
                open(f"D:/Media/photo/{image_url.split('/')[-1]}", 'wb').write(response.content)
                print(f"downloaded {image_url.split('/')[-1]}")
            except:
                print("error")
