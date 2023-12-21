from bs4 import BeautifulSoup
import random
import requests
import datetime
import sqlite3
USER_AGENT_SCRAPER_BASE_URL = 'http://www.useragentstring.com/pages/useragentstring.php?name='

POPULAR_BROWSERS = ['Chrome', 'Firefox', 'Mozilla', 'Safari', 'Opera', 'Opera Mini', 'Edge', 'Internet Explorer']

def get_user_agent_strings_for_this_browser(browser):
    """
    Get the latest User-Agent strings of the given Browser
    :param browser: string of given Browser
    :return: list of User agents of the given Browser
    """

    url = USER_AGENT_SCRAPER_BASE_URL + browser
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    user_agent_links = soup.find('div', {'id': 'liste'}).findAll('a')[:20]

    return [str(user_agent.text) for user_agent in user_agent_links]


def get_user_agents():
    """
    Gather a list of some active User-Agent strings from
    http://www.useragentstring.com of some of the Popular Browsers
    :return: list of User-Agent strings
    """

    user_agents = []
    for browser in POPULAR_BROWSERS:
        user_agents.extend(get_user_agent_strings_for_this_browser(browser))
    return user_agents[3:] # Remove the first 3 Google Header texts from Chrome's user agents

def getPriceCC(url):
    random_user_agent = random.choice(get_user_agents())
    header={'User-Agent':random_user_agent}
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    products = soup.find_all("a", class_="text-dark text-truncate_3")
    for product in products:
#         current_datetime = datetime.datetime.now()
        product_name = product.string
        link = product['href']
        response = requests.get(link, headers = header)
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find("span", class_="h2-big").find("strong").string
        
        # product_details
        product_details = soup.find("table", class_="pi-specs-table")
        attributes = product_details.find_all("tr")
        product_detail = ""
        for attribute in attributes:
            tds = attribute.find_all("td")
            for td in tds:
                try:
                    product_detail = product_detail + td.string + " " 
                except:
                    print("no product detail available")
        c.execute("""INSERT INTO cc_products VALUES(?,?,?)""", (product_name, price, product_detail))
        conn.commit()

base_url = "https://www.canadacomputers.com/specials.php?cat="
conn = sqlite3.connect('pc_parts.db')
c = conn.cursor()

c.execute("""CREATE TABLE cc_products(product_name TEXT, price TEXT, product_details TEXT)""")

categories = ["CPU","Desktop+PCs","Hard+Drives%2FSolid+State+Drives","Memory","LCD%2FLED+Monitors","Motherboards","Power+Supplies"]

for cat in categories:
    url = base_url + cat
    getPriceCC(url)

conn.close()

# https://www.canadacomputers.com/index.php?cPath=4_65
    
base_url = "https://www.canadacomputers.com/index.php?cPath="
conn = sqlite3.connect('pc_parts.db')
c = conn.cursor()

c.execute("""CREATE TABLE cc_products(product_name TEXT, price TEXT, product_details TEXT)""")

categories = ["4_65","4_64","26_1832","26_1842","24_311","43_557_558","43_557_559", "43_557_5769","179_4229", "15_4232", "6_6004", "33_1938"]

for cat in categories:
    url = base_url + cat
    getPriceCC(url)

conn.close()
