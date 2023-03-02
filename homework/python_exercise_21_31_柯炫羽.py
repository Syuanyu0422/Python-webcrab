import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import train_test_split as tts

#載入糖尿病資料庫
diabetes=datasets.load_diabetes()
#設定資料
X=pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
target=pd.DataFrame(diabetes.target,columns=['Quantitative Measure'])
y=target['Quantitative Measure']
#建立模型
lm=LinearRegression()
lm.fit(X,y)
#預測資料
pred_y=lm.predict(X)
#算出MSE跟R
mse=mse(y,pred_y)
rsquare=lm.score(X,y)
print('1.不分割資料集:')
print('MSE:',mse)
print('R-square:',rsquare)

#將資料分成訓練資料:測次資料=3:1
Xtrain,Xtest,ytrain,ytest=tts(X,y,test_size=0.25,random_state=100)
#先用訓練資料建立模型
lm1=LinearRegression()
lm1.fit(Xtrain,ytrain)
#使用測試資料來預測資料
pred_ytest1=lm1.predict(Xtest)
#算出MSE跟R
mse_test1 = np.mean((ytest-pred_ytest1)**2)
rsquare=lm1.score(Xtest,ytest)
print('2.訓練與測試比率為3:1 :')
print('MSE:',mse_test1)
print('R-square:',rsquare)

#將資料分成訓練資料:測次資料=4:1
Xtrain,Xtest,ytrain,ytest=tts(X,y,test_size=0.2,random_state=100)
#先用訓練資料建立模型
lm2=LinearRegression()
lm2.fit(Xtrain,ytrain)
#使用測試資料來預測資料
pred_ytest2=lm2.predict(Xtest)
#算出MSE跟R
mse_test2=np.mean((ytest-pred_ytest2)**2)
rsquare=lm2.score(Xtest,ytest)
print('3.訓練與測試比率為4:1 :')
print('MSE:',mse_test2)
print('R-square:',rsquare)

''' 4. 我會選擇以第三種方式建立模型，
將大部分的資料作為訓練資料做學習，再用少部分來做測試，
通常誤差值MSE較小，R-square也較高 '''
