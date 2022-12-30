# this code download all torrent links in one page (for example a TV serie) and download the corresponding mp4 files

import requests
from bs4 import BeautifulSoup
from torrentp import TorrentDownloader

link_response = requests.get(f"https://www.dygod.net/html/tv/hytv/20221222/118472.html")
link_soup = BeautifulSoup(link_response.content, 'html.parser')
title = link_soup.find('title').string
if "连载至" in title:
    title = title.split('连载至')[0].split('《')[-1].split('》')[0]
    print(title)
elif "全" in title:
    title = title.split('全')[0].split('《')[-1].split('》')[0]
    print(title)
else:
    pass


tds = link_soup.find_all('td', style="WORD-WRAP: break-word")
for td in tds:
    torrent_link = td.find('a')["href"]
    print(torrent_link)

    torrent_file = TorrentDownloader(f"{torrent_link}", f'D:/Media/TV series/{title}')
    torrent_file.start_download()
