import tweepy
import config
import demoji
import re

def run():
    api = config.get_api()
    cnt = 0
    tweet_list = []

    q = "? -filter:retweets exclude:retweets lang:en"
    for tweet in tweepy.Cursor(api.search_tweets, q=q, result_type="mixed", tweet_mode='extended').items(100):
        if is_valid_text(tweet) == False:
            continue
        text = clean_text(tweet.full_text)
        tweet_list.append(text)
        if tweet.in_reply_to_status_id != None:
            rep = searcy_by_id(tweet.in_reply_to_status_id)
            print(rep.full_text)
        cnt += 1

    print(cnt)
    for tweet in tweet_list:
        print(tweet)
        print("====================")

def searcy_by_id(id):
    api = config.get_api()

    tweet = api.get_status(id=id, tweet_mode='extended')
    return tweet

def clean_text(text):
    text = demoji.replace(string=text)
    text = re.sub(r"@(\w+)", "", text) # @メンション削除
    text = re.sub(r"#(\w+)", "", text) # ハッシュタグ削除
    text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "" , text) # url削除
    return text

def is_valid_text(tweet):
    if tweet.in_reply_to_user_id == None:
        return False
    
    if tweet.metadata["iso_language_code"] != "en":
        return False

    return True

if __name__ == "__main__":
    run()