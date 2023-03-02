i=int(input('請輸入一個整數:'))
if i%2==0 and i%7==0:
    print(i,'是2及7的倍數')
elif i%2==0 and i%7!=0:
    print(i,'是2的倍數')
elif i%2!=0 and i%7==0:
    print(i,'是7的倍數')
else:
    print(i,'不是2也不是7的倍數')
