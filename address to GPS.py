# encoding=utf8
import pandas as pd
import json
import urllib.request
import urllib.parse
import requests
import demjson
import csv

url = "D:\E Disk\Python\GPS Client\Businss District\TJ sample POS vs home raw v1.2.csv"
tips= pd.read_csv(url,encoding="utf-8")
pd.set_option('max_colwidth',10000)
df1=tips

def apiadd(address):

  url = 'http://api.map.baidu.com/geocoder/v2/'
  ak = '1vfEYzkxd4fWornUr0mdEyMweXuqztDA' # 百度地图api密钥
  add=urllib.parse.quote(address)
  output = '&output=json&ak='
  uri = url+'?address='+ add+ output+ak
  temp1 = urllib.request.urlopen(uri)
  temp2=temp1.read().decode("utf-8")
  temp3=json.loads(temp2)
  temp4=temp3.get('result',None)
  if temp4 is not None:
      lat= temp4["location"]["lat"]
      lng= temp4["location"]["lng"]
  else:
      lat=None
      lng=None
 # lng=((temp3.get("result",None)).get("location",None)).get("lng",None)
 # District = jsondata["result"]["addressComponent"]["district"]  # District
  return (lat,lng)

df1['gps']=df1.apply(lambda x: apiadd(x['HOME_ADDRESS']), axis=1)
#df1['District']=df1.apply(lambda x: apidis(x['NUM_LATITUDE'], x['NUM_LONGITUDE']), axis=1)
df1.to_csv('TJ_client_home_gps_v2.csv')


