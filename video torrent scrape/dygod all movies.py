# this code get all movies links and go into the movie page and download the torrent file and corresponding mp4 files

import requests
from bs4 import BeautifulSoup
from torrentp import TorrentDownloader

response = requests.get(f'https://www.dygod.net/html/gndy/dyzz/index.html')
response.content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the images on the page
tags = soup.find_all('a', class_='ulink')

for tag in tags:
    link = tag['href']
    link_response = requests.get(f"https://www.dygod.net{link}")
    link_soup = BeautifulSoup(link_response.content, 'html.parser')
    torrent_link = link_soup.find('td', style="WORD-WRAP: break-word").find('a')["href"]
    print(torrent_link)
    
    torrent_file = TorrentDownloader(f"{torrent_link}", '.')
    torrent_file.start_download()
