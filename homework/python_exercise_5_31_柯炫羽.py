# FOR迴圈
a=int(input('請輸入一個數字:'))
sum7=0
for i in range(1,a+1) :
    if i%7==0:
        sum7=sum7+i
        continue

print('從1到',a,'的總和是: ',sum7,sep='')

#%% WHILE迴圈
a=int(input('請輸入一個數字:'))
sum7=0
i=0
while i<=a :
    i+=1
    if i%7==0:
        sum7=sum7+i
        continue

print('從1到',a,'的總和是: ',sum7,sep='')

