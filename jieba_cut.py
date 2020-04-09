#-*-coding:utf-8-*-
import pandas as pd
import re
import jieba
import jieba.posseg as pseg
url = "D:\\E Disk\\Digital\\Wechat\\WeChat Text mining\\Text_data_201806.csv"
tips = pd.read_csv(url,encoding="utf-8")
pd.set_option('max_colwidth',1000)
df1=tips[['Homer ID', 'Source']]
df=df1.set_index('Homer ID')
l1=[]
for index, i in df['Source'].iteritems():
  e=( re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：]+", "",i))
  words=pseg.cut(e)
  for w in words:
     l1.append({'Homer ID':index,'word':w.word,'flag':w.flag})
#pd.DataFrame(l1).to_csv('key_words_Sep_v1.0.csv')
df2=pd.DataFrame(l1)
df2[(df2['flag']!= ('c'))& =(df2['flag']!= ('df'))& (df2['flag']!= ('dg')) & (df2['flag']!= ('e'))
       &(df2['flag']!= ('eng'))&(df2['flag']!= ('f'))&(df2['flag']!= ('g'))&(df2['flag']!= ('h'))
       &(df2['flag']!= ('k'))&(df2['flag']!= ('m'))&(df2['flag']!= ('mq'))&(df2['flag']!= ('ng'))
       &(df2['flag']!= ('o'))&(df2['flag']!= ('p'))&(df2['flag']!= ('q'))&(df2['flag']!= ('r'))
       &(df2['flag']!= ('rr'))&(df2['flag']!= ('tg'))&(df2['flag']!= ('u'))&(df2['flag']!= ('ud'))
       &(df2['flag']!= ('ug'))&(df2['flag']!= ('uj'))&(df2['flag']!= ('ul'))&(df2['flag']!= ('uv'))
       &(df2['flag']!= ('uz'))&(df2['flag']!= ('x'))&(df2['flag']!= ('y'))&(df2['flag']!= ('yg'))
       &(df2['flag']!= ('zq'))
      ].to_csv('key_words_Sep_v1.1.csv')




