# hahow 會遇到一些問題~

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get('https://hahow.in/')
print(driver.title)
soup=BeautifulSoup(driver.page_source,'lxml')
with open('hahow.html','w',encoding='UTF-8') as file:
    file.write(soup.prettify())
    print('檔案已寫入hahow.html')

driver.quit()


#%% 樂透
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)

lotto_list=[]
driver.get('https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx')
element=driver.find_element(By.ID,'Lotto649Control_history_radYM')
element.click()

while True:
    select_year= Select(driver.find_element(By.NAME,'Lotto649Control_history$dropYear'))
    year= input('請輸入你要找的樂透年份:')
    select_year.select_by_value(year)  #select_by_value裡面放的是字串
    for month in range(1,12):
        select_month= Select(driver.find_element(By.NAME,'Lotto649Control_history$dropMonth'))
        select_month.select_by_value(str(month))
       
        submit=driver.find_element(By.NAME,'Lotto649Control_history$btnSubmit')
        submit.click()
        
        html=driver.page_source
        bs=BeautifulSoup(html,'html.parser')
        #class因為有分橘色綠色，所以找td_hm就好
        table_count=len(bs.findAll('table',{'class':'td_hm'}))
        
        for i in range(table_count):
            period=bs.find('span',{'id':'Lotto649Control_history_dlQuery_L649_DrawTerm_'+str(i)})
            print('開獎期數:',period.text)
            day=bs.find('span',{'id':'Lotto649Control_history_dlQuery_L649_DDate_'+str(i)})
            print('開獎日期:',day.text)
            print('開獎結果:')
            for j in range(1,7):
                balls=[]
                ball=bs.find('span',{'id':'Lotto649Control_history_dlQuery_No'+str(j)+'_'+str(i)})                
                print(ball.text,end=' ')
                balls.append(int(ball.text))
            lotto_list.append(balls)    
            print()
            special=bs.find('span',{'id':'Lotto649Control_history_dlQuery_No7_'+str(i)})
            print('特別號:',special.text)
    check=input('還要繼續查詢嗎? 繼續請輸入Y，結束請輸入N ')
    if check.upper == 'N' :
        print('已結束，謝謝!')
    break
driver.quit()

#%%  NBA
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd

url='https://www.nba.com/stats/players/traditional'
driver=webdriver.Chrome()
driver.get(url)

# 把接受cookie點掉
accept=driver.find_element(By.ID,'onetrust-accept-btn-handler')
accept.click()

pages_remaining = True
page_num = 1
pages=soup.select_one(r'#__next > div.Layout_base__6IeUC.Layout_withSubNav__ByKRF.Layout_justNav__2H4H0 > div.Layout_mainContent__jXliI > div.MaxWidthContainer_mwc__ID5AG > section.Block_block__62M07.nba-stats-content-block > div > div.Crom_base__f0niE > div.Crom_cromSettings__ak6Hd > div.Pagination_content__f2at7.Crom_cromSetting__Tqtiq > div:nth-child(4)')
pages=pages.text.split()
pages=int(pages[-1])
print('總共有%d頁'% pages)

while pages_remaining:
    soup=BeautifulSoup(driver.page_source,'lxml')
    
    print('載入第%d頁中' % page_num)
        
    try:
        # 用CSS Selector找
        table=soup.select_one(r'#__next > div.Layout_base__6IeUC.Layout_withSubNav__ByKRF.Layout_justNav__2H4H0 > div.Layout_mainContent__jXliI > div.MaxWidthContainer_mwc__ID5AG > section.Block_block__62M07.nba-stats-content-block > div > div.Crom_base__f0niE > div.Crom_container__C45Ti > table')
        
        df= pd.read_html(str(table))  #table出來是解析物件，把她轉成字串，read_html裡面要放字串
        df[0].to_csv('All_player_stats'+str(page_num)+'.csv')  #轉Dataframe後，會是一個list，裡面放一個dataframe，所以用索引0
        print('儲存頁面:',page_num)
        
        next_page = driver.find_element(By.XPATH,r'//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[5]/button[2]')
        next_page.click()
        page_num+=1
        if page_num>pages:
            pages_remaining=False

    except:
        print('頁面%d儲存失敗' % page_num)
        pages_remaining=False


driver.quit()