import re
import time
import smtplib
from email.mime.text import MIMEText
from time import sleep

import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#抓取最新章节，发送到邮箱
class Mailhelper():
    def __init__(self):
        self.mail_host = "smtp.qq.com"
        self.mail_user = "example@qq.com"
        self.mail_pass = "yourself"
        self.port = '25'

    def send_mail(self, to_list, sub, content):
        me = "<"+ self.mail_user + ">"
        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP(self.mail_host,self.port)
            server.connect(self.mail_host) 
            server.login(self.mail_user,self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            print('已更新！已发送至邮箱!time:{}'.format(time.strftime(r"%m/%d/%Y %H:%M:%S",time.localtime())))
        except Exception as e:
            print(str(e))
            return False

def get_page():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
        }
    url = 'https://www.booktxt.net/0_595/'
    res = requests.get(url,headers=headers,verify=False)  
    res.encoding = res.apparent_encoding
    doc = pq(res.text)
    #ddlist = doc('dd')  #<class 'lxml.html.HtmlElement'>
    latest = pq(doc('dd')[-1])         #重点注意
    #d = doc('dd')    #<class 'pyquery.pyquery.PyQuery'>
    index = latest('a').attr.href
    url = "https://www.booktxt.net/0_595/" + index
    return url

def parse_data(url):
    html = requests.get(url,verify=False).content
    soup = BeautifulSoup(html,'lxml')
    try:
        content = soup.find(id='content').get_text().replace('\xa0\xa0\xa0\xa0','\n')
        title = soup.find("h1").get_text()
    except AttributeError as e:
        print('出了点问题',e)
    return content,title

def save_to_mongo(data):
    pass

def main():
    helper = Mailhelper()
    mailto_list=['szl1452@163.com']
    if url not in read_list:
        update,title = parse_data(url)
        helper.send_mail(mailto_list,title, update) #发送到邮箱
        read_list.append(url)
    else:
        print('未更新！')        

if __name__ == '__main__':
   # mailto_list=['mailyour@163.com']
   # helper = Mailhelper()
    get_page()
