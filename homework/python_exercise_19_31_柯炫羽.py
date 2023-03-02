# 導入模組
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#設定資料
height=np.array([147,163,159,155,163,158,172,161,153,161])
weight=np.array([41,60,47,53,48,55,58.5,49,46,52.5])

X=pd.DataFrame(height,columns=['Height'])
y=pd.DataFrame(weight,columns=['Weight'])

#建立模型
lm=LinearRegression()
lm.fit(X,y)

#預測身高155、165的體重
predict_height=pd.DataFrame([155,165],columns=['Predict Height'])
predict_weight=lm.predict(predict_height)
print('預測身高155的體重為: %.1f'% predict_weight[0][0])
print('預測身高165的體重為: %.1f'% predict_weight[1][0])
#輸出迴歸係數及截距
print('迴歸係數:',lm.coef_)
print('截距:',lm.intercept_)

#預測體重55、65、70的身高
#建立模型 (自變數改為體重y 應變數則為身高X)
lm2=LinearRegression()
lm2.fit(y,X)
predict_weight=pd.DataFrame([55,65,70],columns=['Predict Weight'])
predict_height=lm2.predict(predict_weight)

#以圖示表示，先畫出散佈圖
plt.scatter(X,y)
plt.xlabel('Height')
plt.ylabel('Weight')
#繪製完整的迴歸線
regression_height=lm2.predict(y)
plt.plot(regression_height,weight,color='green')
#標記出三個體重個別對應到的預測身高
plt.plot(predict_height,predict_weight,color='red',marker='.',markersize=10)

#輸出預測的身高
print('預測體重55、65、70的身高分別為:')
for height in predict_height:
    print('%d'% height,end='\t')
