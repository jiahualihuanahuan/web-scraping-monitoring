# this code download all torrent links in one page (for example a TV serie) and download the corresponding mp4 files

import requests
from bs4 import BeautifulSoup
from torrentp import TorrentDownloader

link_response = requests.get(f'https://www.dygod.net/html/tv/hytv/20221126/118280.html')
link_soup = BeautifulSoup(link_response.content, 'html.parser')
tds = link_soup.find_all('td', style="WORD-WRAP: break-word")
for td in tds:
    torrent_link = td.find('a')["href"]
    print(torrent_link)

    torrent_file = TorrentDownloader(f"{torrent_link}", '.')
    torrent_file.start_download()
