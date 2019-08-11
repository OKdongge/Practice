import re
import smtplib
from email.mime.text import MIMEText

import requests
from pyquery import PyQuery as pq


#抓取最新章节，发送到邮箱
class Mailhelper():
    def __init__(self):
        self.mail_host = "smtp.qq.com"
        self.mail_user = "example@qq.com"
        self.mail_pass = "yourself"
        self.port = '25'

    def send_mail(self, to_list, sub, content):
        me = "更新了！！" + "<"+ self.mail_user + ">"
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
            print('Done')
        except Exception as e:
            print(str(e))
            return False

def get_page():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
        }
    url = 'https://www.booktxt.net/0_595/'
    #requests.packages.urllib3.disable_warnings()
    res = requests.get(url,headers=headers,verify=False)
    doc = pq(res.text)
    ddlist = doc('dd')  #<class 'lxml.html.HtmlElement'>
    for i in ddlist.items():
        print(i)
        break
#    print(ddlist[:8])
   # read_list = []

#    helper.send_mail(mailto_list,fashi[:15], fashi)#发送到邮箱


if __name__ == '__main__':
   # mailto_list=['mailyour@163.com']
   # helper = Mailhelper()
    get_page()
