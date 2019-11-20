# import json
# import sys
# import glob
# import os

# from requests_oauthlib import OAuth1Session

# # Consumer Key
# CK = "EtzGyi1wh5vl67tRtIhKq9i89"
# # Consumer Secret
# CS = "mTMg8oir9DUIMsMiTDGoIiqs3clzVkdUFPnKkkibc7Y2zqlu7j"
# # Access Token
# AT = "1010784914445221895-UI2wFlCMck5CzXFzXMvR8pEMTgtK2s"
# # Accesss Token Secert
# AS = "2pNjWk8XK1eVioyQkTeY2EPoVARqTCv334jmvlro1H8gT"

# session = OAuth1Session(CK, CS, AT, AS)


# def screen_name_list(file):
#     #読み込み用データとして、fileを開いて読み込む
#     f = open(file, "r", encoding="utf-8").read()
#     #改行コード（\n）で区切ってリスト化（配列化）する
#     screen_name = f.split("\n")
#     #screen_nameリストを返却する
#     return screen_name


# train_list = glob.glob('list/*.txt')
# os.makedirs("data", exist_ok=True)

# for train in train_list:
#     screen_names = screen_name_list(train)

#     for screen_name in screen_names:
#         url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
#         params = {"screen_name": screen_name, "count": 50}

#         response = session.get(url, params=params)
#         response_text = json.loads(response.text)

#         texts = []
#         # テキスト部分を格納する
#         for data in response_text:
#             texts.append(data['text'])
#         # get()メソッド keyに対するvaluesを獲得
#         # for文の dataをget()で獲得
#         texts = [data.get('text') for data in response_text]

#         #  ディレクトリー名を書き換える
#         data_name = str(train).replace('list', 'data', 1)

#         # withブロックを使うとブロックの終了時に自動的にクローズされる
#         # 引数a 書き込み用に開き、ファイルが存在する場合は末尾に追記する
#         with open(data_name, "a") as f:
#             for text in texts:
#                 f.write(str(text)+"\n")
