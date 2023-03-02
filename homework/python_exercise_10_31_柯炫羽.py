import json
with open('drugstore.json',encoding='UTF-8') as file:
    data=json.load(file)
    ntp=[]
    for row in data:
        if row[0]['機構狀態']=='開業' and row[2]['地址縣市別']=='新北市':
            ntp.append(row)

    name=[]
    add=[]    
    for items in ntp[10:20]:
        print(items[1]['機構名稱'],end=' ')
        print(items[2]['地址縣市別'],items[3]['地址鄉鎮市區'],items[4]['地址街道巷弄號'],sep='')
   