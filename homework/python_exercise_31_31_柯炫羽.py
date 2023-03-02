# 建立一個大樓設計圖
class Biuld:
    def __init__(self,name,size,price,quantity):
        self._name=name
        self._size=size
        self._price=price
        self._quantity=quantity    
    def set_name(self,name):
        self._name=name
    def set_price(self,price):
        self._price=price
    def set_quantity(self,quantity):
        self._quantity=quantity
    #方法四 可以回傳四項資訊
    def get_info(self):
        return self._name,self._size,self._price,self._quantity

#設定初始值
name='A大樓設計圖'
size=30
price='300萬'
quantity=20

A1=Biuld(name,size,price,quantity)
A1.set_name('A1大樓')
A1.set_price('350萬')
A2=Biuld(name,size,price,quantity)
A2.set_name('A2大樓')
A2.set_quantity(30)
print('A1:',A1.get_info())
print('A2:',A2.get_info())
