import json
import sys
import glob
import os

from requests_oauthlib import OAuth1Session

# Consumer Key
CK = "EtzGyi1wh5vl67tRtIhKq9i89"
# Consumer Secret
CS = "mTMg8oir9DUIMsMiTDGoIiqs3clzVkdUFPnKkkibc7Y2zqlu7j"
# Access Token
AT = "1010784914445221895-UI2wFlCMck5CzXFzXMvR8pEMTgtK2s"
# Accesss Token Secert
AS = "2pNjWk8XK1eVioyQkTeY2EPoVARqTCv334jmvlro1H8gT"

session = OAuth1Session(CK, CS, AT, AS)


def screen_name_list(file):
    # open and read file
    f = open(file, "r", encoding="utf-8").read()
    # split(\n) create array
    screen_name = f.split('\n')
    return screen_name


# get .txt file in the list folder
train_list = glob.glob('list/*.txt')
# create "data" dirctory at the same level as list
# exist_ok=True: same file already exists does not cause an error
os.makedirs("data", exist_ok=True)

# get tweet-data
for train in train_list:
    # run screen_name_list
    screen_name = screen_name_list(train)
    # set Api URL for getting users timeline
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

    # set number of tweets to retrieve at one time
    params = {"screen": screen_name, "count": 100}
    # access Twitter Api and read data
    response = session.get(url, params=params)
    response_text = json.loads(response.text)

    # Prepare a list to store data read from Twitter API
    texts = []

    # tweet data append array (texts)
    for data in response_text:
        texts.append(data['text'])

    # rename list directory
    data_name = str(train).replace('list', 'data', 1)

    # open the file to write tweet-data
    with open(data_name, "a") as f:
        for text in texts:
            # ツイートのテキストを書き込む
            f.write(str(text) + "\n")