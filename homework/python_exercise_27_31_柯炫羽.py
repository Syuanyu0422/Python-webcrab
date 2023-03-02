import requests as req
from bs4 import BeautifulSoup

#擷取資料
url='https://www.taiwanlottery.com.tw/index_new.aspx'
html=req.get(url)

#解析資料
bs=BeautifulSoup(html.text,'html.parser')
   


lotter=bs.select('.contents_box02')
lotter_49 = lotter[3]
date_49=lotter_49.find('span',{'class':'font_black15'})
print('49樂合彩開獎日期及級數:',date_49.text)
ball_49=lotter_49.find_all('div',{'class':'ball_tx ball_yellow'})
print('49樂合彩開獎結果:',end=' ')
for i in range(len(ball_49)):
    print(ball_49[i].text,end=' ')
print()


lotter2=bs.select('.contents_box04')
lotter_4star=lotter2[1]
date_4star=lotter_4star.find('span',{'class':'font_black15'})
print('四星彩開獎日期及級數:',date_4star.text)
ball_4star=lotter_4star.find_all('div',{'class':'ball_tx ball_purple'})
print('四星彩開獎結果:',end=' ')
for i in range(4):
    print(ball_4star[i].text,end=' ')

