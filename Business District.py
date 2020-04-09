# encoding=utf8
import pandas as pd
import json
import urllib.request
import requests
import demjson
import csv

url = "D:\E Disk\Python\GPS Client\Businss District\GDSZ sample raw check v2.0.csv"
tips= pd.read_csv(url,encoding="utf-8")
pd.set_option('max_colwidth',10000)
df1=tips

def apibus(lat, lon):

  url = 'http://api.map.baidu.com/geocoder/v2/'
  ak = '1vfEYzkxd4fWornUr0mdEyMweXuqztDA' # 百度地图api密钥
  back = '&location='
  location = str(lat)+","+str(lon)
  output = '&output=json&pois=1'
  uri = url + '?'+ back + location + output+ '&ak='+ ak
  temp1 = urllib.request.urlopen(uri)
  temp2=temp1.read().decode("utf-8")
  temp3=json.loads(temp2)
  temp4 = temp3.get('result', None)
  if temp4 is not None:
    Business = temp4["business"]  # 商圈
  else:
    Business= None
  return (Business)
"""
def apidis(lat, lon):

  url = 'http://api.map.baidu.com/geocoder/v2/'
  ak = '1vfEYzkxd4fWornUr0mdEyMweXuqztDA' # 百度地图api密钥
  back = '&location='
  location = str(lat)+","+str(lon)
  output = '&output=json&pois=1'
  uri = url + '?'+ back + location + output+ '&ak='+ ak
  temp1 = urllib.request.urlopen(uri)
  temp2=temp1.read().decode("utf-8")
  jsondata=json.loads(temp2)
  Business = jsondata["result"]["business"]  # 商圈
  District = jsondata["result"]["addressComponent"]["district"]  # District
  return (District)
"""
df1['Business']=df1.apply(lambda x: apibus(x['NUM_LATITUDE'], x['NUM_LONGITUDE']), axis=1)
#df1['District']=df1.apply(lambda x: apidis(x['NUM_LATITUDE'], x['NUM_LONGITUDE']), axis=1)
df1.to_csv('GDSZ_sample_v2.0.csv')
#print(df1)