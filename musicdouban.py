import re
import requests
import pymongo
from pyquery import PyQuery as pq

MAX_PAGE = 10

def parse_page(index):
    url = 'https://music.douban.com/top250?start={}'.format((index-1)*25)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    res = requests.get(url,headers=headers).text
    doc = pq(res)
    items = doc.find('.item').items()
    pattern = re.compile(r'\d+')
    for item in items:
        numinfo = item('.pl2').find('span[class="pl"]').text()
        product = {
            'title':item('.pl2 a').text(),
            'author':item('.pl2 p').text().split('/')[0],
            'score':item('.pl2 .rating_nums').text(),
            'num':pattern.search(numinfo).group(0)
        }
        print(product)
        save_to_Mongodb(product)

def save_to_Mongodb(data):
    #连接Mongodb
    client = pymongo.MongoClient(host='localhost',port=27017)
    #指定数据库
    db = client.douban 
    #指定集合
    collection = db.doubanmusic
    collection.insert_one(data)

def main():
    for i in range(1,MAX_PAGE+1):
        parse_page(i)

if __name__ == "__main__":
    main()

