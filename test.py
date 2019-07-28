from pyquery import PyQuery as pq 
import requests
doc = pq(filename='tieba.html',encoding='utf-8')
items = doc('.t_con cleafix')
print(items)