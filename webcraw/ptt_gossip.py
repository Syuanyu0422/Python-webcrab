import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


#上網爬文說要判斷element是否存在要自己寫函數
def element_exist():
    try:
        artical.find_element(By.TAG_NAME,'a')
        return True
    except:
        return False
    

#第一題 (置頂文章會出現)
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
driver=webdriver.Chrome()
driver.get(url)
#思考一下自己滿18了嗎
time.sleep(3)

try:
    #點擊我已滿18歲
    driver.find_element(By.NAME,'yes').click()
    
    #n代表第幾篇文章
    n=0
    while n<100:
        articals = driver.find_elements(By.CLASS_NAME,'r-ent')
        for artical in articals:
            if element_exist():
                n+=1
                print('第%d篇' % n)
                print('標題:',artical.find_element(By.CLASS_NAME,'title').text)
                print('留言者:',artical.find_element(By.CLASS_NAME,'author').text)           
                print('連結網址:',artical.find_element(By.TAG_NAME,'a').get_attribute('href'))
            if n==100:
                break
        # if n==10:
        #     break
        #點上一頁
        last=driver.find_element(By.CSS_SELECTOR,'#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)')
        last.click()
        #睡一下
        time.sleep(3)
        soup=BeautifulSoup(driver.page_source,'lxml')
except:
    print('出現錯誤')    
driver.quit()

#%%
#第二題
#最舊的網址從index1開始，第二頁為index2，以此類推
url= 'https://www.ptt.cc/bbs/Gossiping/index{0}.html'
#用n去算50篇文章
n=1
#i代表index頁數
i=1
while n<51:
    url2=url.format(i)
    try:
        #分級內容，設定cookies
        r=requests.get(url2,cookies={'over18':'1'})
        soup=BeautifulSoup(r.text,'lxml')
        #找出每一篇有爆文章
        tag_divs = soup.find_all('div',class_='r-ent')
        for tag in tag_divs:
            if n==51:
                break
            #找出有爆的!
            if tag.find('span') and tag.span.text == '爆':
                print('目前在第%d頁' % i)
                print('第%d篇有爆的文章' % n)
                print('標題:',tag.a.text)
                print('留言者',tag.find(class_='author').text)
                print('連結網址','https://www.ptt.cc'+tag.a['href'])
                n+=1
                #睡一下
                time.sleep(3)
        i+=1
    except:
        print('擷取失敗，出現錯誤')

