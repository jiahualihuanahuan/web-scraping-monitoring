import requests
from bs4 import BeautifulSoup
import os
import time

while True:
	for id in [186,253,64,68]:
		# print current time on each iteration
		current_time = time.localtime()
		current_time = time.strftime("%H:%M:%S", current_time)
		print(f"start time is: {current_time} \n working on {id} job")

		response = requests.get(f'http://www.sexinsex.net/bbs/forum-{id}-1.html')
		# Parse the HTML content of the page
		soup = BeautifulSoup(response.content, 'html.parser')

		for css_class in ["new", "hot"]: # "common", "lock", "hot"
			# Find all the images on the page; change "class_=??" to "common", "new", "lock", hot" for various results
			tags = soup.find_all('th', class_=css_class)

			for tag in tags:
				tag.find_all('a')
				link = tag.find('span').find('a')['href']
				response = requests.get(f'http://www.sexinsex.net/bbs/{link}')

		        # Parse the HTML content of the page
				soup = BeautifulSoup(response.content, 'html.parser')

				title = soup.find('title').string[:10]
				print(title)

		        # Find all the images on the page
				images = soup.find_all('img')

				dir_name = f"D:/Media/nosql/photos/{title}/"
				if not os.path.exists(dir_name):
					os.makedirs(dir_name)

				# Iterate over the images and download each one
				for image in images:
					try:
						image_url = image['src']
						response = requests.get(image_url)
						print(f"downloading {image_url.split('/')[-1]}")

						open(f"D:/Media/nosql/photos/{title}/{image_url.split('/')[-1]}", 'wb').write(response.content)
						print(f"downloaded {image_url.split('/')[-1]}")
					except:
						print("error")
	
	# print current time before sleep
	current_time = time.localtime()
	current_time = time.strftime("%H:%M:%S", current_time)
	print("job finished at {current_time} \n waiting for one hour before next job...")
	time.sleep(3600)
