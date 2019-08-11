import time
import requests
from pyquery import PyQuery as pq 

html = """<dd><a href="6169442.html">第3047章 一宗隐患</a></dd>
                        <dd><a href="6169187.html">第3046章 天敌</a></dd>
                        <dd><a href="6138510.html">第3045章 天使的黑名单</a></dd>
                        <dd><a href="6138283.html">第3044章 龙蛋商店</a></dd>
                        <dd><a href="6124938.html">第3043章 大天使的老师</a></dd>
                        <dd><a href="6108103.html">第3042章 禁咒体制</a></dd>
                        <dd><a href="6076698.html">第3041章 莫凡，你别冲动</a></dd>
                        <dd><a href="6076695.html">第3040章 关键人物</a></dd>
					<dt>《全职法师》正文</dt>
                        <dd><a href="128832.html">开新坑了！</a></dd>
                        <dd><a href="128833.html">第1章 世界大变</a></dd>
                        <dd><a href="128834.html">第2章 真实的阶级</a></dd>
 
"""
#print(type(doc('dd')))  #<class 'pyquery.pyquery.PyQuery'>

doc = pq(html)
dd = doc('dd a')      #list

n = 1
while n > 0:
    print('这是第%d次' % n)
    for i in dd.items():
        print(i.attr.href)
        n -= 1

#print(dd.attr('href'))  #调用attr方法
#print(dd.attr.href)     #调用attr属性

#对多个节点调用attr，只返回一个属性



