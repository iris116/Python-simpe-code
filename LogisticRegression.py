import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

car_data = pd.read_csv(r'D:\ACLtest.csv')
car_data = car_data.dropna() #去掉缺失值

#提取特征和对象类别
i = 0
for i in range(4):
  X= car_data.iloc[:, [i,i+1]]
  y= car_data.loc[:,'RACV']
#划分训练集和测试集
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#建立逻辑回归模型 ，惩罚参数为100
  lr_model = LogisticRegression(C= 100, max_iter=1000)
  lr_model.fit(X_train, y_train.astype('int'))
  predict_data = lr_model.predict(X_test)
  accuracy = np.mean(predict_data == y_test.astype('int'))
  print(accuracy)
  print(X)

i= i + 1
