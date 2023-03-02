import sqlite3

#先把csv檔讀進來成為一個list
with open('109各鄉鎮市區人口密度.csv') as file:
    file=file.read()
    f=file.split()

#建立/連線資料庫
con=sqlite3.connect('exercise.db')
c=con.cursor()
print('資料庫連線成功')

#建立資料表
sql="CREATE TABLE IF NOT EXISTS population('{}' TEXT,'{}' VARCHAR(10) ,'{}' TEXT,'{}' TEXT,'{}' TEXT)"
title=f[0].split(',')
sql=sql.format(title[0],title[1],title[2],title[3],title[4])
c.execute(sql)
print('資料表建立成功')

#把csv檔案內容寫入資料表
for row in f:
    data=row.split(',')
    sql="INSERT INTO population VALUES('{}','{}','{}','{}','{}')"
    sql=sql.format(data[0],data[1],data[2],data[3],data[4])
    c.execute(sql)
    con.commit()
print('資料寫入成功')

# 顯示前5筆數據
sql=''' SELECT * FROM population '''
cur=c.execute(sql)
j=0
for row in cur:    
    if row[0]=='109':
        print(row)
        j+=1
        if j==5:
            break    

con.close()


''' SQL語法可以用LIMIT直接選取要的資料
SELECT * FROM population LIMIT 2,5   不包頭，取5筆，等於取3.4.5.6.7
'''