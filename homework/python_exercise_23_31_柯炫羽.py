from sklearn import datasets,neighbors,tree
import pandas as pd
from sklearn.model_selection import train_test_split as tts

#載入資料
iris=datasets.load_iris()
#設定資料
X=pd.DataFrame(iris.data,columns=iris.feature_names)
target=pd.DataFrame(iris.target,columns=['target'])
y=target['target']
#使用KNN，K=50，建模查看正確率
k=50
knn=neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X,y)
print('KNN正確率:',knn.score(X, y))
#使用決策數，層數=4，建模查看正確率
dtree=tree.DecisionTreeClassifier(max_depth=4)
dtree.fit(X,y)
print('tree正確率:',dtree.score(X,y))
#訓練資料:測試資料=3:2，使用KNN，調整k值，建模查看正確率
Xtrain,Xtest,ytrain,ytest=tts(X,y,test_size=0.4,random_state=50)
k=11
knn2=neighbors.KNeighborsClassifier(n_neighbors=k)
knn2.fit(Xtrain,ytrain)
print('訓練資料:測試資料=3:2的正確率:',knn2.score(Xtest,ytest))
