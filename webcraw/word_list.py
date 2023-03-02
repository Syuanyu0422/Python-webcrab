import time
import requests
from bs4 import BeautifulSoup

#觀察網址結構
url='https://www.majortests.com/word-lists/word-list-{0}.html'

for i in range(1,16):
    #每一頁的網址結構
    if i<10:
        url2 = url.format('0'+str(i))
    else:
        url2 = url.format(i)
    r= requests.get(url2)    
    print('網址:',url2)
    print('稍等3秒鐘')
    time.sleep(3)
    bs=BeautifulSoup(r.text,'lxml')
    word_list=bs.find_all(class_='wordlist')
    print('此網址內所有單字表的單字:')
    for group in word_list:
        words=group.find_all('th')
        print('GROUP',i)
        i+=1
        for word in words:
            print(word.text)
        print('-'*15)