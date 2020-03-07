# coding: utf-8
import MeCab
from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors


def morpheme_list(text):
  results = mecab.parse(text).split("\n")
  morphemes = []
  for word in results:
    if word == "EOS":
      i = "".join(l+" " for l in morphemes)[:-1]
      return i
    cols = word.split("\t")
    res_cols = cols[1].split(",")
    if res_cols[0] in ["助詞","助動詞","記号"]:
      continue
    else:
      morphemes.append(cols[0])
  #入力文を形態素ごとに空白区切したやつ
  i = "".join(l+" " for l in morphemes)[:-1]

  return i

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
model_path = 'model/word2vec.gensim.model'
model = Word2Vec.load(model_path)
