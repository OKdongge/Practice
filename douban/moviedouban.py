import re
import requests
import pymongo
from pyquery import PyQuery as pq

MAX_PAGE = 10

def parse_page(index):
    url = 'https://movie.douban.com/top250?start={}'.format((index-1)*25)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    res = requests.get(url,headers=headers).text
    doc = pq(res)
    items = doc.find('.item').items()
    num_pattern = re.compile(r'\d+')
    auth_pattern = re.compile(r': (.*?) ')     #注意源代码中的&并不能匹配到
    for item in items:
        numinfo = item('.star span').eq(3).text()  
        #print(numinfo)                #为什么输出了十个
        authinfo = item('.bd').find('p[class=""]').text()
        #authinfo = item('.bd p').text()
        movie = {
                'title':item('span[class="title"]').text(),
                'author':auth_pattern.search(authinfo).group(1),
                'score':item('.rating_num').text(),
                'num':num_pattern.search(numinfo).group(0),
                'quota':item('.quote').text()  
        }
        print(movie)
        save_to_Mongodb(movie)

def save_to_Mongodb(data):
    #连接Mongodb
    client = pymongo.MongoClient(host='localhost',port=27017)
    #指定数据库
    db = client.douban 
    #指定集合
    collection = db.doubanmovie
    collection.insert_one(data)

def main():
    for i in range(1,MAX_PAGE+1):
        parse_page(i)

if __name__ == "__main__":
    main()

