import tweepy
import config
import demoji
import re
import csv

def run():
    api = config.get_api()
    all_list = []
    total = 100000

    # q = "? since:2019-06-15 unitl:2019-06-16 -filter:retweets exclude:retweets lang:ja"
    q = "国葬 exclude:nativeretweets"
    for i, tweet in enumerate(tweepy.Cursor(api.search_tweets, q=q, result_type="mixed", tweet_mode='extended').items(total)):
        text, ok = is_valid_tweet(tweet)
        if ok == False:
            continue

        all_list.append(text)

        print(i, "/", total)
    print(all_list)
    output_to_csv(all_list)

def clean_text(text):
    text = demoji.replace(string=text) # 絵文字削除
    text = re.sub(r"@(\w+)", "", text) # @メンション削除
    text = re.sub(r"#(\w+)", "", text) # ハッシュタグ削除
    text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "" , text) # url削除
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    text = text.replace("\u3000", "")
    text = text.replace("\u2069", "")
    text = text.replace("\u2066", "")
    return text

def get_timeline():
    api = config.get_api()
    statuses = api.home_timeline()
    
    return statuses

def is_valid_tweet(tweet):
    text = clean_text(tweet.full_text)

    if 'みんなからの匿名質問を募集中！' in text:
        return text, False

    return text, True

def output_to_csv(all_list):
    with open("out.csv", "w") as file:
        for line in all_list:
            file.write(line)
            file.write("\n")
    return 

if __name__ == "__main__":
    run()