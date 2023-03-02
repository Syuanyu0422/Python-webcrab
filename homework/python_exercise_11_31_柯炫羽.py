import numpy as np

X=np.random.randint(1,21,20)
print('隨機正整數:',X)
X=np.array(X).reshape(5,4)
print('X矩陣內容:')
print(X)
print('最大:',X.max())
print('最小:',X.min())
print('平均:',X.mean())
print('總和:',X.sum())
print('標準差:',np.std(X))
c=X[np.ix_([0,4],[0,3])]
print('四個角落元素:')
print(c)