import pandas as pd
import re
import jieba
import jieba.posseg as pseg
url = "D:\\E Disk\\Digital\\Wechat\\WeChat Text mining\\Text_data_201806.csv"
tips = pd.read_csv(url,encoding="utf-8")
pd.set_option('max_colwidth',1000)
df1=tips[['t.openid', 't.content']]
df=df1.set_index('t.openid')
l1=[]
jieba.add_word("提前还款",tag="v")
jieba.add_word("分期",tag="v")
f = open("D:\\E Disk\\Digital\\Wechat\\WeChat Text mining\\stop_words.txt",encoding='utf-8',errors='ignore')
stopwords=[]
for line in f:
    stopwords.append(line.strip('\n'))
for index, i in df['t.content'].iteritems():
  e=( re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：]+", "",i))
  words=pseg.cut(e)
  for w in words:
       if w.word not in stopwords:
          l1.append({'t.openid': index, 'word': w.word, 'flag': w.flag})
df2=pd.DataFrame(l1)
df3=df2.groupby('word').count()
df3.to_csv('key_words_wechat.csv',encoding='utf-8')