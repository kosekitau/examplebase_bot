# coding: utf-8
import pandas as pd
import MeCab
from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import item

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
print("学習済みモデル読み込み")
model_path = 'model/word2vec.gensim.model'
model = Word2Vec.load(model_path)
print("読み込み終わり")
df = pd.read_csv('data.csv')
df = df.dropna()


def ans(text, df):
  text_wakati = item.morpheme_list(text)#入力文の形態素解析
  wmd = lambda x: model.wv.wmdistance(text_wakati, x)
  result = df['input_wakati'].map(wmd).idxmin()
  return df['output'].iloc[result]


while True:
  text = input(">>>")
  if text == "quit":
    break
  r = item.ans(text, df)
  print(r)
