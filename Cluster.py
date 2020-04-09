# 目标：把n个样本点划分到K个类中，使得每个点属于离它最近的质心对应的类，以之作为聚类的标准
# 随机找出三个点，作为质点
# 其他的点，分别于这三个点记录最近的点一组
# 把每组中心，作为新的质点
# 再次计算每个点，与质心的距离，归为质心最近的那一组
# 把每组的中心，作为新的质点
# 如果新的分组成员不在变化，并且质心不在变化，聚类完成
# API:
# sklearn.cluster.Kmeans(n_cluters_要聚类的个数 = 8)
# fit(data_训练数据) 训练模型
# predict(data_需要预测的数据)

# 典型的基于距离的非层次聚类算法，在最小化误差函数的基础上将数据划分预定的类数K，采用距离作为相似性的评级指标
# K的含义：K是人工固定好的数字，假设数据集合可以分为K个簇，由于是依靠人工定好，需要一点先验知识
# 算法过程   聚类的结果可能依赖于初始聚类中心的随机选择，可能使得结果严重偏离全局最优分类，需要多次测试K值
# 1. 从N个样本数据中随机选取K个对象作为初始的聚类中心
# 2. 分布计算每个样本到各个聚类中心的距离，将对象分配到距离近的聚类中
# 3. 所有对象分配完成后，重新计算K各聚类的中心
# 4. 与前一次计算得到的K个聚类中心比较，如果聚类中心发生变化，换过程2，否则转过程5
# 5. 当质心不发生变化时停止输出聚类结果
# 数据类型与相似性的度量
# 连续属性，先要对各个属性值进行标准化，在进行距离计算
# 文档数据，使用余弦相似度度量，现将文档整理成文档-词矩阵格式
# 目标函数
# 代码模型解释
# .fit()  来训练模型
# .lable_ 训练好之后，给样本数据的标签
# .predict() 预测新的输入的标签
import numpy as np
import pandas as pd
import xlrd

#参数初始化
inputfile = 'D:/E Disk/Python/Cluster case/SAT_POS_raw data_1.xlsx' #销量及其他属性数据
outputfile = 'D:/E Disk/Python/Cluster case/SAT_POS_result.xlsx' #保存结果的文件名
k = 3 #聚类的类别
iteration = 500 #聚类最大循环次数
data = pd.read_excel(inputfile, index_col = 'Code salesroom') #读取数据
data_zs = 1.0*(data - data.mean(axis=0))/data.std(axis=0) #数据标准化

from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration) #分为k类，并发数4
model.fit(data_zs) #开始聚类

#简单打印结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'类别数目'] #重命名表头

#详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别'] #重命名表头
r.to_excel(outputfile) #保存结果


