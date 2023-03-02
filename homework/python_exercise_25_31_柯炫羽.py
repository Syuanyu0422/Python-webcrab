import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans,DBSCAN
from sklearn import neighbors
import warnings

warnings.filterwarnings('ignore')

report=pd.read_csv('World Happiness Report.csv')

X=pd.DataFrame(report.iloc[:,3:9])
y=report['Score']

lm=LinearRegression()
lm.fit(X,y)

y_pred=lm.predict(X)

print('截距:',lm.intercept_)
print('迴歸係數:',lm.coef_)
print('MSE:',mse(y, y_pred))
print('R-square:',lm.score(X,y))

print('='*10)
#把幸福程度做分類(網路參考資料:https://learn.microsoft.com/zh-tw/archive/msdn-magazine/2013/august/test-run-converting-numeric-data-to-categorical-data)
bins=[2,4,5,6,7,8]
labels=[0,1,2,3,4]
report.insert(3,'Score_label',pd.cut(report['Score'],bins=bins,labels=labels))
report['Score_label']=report['Score_label'].astype(int)

# 我選擇用KNN
X=pd.DataFrame(report.iloc[:,4:10])
y=np.array(report['Score_label'])

best_score=0
best_k=None
for k in range(2,len(X)):  #包含自己所以最小從2開始
    knn=neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(X,y)
    if knn.score(X,y)>best_score:
        best_score=knn.score(X,y)
        best_k=k
# 使用KNN演算法，K=2時的準確率
print('KNN準確率:',best_score)
print('='*10)

#用kmeans分成5群，顯示分群結果跟準確率
km=KMeans(n_clusters=5,random_state=50)
km.fit(X)
print('分群結果:',km.labels_)
y_pred=km.predict(X)

# 要將標籤統一化
# print(y_pred)
# print(y)
y_pred=np.choose(y_pred,[0,3,2,4,1])

print('KMeans準確率',accuracy_score(y, y_pred))
# 都好低QQ....
print('='*10)

# 用DBSCAN
X=pd.DataFrame(report.iloc[:,4:10])

# 最遙遠的距離可能是2.38多吧    
epss=np.arange(0.1,2,0.1)
for sample in range(1,156):
    for eps in epss:
        db=DBSCAN(eps=eps,min_samples=sample)
        db.fit(X)
        cluster=len(set(db.labels_))
        offset=0
        if -1 in db.labels_:
            offset=1
        if cluster-offset==5:
            print('eps為',eps,',以及min_sample為',sample,'時，可以分為5群')
# 答案不太確定，出來的正確率超級低...        