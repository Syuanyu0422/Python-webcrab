# 樂透
import requests as req
from bs4 import BeautifulSoup
#擷取資料
url='https://www.taiwanlottery.com.tw/index_new.aspx'
html=req.get(url)   
#解析資料
bs=BeautifulSoup(html.text,'html.parser')

data=bs.select('.contents_box02')  

lotter=data[2].find_all('div',{'class':'ball_tx ball_yellow'})  #屬性有些可以不用帶到全部

print('大樂透黃球開獎:')
print('開出順序:',end=' ')
for i in range(0,6):
    print(lotter[i].text,end=' ')
    
print('\n大小順序:',end=' ')
for i in range(6,12):
    print(lotter[i].text,end=' ') 

spe=data[2].find('div',{'class':'ball_red'})
print('\n大樂透紅球特別號:',spe.text)

#%% 蘋果新聞 (已停更)
import requests as req
from bs4 import BeautifulSoup

url='https://www.appledaily.com.tw/realtime/recommend/'
html=req.get(url)

bs=BeautifulSoup(html.text,'html.parser')

news=bs.select('.stories-container')

title=news[0].find_all('span')

print('前10熱門焦點新聞:')
X=1
for i in range(1,11):
    print(X,end='. ')
    print(title[i].text)    
    X+=1
    
#%% 雅虎新聞

url='https://tw.news.yahoo.com/'
html=req.get(url)

bs=BeautifulSoup(html.text,'html.parser')

news=bs.find_all('li',{'class':'Pos(r)'})
X=1
for i in news[:10]:
    print(X,i.text,sep='. ')
    X+=1
    
#%% 下載教育部網站首頁的圖片
import os
import urllib

url='https://www.edu.tw/Default.aspx'
html=req.get(url)

bs=BeautifulSoup(html.text,'html.parser')

links=bs.find_all('img')  

pics_dir='pics'

if not os.path.exists(pics_dir):  #如果這個PY黨的路徑裡不存在這個目錄
    os.mkdir(pics_dir)    # os.mkdir('資料夾名稱') 創建這個目錄
    
for link in links:
    src=link.get('src')    
    fn=src.split('/')[-1]   #檔案名稱直接用分割的找到最後一個    
    if src!=None and ('.jpg' in src or '.png' in src):  
        #確定這個src是存在的的而且以jpg或png為結尾才是圖檔
        print('完整檔案路徑:',src)
        try:
            image= urllib.request.urlopen(src)
            with open(os.path.join(pics_dir,fn),'wb') as file:  
                #wb -> 圖片是用byte寫入 所以用'wb'
                file.write(image.read()) #write(裡面要放字串)  image.read()出來就是字串
                print('下載成功 %s' % fn)
        except:
            print('下載失敗')            
            