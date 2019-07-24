import requests
from pyquery import PyQuery as pq 

def get_data(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
	html = requests.get(url,headers=headers).text
	page_source = html.replace(r'<!--','"').replace(r'-->','"')

	doc = pq(page_source)
	content = doc('.t_con cleafix')
	print(content)


def save_data(data):
	pass

def main():
	url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%85%A8%E8%81%8C%E6%B3%95%E5%B8%88&fr=search'
	get_data(url)



if __name__ == '__main__':
	main()