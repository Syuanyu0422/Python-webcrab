from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url= 'https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx'
driver=webdriver.Chrome()
driver.get(url)

years= ['105','107','109']

for year in years:
    period10= year+'000010'
    period_input = driver.find_element(By.ID,'SuperLotto638Control_history1_txtNO')
    period_input.clear()
    period_input.send_keys(period10)
    print(year+'年第10期:')
    submit=driver.find_element(By.NAME,'SuperLotto638Control_history1$btnSubmit')
    submit.click()
    html=driver.page_source
    bs=BeautifulSoup(driver.page_source,'html.parser')
    print('第一區開獎號碼(依開出順序):')
    for i in range(1,7):
        ball=bs.find('span',{'id':'SuperLotto638Control_history1_dlQuery_SNo'+str(i)+'_0'})
        print(ball.text,end=' ')
    print()
    special=bs.find('span',{'id':'SuperLotto638Control_history1_dlQuery_SNo7_0'})
    print('第二區號碼:',special.text)
    print('='*20)

driver.quit()    