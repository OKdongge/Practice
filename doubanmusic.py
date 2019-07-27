import re
import requests
import pymongo
from pyquery import PyQuery as pq

#连接Mongodb
client = pymongo.MongoClient(host='localhost',port=27017)
#指定数据库
db = client.douban 
#指定集合
collection = db.doubanmusic

url = 'https://music.douban.com/top250?start=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
res = requests.get(url,headers=headers).text
doc = pq(res)

titles,authors,scores,numbers = [],[],[],[]

titlesItems = doc('.pl2 a')
for index in titlesItems.items():
	if index.text():
	#	collection.insert_one({'title':index.text()})
		titles.append(index.text())

authorsItems = doc('.pl2 p')
for index in authorsItems:  #     # <class 'lxml.html.HtmlElement'>  index的属性
	name = pq(index).text().split('/')[0].strip()
#	collection.insert_one({'author':name})
	authors.append(name)

scoresItems = doc('.rating_nums')
for index in scoresItems.items():
#	collection.insert_one({'score':index.text()})
	scores.append(index.text())

numbersItems = doc('.pl2').find('span[class="pl"]')
pattern = re.compile(r'\d+')
for index in numbersItems.items():
	number = pattern.search(index.text()).group(0)
#	collection.insert_one({"number":number})
	numbers.append(number)

#添加到一个字典中
def gentDict():
	for i in range(25):
		yield {
			'author':authors[i],
			'title':titles[i],
			'score':scores[i],
			'number':numbers[i]
		}


print(titles,authors,scores,numbers)
print(len(titles),len(authors),len(scores),len(numbers))
