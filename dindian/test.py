import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Connection':'close'
    }
url = 'https://www.booktxt.net/0_595/'
while 1:
    try:
        res = requests.get(url)
        print(res.status_code)
        print(res.text)
    except:
        print("Connection refused by the server..")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")




 
