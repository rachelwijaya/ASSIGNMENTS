#%%
import json
import sys

filename = "E:/python practice/8 Oct 2019/tweets.json"
tweets_list = []
def tweet(filename, tweet_strings):
    with open(filename, 'w') as file_object:
        json.dump({"statuses": tweets_list}, file_object)
        tweets_list.append({"text" : tweet_strings})
def twitter():
    print("----------TWITTER----------")
    print("1. Show tweets")
    print("2. Tweet")
    while 1:
        choose = int(input("Enter choice 1 or 2: "))
        if choose == 1:
            with open(filename) as f_obj:
                content = json.load(f_obj)
                tweets_list = content["statuses"]
                for i in range(len(tweets_list)):
                    print(tweets_list[i]["text"])
        elif choose == 2:
            tweet = str(input)