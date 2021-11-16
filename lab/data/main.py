import tweepy
import config
import demoji
import re

def run():
    api = config.get_api()
    q = "? -filter:retweets exclude:retweets"
    cnt = 0

    for tweet in tweepy.Cursor(api.search_tweets, q=q, result_type="mixed").items(100):
        if is_valid_text(tweet) == False:
            continue
        print(tweet.text)
        print(tweet.in_reply_to_user_id)

        text = clean_text(tweet.text)
        print(text)
        print("======================")
        cnt += 1
    print(cnt)

def clean_text(text):
    text = demoji.replace(string=text)
    text = text.replace("@", "to")
    text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "" , text)
    return text

def is_valid_text(tweet):
    if tweet.in_reply_to_user_id == None:
        return False
    
    text = tweet.text.replace("@", "to")
    p = re.compile(r'^[a-zA-Z0-9\?!\$&\-(),…\.\'# ]+$')
    if p.fullmatch(text) == None:
        return False
    return True

if __name__ == "__main__":
    run()