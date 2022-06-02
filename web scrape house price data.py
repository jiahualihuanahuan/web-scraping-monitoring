import requests

cookies = {
    '_ga': 'GA1.2.1414670213.1654131177',
    '_gid': 'GA1.2.569051355.1654131177',
    'g_state': '{"i_p":1654138383531,"i_l":1}',
    'storeAsyc_desk': '%7B%22access_token%22%3A%2220220601n8nm0p0h7o2ir2shge9venu739%22%2C%22userId%22%3A214164%2C%22loginAccount%22%3A%7B%22email%22%3A%22%22%2C%22phonenumber%22%3A%226478181207%22%2C%22countrycode%22%3A%22%2B1%22%7D%7D',
    'mapData_desk': '%7B%22active_base_listing_filter%22%3A%7B%22listing_days%22%3A0%2C%22sold_days%22%3A90%2C%22de_list_days%22%3A1%2C%22list_type%22%3A%5B1%2C3%5D%2C%22house_type%22%3A%5B%22all%22%5D%2C%22listing_price%22%3A%5B0%2C6000000%5D%2C%22rent_price%22%3A%5B0%2C10000%5D%7D%2C%22active_more_listing_filter%22%3A%7B%22bedroom_range%22%3A%5B0%5D%2C%22bathroom_min%22%3A0%2C%22garage_min%22%3A0%2C%22basement%22%3A%5B%5D%2C%22open_house_date%22%3A0%2C%22max_maintenance_fee%22%3A0%2C%22square_footage%22%3A%5B0%2C4000%5D%2C%22front_feet%22%3A%5B0%2C100%5D%2C%22show_comparision%22%3A1%2C%22description%22%3A%22%22%7D%2C%22school_condition%22%3A%7B%22elementary%22%3A1%2C%22secondary%22%3A1%2C%22public%22%3A1%2C%22catholic%22%3A1%2C%22match_score%22%3A0%7D%2C%22zoom%22%3A16.95%2C%22center%22%3A%7B%22lat%22%3A43.80356408870503%2C%22lng%22%3A-79.55777986647125%7D%7D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.2.1414670213.1654131177; _gid=GA1.2.569051355.1654131177; g_state={"i_p":1654138383531,"i_l":1}; storeAsyc_desk=%7B%22access_token%22%3A%2220220601n8nm0p0h7o2ir2shge9venu739%22%2C%22userId%22%3A214164%2C%22loginAccount%22%3A%7B%22email%22%3A%22%22%2C%22phonenumber%22%3A%226478181207%22%2C%22countrycode%22%3A%22%2B1%22%7D%7D; mapData_desk=%7B%22active_base_listing_filter%22%3A%7B%22listing_days%22%3A0%2C%22sold_days%22%3A90%2C%22de_list_days%22%3A1%2C%22list_type%22%3A%5B1%2C3%5D%2C%22house_type%22%3A%5B%22all%22%5D%2C%22listing_price%22%3A%5B0%2C6000000%5D%2C%22rent_price%22%3A%5B0%2C10000%5D%7D%2C%22active_more_listing_filter%22%3A%7B%22bedroom_range%22%3A%5B0%5D%2C%22bathroom_min%22%3A0%2C%22garage_min%22%3A0%2C%22basement%22%3A%5B%5D%2C%22open_house_date%22%3A0%2C%22max_maintenance_fee%22%3A0%2C%22square_footage%22%3A%5B0%2C4000%5D%2C%22front_feet%22%3A%5B0%2C100%5D%2C%22show_comparision%22%3A1%2C%22description%22%3A%22%22%7D%2C%22school_condition%22%3A%7B%22elementary%22%3A1%2C%22secondary%22%3A1%2C%22public%22%3A1%2C%22catholic%22%3A1%2C%22match_score%22%3A0%7D%2C%22zoom%22%3A16.95%2C%22center%22%3A%7B%22lat%22%3A43.80356408870503%2C%22lng%22%3A-79.55777986647125%7D%7D',
    'DNT': '1',
    'Referer': 'https://housesigma.com/web/en/map?id_listing=1DBW7RDvk5RYqlAp&zoom=16.95&center=%7B%22lat%22%3A43.80356408870503,%22lng%22%3A-79.55777986647125%7D&list_type=%5B1,3%5D',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://housesigma.com/web/en/house/1DBW7RDvk5RYqlAp/14-Leyton-Rd-Vaughan-L4L5P1-N5579124', cookies=cookies, headers=headers)
