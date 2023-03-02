# 導入模組
import xml.etree.ElementTree as et
import csv

# 讀取XML資料
file=et.parse('read.xml')
# 找到根部
root=file.getroot()

# 寫入CSV
with open('write.csv','w',newline='',encoding='UTF-8') as file:
    fwriter=csv.writer(file)
    
    for row in root:
        data=[]
        data.append(row[0].text)
        data.append(row[1].text)
        data.append(row[2].text)
        fwriter.writerow(data)
        