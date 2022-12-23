import requests
from bs4 import BeautifulSoup

for id in range(523):
    response = requests.get(f'http://www.domain.net/bbs/forum-252-{id}.html')
    print(f"we are at page {id}")
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the images on the page
    tags = soup.find_all('th', class_='lock/common/new')

    for tag in tags:
        tag.find_all('a')
        link = tag.find('span').find('a')['href']
        response = requests.get(f'http://www.domain.net/bbs/{link}')

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
