response = requests.get(f'https://www.dygod.net/html/tv/hytv/')
response.content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the images on the page
tags = soup.find_all('table', class_='tbspan')

for tag in tags:
    link = tag.find('a')['href']
    link_response = requests.get(f"https://www.dygod.net{link}")
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

        torrent_file = TorrentDownloader(f"{torrent_link}", f'D:/Media/hytv/{title}')
        torrent_file.start_download()
