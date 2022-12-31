# download torrent files

import requests
from bs4 import BeautifulSoup
import os
import time
import random
from torrentp import TorrentDownloader

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

for id in range(1,500):
    # 143 亚洲成人无码原创区
    # 25 亚洲无码区
    # 230 亚洲成人有码原创区
    # 229 欧美成人无码原创区
    response = requests.get(f'http://www.sexinsex.net/bbs/forum-143-{id}.html', headers = headers)
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    for tipe in ["new","common","lock"]:
        ths = soup.find_all('th', class_=tipe)

        for th in ths:
            link = th.find('span').find('a')['href']
            print(link)
            try:
                title = th.find_all('a')[1].string
                print(title)
                if  title.__contains__("fc2") or title.__contains__("FC2"):
                    link_response = requests.get(f'http://www.sexinsex.net/bbs/{link}', headers = headers)
                    link_soup = BeautifulSoup(link_response.content, 'html.parser')

                    attachment = link_soup.find('dl', class_='t_attachlist').find('a')['href']
                    attachment_name = link_soup.find('dl', class_='t_attachlist').find('a').string
                    response = requests.get(f'http://www.sexinsex.net/bbs/{attachment}', headers = headers)
                    open(f"D:/Media/torrent/{attachment_name}", 'wb').write(response.content)

                    torrent_file = TorrentDownloader(f"D:/Media/torrent/{attachment_name}", f'D:/Media/nosql/fc2/')
                    torrent_file.start_download()   
                else:
                    pass
            except:
                print("title error")
