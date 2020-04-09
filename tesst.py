import pandas as pd
import re
import jieba
import jieba.posseg as pseg
url = "D:\\E Disk\\Digital\\Wechat\\WeChat Text mining\\Text_data_201806.csv"
tips = pd.read_csv(url,encoding="utf-8")
pd.set_option('max_colwidth',1000)
df1=tips[['t.openid', 't.content']]
df=df1[0:4].set_index('t.openid')
l1=[]
jieba.add_word("提前还款",tag="v")
jieba.add_word("分期",tag="v")
f = open("D:\\E Disk\\Digital\\Wechat\\WeChat Text mining\\Dic\\stop_words.txt",encoding='utf-8',errors='ignore')
stopwords=[]
for line in f:
    stopwords.append(line.strip('\n'))
s= open("D:\\E Disk\\Digital\\Wechat\\WeChat Text mining\\Dic\\BosonNLP_sentiment_score.txt",encoding='utf-8',errors='ignore')
senList=[]
for s in senList:
    senDict[s.split(' ')[0]] = s.split(' ')[1]
print (senlist)
n= open("D:\\E Disk\\Digital\\Wechat\\WeChat Text mining\\Dic\\notDict.txt",encoding='utf-8',errors='ignore')
notList=[]
de= open("D:\\E Disk\\Digital\\Wechat\\WeChat Text mining\\Dic\\degreeDict.txt",encoding='utf-8',errors='ignore')
degreeList=[]
for line in de:
    stopwords.append(line.strip('\n'))
def sent2word(sentence):
    """
    Segment a sentence to words
    Delete stopwords
    """
    segList = jieba.cut(sentence)
    segResult = []
    for w in segList:
        segResult.append(w)
    newSent = []
    for word in segResult:
        #print('word:'+word)
      #  print (stopwords)
        if word  not in stopwords:
            newSent.append(word)
    return newSent
"""
2. 情感定位
"""
def classifyWords(wordDict):
    # (1) 情感词
    senDict =defaultdict()
    for s in senList:
        senDict[s.split(' ')[0]] = s.split(' ')[1]
    # (2) 否定词
    notList = readLines('notDict.txt')
    # (3) 程度副词
    degreeList = readLines('degreeDict.txt')
    degreeDict = defaultdict()
    for d in degreeList:
        degreeDict[d.split(',')[0]] = d.split(',')[1]

    senWord = defaultdict()
    notWord = defaultdict()
    degreeWord = defaultdict()

    for word in wordDict.keys():
        if word in senDict.keys() and word not in notList and word not in degreeDict.keys():
            senWord[wordDict[word]] = senDict[word]
        elif word in notList and word not in degreeDict.keys():
            notWord[wordDict[word]] = -1
        elif word in degreeDict.keys():
            degreeWord[wordDict[word]] = degreeDict[word]
    return senWord, notWord, degreeWord


df['sentence']=df.apply(lambda x: sent2word(x['t.content']), axis=1)
print(df)
#df.to_csv('sentence.csv', encoding='utf_8_sig')


