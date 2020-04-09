#-*-coding:utf-8-*-
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import numpy as np
import re
url = "D:\E Disk\Python\GPS Client\Businss District\TJ sample POS vs home raw v1.1.csv"
tips= pd.read_csv(url,encoding="utf-8")
pd.set_option('max_colwidth',10000)
df1=tips
df1[['Client_home_lgt']].astype(float)
df1[['Client_home_lat']].astype(float)
#df1.fillna(0,inplace=True)
#df1['LONGITUDE_WORK'] = df1['LONGITUDE_WORK'].astype(float)
#df1['LATITUDE_WORK'] = df1['LATITUDE_WORK'].astype(float)
#计算两点间距离
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半径，单位为公里
    distance=c * r * 1000
    return (distance)

df1['Distance_pos2home']=df1.apply(lambda x: haversine(x['NUM_LONGITUDE'], x['NUM_LATITUDE'], x['Client_home_lgt'], x['Client_home_lat']), axis=1)
/df1.to_csv('TJ sample POS vs home result v1.0.csv')
