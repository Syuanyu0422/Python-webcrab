from sklearn import datasets,metrics,neighbors
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans,DBSCAN
from sklearn.model_selection import train_test_split as tts

#載入資料
wine=datasets.load_wine()
#設定資料
X=pd.DataFrame(wine.data,columns=wine.feature_names)
y=wine.target

#使用Kmeans分成三群，算出其正確率
k=3
kmeans=KMeans(n_clusters=k,random_state=20)
kmeans.fit(X)

# print(kmeans.labels_)
# print(y)
#標籤統一  0->1 1->2 2->0
y_pred=np.choose(kmeans.labels_,[1,2,0])

print('Kmeans正確率:',metrics.accuracy_score(y, y_pred))

#找一下那些自變數對應變數影響較大
lm=LinearRegression()
lm.fit(X,y)
coef=lm.coef_
'''
對預測結果較有影響的自變數:
    6 flavanoids
    7 nonflavanoid_phenols
    11 od280/od315_of_diluted_wines
'''
#純觀察
# colormap=np.array(['r','g','b'])
# plt.figure(figsize=(15,5))
# plt.subplot(1,2,1)
# plt.scatter(X.iloc[:,6],X.iloc[:,11],color=colormap[y_pred])
# plt.xlabel('flavanoids')
# plt.ylabel('nonflavanoid_phenols')
# plt.title('Kmeans predict')
# plt.subplot(1,2,2)
# plt.scatter(X.iloc[:,6],X.iloc[:,11],color=colormap[y])
# plt.xlabel('flavanoids')
# plt.ylabel('nonflavanoid_phenols')
# plt.title('real class')
'''
發現用欄位6,11還有6,7當XY軸做出來的散佈圖，
可以很明顯的看出距離與分類之間的關係很大!
所以選擇了用KNN，而且KNN可以用有答案的資料來學習建模，
正確率也會比Kmeans還高~
'''
#使用三個與應變數最有關係的欄位來做建模學習
X=pd.DataFrame([X.iloc[:,6],X.iloc[:,7],X.iloc[:,11]]).T
X.columns=['flavanoids','nonflavanoid_phenols','od280/od315_of_diluted_wines']
#使用KNN分類，因為有答案先把資料分為訓練及測試
Xtrain,Xtest,ytrain,ytest=tts(X,y,test_size=0.33,random_state=100)
#建立模型
knn=neighbors.KNeighborsClassifier(n_neighbors=9)
knn.fit(Xtrain,ytrain)
print('knn正確率:',knn.score(Xtest, ytest))
y_pred_knn=knn.predict(Xtest)
print(y_pred_knn)
print(ytest)


#純觀察
# colormap=np.array(['r','g','b'])
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.scatter(Xtest.iloc[:,0],Xtest.iloc[:,2],color=colormap[y_pred_knn])
# plt.xlabel('flavanoids')
# plt.ylabel('nonflavanoid_phenols')
# plt.title('Knn predict')
# plt.subplot(1,2,2)
# plt.scatter(Xtest.iloc[:,0],Xtest.iloc[:,2],color=colormap[ytest])
# plt.xlabel('flavanoids')
# plt.ylabel('nonflavanoid_phenols')
# plt.title('real class')


