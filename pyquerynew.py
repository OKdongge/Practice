import re 
from pyquery import PyQuery as pq  
from lxml import etree

html = """
<div class="pl2">
        <a href="https://music.douban.com/subject/3040149/" onclick="moreurl(this,{i:'1',query:'',subject_id:'3040149',from:'music_subject_search'})" >
            Viva La Vida
                <span style="font-size:12px;">Death And All His Friends</span>
       </a>

            <a class="start_radio" target="_blank" title="试听" href="https://music.douban.com/subject/3040149/?auto_play=1#link-report"></a>
            <p class="pl">Coldplay / 2008-06-17 / 专辑 / CD / 摇滚</p>

        
        
                    <div class="star clearfix"><span class="allstar45"></span><span class="rating_nums">8.7</span>
                <span class="pl">
                    (
                            93632人评价
                    )
                </span></div>

        </div>
"""
html1 = """
<html><body><tr class="item">
                <td width="100" valign="top">
        

        <a class="nbg" href="https://music.douban.com/subject/2995812/" onclick="moreurl(this,{i:'0',query:'',subject_id:'2995812',from:'music_subject_search'})" title="Jason Mraz - We Sing. We Dance. We Steal Things.">
            <img src="https://img3.doubanio.com/view/subject/s/public/s2967252.jpg" alt="Jason Mraz - We Sing. We Dance. We Steal Things." style="width: 80px; max-height: 120px;"/>
        </a>
        </td>
        <td valign="top">
        
        <div class="pl2">
        <a href="https://music.douban.com/subject/2995812/" onclick="moreurl(this,{i:'0',query:'',subject_id:'2995812',from:'music_subject_search'})">
            We Sing. We Dance. We Steal Things.
       </a>

            <p class="pl">Jason Mraz / 2008-05-13 / Import / Audio CD / 民谣</p>

        
        
                    <div class="star clearfix"><span class="allstar45"/><span class="rating_nums">9.1</span>
                <span class="pl">
                    (
                            107193人评价
                    )
                </span></div>

        </div>
        </td>
        </tr>
</body></html>"""

doc = pq(html)
titles = doc('.pl2 a').eq(0)
for index in titles.items():
	print(index.text())



"""
authors = doc('.pl2 p')
for index in authors:                 # <class 'lxml.html.HtmlElement'> index的属性
    print(pq(index).text().split('/')[0].strip())

scores = doc('.rating_nums')
for index in scores.items():
    print(index.text())

numbers = doc('.pl2').find('span[class="pl"]')
pattern = re.compile('\d+')
collection.insert_one({"number":index.text()})
print(pattern.search(numbers.text()).group(0))

"""

#获得指定标签 eq(index)
