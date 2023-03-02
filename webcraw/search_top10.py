import requests
from bs4 import BeautifulSoup

#找出關鍵字搜尋結果排名第一頁的網頁標題及網址(純搜尋)
def key_top10(search):
    url='https://www.google.com/search?q='+search
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    html=requests.get(url,headers=headers)
    bs=BeautifulSoup(html.text,'html.parser')

    ress = bs.find_all(class_='yuRUbf')
    i=1
    for res in ress:    
        title=res.find('h3')
        print(str(i)+'.'+title.text)
        i+=1
        blog_url= res.find('a')['href']
        print(blog_url)
        print()
    

# 在此設定關鍵字
search='台中溫泉'
key_top10(search)
        
#%% 找出標題及網址，並寫入檔案

def top10_data(search):
    # 指定檔案路徑
    bold=''
    # 完整路徑+檔名
    fn= bold+search+'.csv'
    # 寫入CSV，先寫入欄標題
    with open(fn,'w') as file:
        file.writelines('標題,網址')
        file.writelines('\n')
    url='https://www.google.com/search?q='+search
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    try:
        html=requests.get(url,headers=headers)
        bs=BeautifulSoup(html.text,'html.parser')
        ress = bs.find_all(class_='yuRUbf')
    except:
        print('網頁擷取出現錯誤')
    rank=1
    print(search+'搜尋結果第一頁:')
    for res in ress: 
        try:
            title=res.find('h3')
            print(str(rank)+'.'+title.text)
            rank+=1
            blog_url= res.find('a')['href']
            # EXCEL的超連結函式
            url='=HYPERLINK("%s")' % blog_url
            with open(fn,'a') as file:
                file.writelines(title.text+','+url)
                file.writelines('\n')
            
        except:
            print('資料擷取出現錯誤')
    print('已完成寫入'+fn)

# 用迴圈找出全台各地溫泉關鍵字搜尋結果第一頁，並寫入CSV
Taiwan = ['基隆','台北','桃園','新竹','苗栗','台中','南投','彰化','雲林','嘉義','台南','高雄','屏東','宜蘭','花蓮','台東']
for i in Taiwan:
    search='%s租車' % i
    top10_data(search)
