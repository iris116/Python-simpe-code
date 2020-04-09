import pandas as pd
import re
import jieba
import jieba.posseg as pseg
url= open("D:\\E Disk\\Python\\TS voice text mining\\TS voice_1.1.csv",encoding='utf-8',errors='ignore')
tips = pd.read_csv(url,encoding="utf-8")
pd.set_option('max_colwidth',1000)
df1=tips[['t0.code_call_agent', 't0.text']]
df=df1[0:5].set_index('t0.code_call_agent')
l1=[]
jieba.add_word("提前还款",tag="v")
jieba.add_word("分期",tag="v")
jieba.add_word("短信",tag="v")
jieba.add_word("现金贷",tag="v")
jieba.add_word("利息太高",tag="v")
jieba.add_word("期数太长",tag="v")
jieba.add_word("消费贷",tag="v")
jieba.add_word("额度太低",tag="v")
jieba.add_word("期数太短",tag="v")
jieba.add_word("现在不需要",tag="v")
jieba.add_word("费用太高",tag="v")
f = open("D:\\E Disk\\Digital\\Wechat\\WeChat Text mining\\dic\\stop_words_TS.txt",encoding='utf-8',errors='ignore')
stopwords=[]
for line in f:
    stopwords.append(line.strip('\n'))
for index, i in df['t0.text'].iteritems():
    e = (re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：]+", "", i))
    words = pseg.cut(e)
    for w in words:
        if w.word not in stopwords:
          l1.append({'code_call_agent': index, 'word': w.word, 'flag': w.flag})
df2=pd.DataFrame(l1)
df3=df2.groupby('word').count()
print(df3)
#df3.to_csv('key_words_TS_2.csv',encoding='utf-8')