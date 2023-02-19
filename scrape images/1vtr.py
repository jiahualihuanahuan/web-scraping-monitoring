# website url layout
# https://www.1vtr.com/{page_id}.html/{subpage_id}

content_hashes = []

for page_id in range(1, 130001):
    for subpage_id in range(1,1500):
        response = requests.get(f'https://www.1vtr.com/{page_id}.html/{subpage_id}')
        
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('title').string.split('-')[0]
        
        # remove some invalid character for windows directory to avoid problem
        invalid_chars = [':','<','>','?','：','!','*','|','/','.','"','传疯了']
        # iterate through all invalid characters and remove them from title
        for invalid_char in invalid_chars:
            title = title.replace(f'{invalid_char}','')
        print(title)
        print(page_id)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        try:
            content_div = soup.find_all('div', class_="entry-content clearfix")[0]
            # get a hash of the webpage and store it in a list and compare it later on to future hash value, if the same value exist, jump out of the loop and proceed with next page
            content_hash = hashlib.sha256(str(soup).encode('utf-8')).hexdigest()
            print(content_hash)
        except:
            print("content error")
        # check if new hash value in existing list of stored hash values, if yes, jump out of the loop and proceed to next one
        if content_hash in content_hashes:
            break
        # if new hash value is not in the existing hash values list, save it in the list for future page check
        else:
            content_hashes.append(content_hash)

            # Find all the images on the page
            images = content_div.find_all('img')

            dir_name = f"D:/Media/nosql/1vtr/{title}/"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            # Iterate over the images and download each one
            for image in images:
                try:
                    image_url = image['src']
                    if image_url.split(".")[-1] == "jpg":
                        response = requests.get(image_url)
                        print(f"downloading {image_url.split('/')[-1]}")

                        open(f"D:/Media/nosql/1vtr/{title}/{image_url.split('/')[-1]}", 'wb').write(response.content)
                        print(f"downloaded {image_url.split('/')[-1]}")
                    else:
                        pass
                except:
                    print("error")
