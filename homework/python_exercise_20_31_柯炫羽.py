import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#載入糖尿病資料庫
diabetes=datasets.load_diabetes()
#設定資料
X=pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
y=pd.DataFrame(diabetes.target,columns=['Quantitative Measure'])
#建立模型
lm=LinearRegression()
lm.fit(X,y)
#利用模型預測資料
pred_y=lm.predict(X)
#繪製散佈圖，比較預測一年後患病的定量指標和實際一年後患病的定量指標
plt.scatter(y,pred_y)
plt.title('Quantitative Measure vs Predicted Quantitative Measure')
plt.xlabel('Quantitative Measure')
plt.ylabel('Predicted Quantitative Measure')
plt.show()

#設定資料，只取age、sex、bmi、bp作為解釋變數
X=pd.DataFrame(diabetes.data[:,0:4],columns=diabetes.feature_names[0:4])
y=pd.DataFrame(diabetes.target,columns=['Quantitative Measure'])
#建立模型
lm2=LinearRegression()
lm2.fit(X,y)
#利用此模型預測資料
pred2_y=lm2.predict(X)
#繪製散佈圖
plt.scatter(y,pred2_y)
plt.title('Quantitative Measure vs Predicted Quantitative Measure')
plt.xlabel('Quantitative Measure')
plt.ylabel('Predicted Quantitative Measure')
plt.show()