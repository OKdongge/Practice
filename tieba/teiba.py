import re
import requests
import pymongo
from config import *
from pyquery import PyQuery as pq 

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_data(page):
	url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(KEYWORD,(page-1)*50)
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
	html = requests.get(url,headers=headers).content
	page_source = html.decode('utf-8').replace(r'<!--','').replace(r'-->','')
	#正则表达式获取帖子标题
	pattern = re.compile(r'href="(/p/\d+)" title="(.*?)" target="_blank" class="j_th_tit ">(.*?)</a>')
	result = pattern.findall(page_source)  #return a tuple?
	print(len(result))
	for i in result:
		tiezi = {
			'url':i[0],
			'title':i[1]
		}
		print(tiezi)
		save_info(tiezi)
def get_img():
	pass

def save_info(data):
	try:
		if db[MONGO_COLLECTION].insert_one(data):
			print('succ')
	except Exception:
		print('failed')		

def main():
	for index in range(1,MAX_PAGE+1):
		get_data(index)

if __name__ == '__main__':
	main()

