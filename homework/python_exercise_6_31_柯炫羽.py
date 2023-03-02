times= int(input('請輸入欲產生的個數 :'))
i=1
lista=[]
for i in range(times):
    i+=1
    #print('請輸入第',i,'個數字:',sep='')
    num=eval(input('請輸入第',i,'個數字:'))
    lista.insert(0,num)
    

lista.sort()
print(lista)
print(tuple(lista))
print(set(lista))
