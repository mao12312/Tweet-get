# coding:utf-8
import numpy as np
import csv
from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
from collections import Counter, defaultdict

# 名詞だけ抽出、単語をカウント


def counter(texts):
    t = Tokenizer()
    words_count = defaultdict(int)
    words = []
    for text in texts:
        tokens = t.tokenize(text)
        for token in tokens:
            # 品詞から名詞だけ抽出
            pos = token.part_of_speech.split(',')[0]
            if pos in ['名詞']:
                # 必要ない単語を省く(実際の結果を見てから不必要そうな単語を記載しました)
                if token.base_form not in ["こと", "よう", "そう", "これ", "それ", "本田", "カードバトル", "pepsi","フォロー","jpn","バトル","コイン","ペプシ","フォロー","RT","ジャパン","コーラ","カード","プレゼント","毎日","挑戦","ケース","記念"]:
                    words_count[token.base_form] += 1
                    words.append(token.base_form)
    return words_count, words


with open('data/twitter_list.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    texts = []
    for row in reader:
        if(len(row) > 0):
            text = row[0].split('http')
            texts.append(text[0])

words_count, words = counter(texts)
text = ' '.join(words)

# fontは自分の端末にあるものを使用する
fpath = "~/Library/Fonts/Ricty-Bold.ttf"
wordcloud = WordCloud(background_color="white",
                      font_path=fpath, width=900, height=500).generate(text)

wordcloud.to_file("./wordcloud_sample1.png")
