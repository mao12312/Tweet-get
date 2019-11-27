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
                if token.base_form not in ["こと", "よう", "そう", "これ", "それ"]:
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

wordcloud.to_file("./wordcloud_sample.png")


text = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

file_data = open("data/twitter_list.txt", "r")

for line in file_data:
    print(line)
file_data.close()


wordcloud = WordCloud(width=480, height=320)

# テキストからワードクラウドを生成する。
wordcloud.generate(text)

# ファイルに保存する。
wordcloud.to_file('wordcloud.png')

# numpy 配列で取得する。
img = wordcloud.to_array()


