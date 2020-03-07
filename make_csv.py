from os import listdir, path
import json
import pandas as pd
import item

#ディレクトリのjsonファイルより対話データを取り出し

#記事ファイルをダウンロードしたディレクトリから取得する関数を定義する。
def corpus_files():
    dirs = [path.join('./json', x)
            for x in listdir('./json')]
    docs = [path.join(x, y)
            for x in dirs for y in listdir(x) ]
    return docs

#パスの中にある文章を読んで取得
def read_document(path):
  doc = ""
  with open(path, 'r') as f:
    doc = json.load(f)
    f.close()
  return doc

def corpus_to_sentences(corpus):
  docs = [read_document(x) for x in corpus]#パス取得してパスごとの文章取得してリスト
  return docs

corpus = corpus_files()#jsonファイルへのパスリストを生成
sentences = corpus_to_sentences(corpus)#一文ずつリストに保存
inp = []
opt = []
input_wakati = []

for i in range(len(sentences)):
  for j in range(len(sentences[i]["turns"])-1):
    inp.append(sentences[i]["turns"][j]["utterance"])
    opt.append(sentences[i]["turns"][j+1]["utterance"])
    input_wakati.append(item.morpheme_list(sentences[i]["turns"][j]["utterance"]))

df = pd.DataFrame({'input':inp, 'output':opt, 'input_wakati':input_wakati})
df.to_csv('data.csv', index=None)
