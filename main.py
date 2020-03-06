# coding: utf-8
import pandas as pd
import MeCab
import re
from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
print("学習済みモデル読み込み")
model_path = 'model/word2vec.gensim.model'
model = Word2Vec.load(model_path)
print("読み込み終わり")
df = pd.read_csv('data.csv')

def morpheme_list(text):
  results = mecab.parse(text).split("\n")
  morphemes = []
  for word in results:
    if word == "EOS":
      break
    cols = word.split("\t")
    res_cols = cols[1].split(",")
    if res_cols[0] in ["助詞","助動詞","記号"]:
      continue
    else:
      morphemes.append(cols[0])
  #入力文を形態素ごとに空白区切したやつ
  i = "".join(l+" " for l in morphemes)[:-1]

  return i

#データの呼び出しと書き込み。
def ans(text, df):
  text_wakati = morpheme_list(text)#入力文の形態素解析
  wmd = lambda x: model.wv.wmdistance(text_wakati, x)
  result = df['input_wakati'].map(wmd).idxmin()
  return df['output'].iloc[result]


while True:
  text = input(">>>")
  if text == "quit":
    break
  r = ans(text, df)
  print(r)
