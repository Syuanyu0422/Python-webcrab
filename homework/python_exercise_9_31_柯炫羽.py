import json as js
fn='jsonoutput.json'
data={'breakfast':50,'lunch':80,'dinner':100}
with open(fn,'w') as file:
    js.dump(data,file)

with open(fn,) as file1:
    data1=js.load(file1)
    print('早餐費用 :',data1['breakfast'],'元')
    print('中餐費用 :',data1['lunch'],'元')
    print('晚餐費用 :',data1['dinner'],'元')
    