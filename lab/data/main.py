import tweepy
import config
import demoji
import re

def run():
    api = config.get_api()

    for tweet in tweepy.Cursor(api.search_tweets, q="a -filter:retweets").items(10):
        # if tweet.in_reply_to_user_id == None:
        #     continue
        print(tweet.text)

        text = clean_text(tweet.text)
        print(text)
        print(check_text(text))
        print("======================")

def clean_text(text):
    text = demoji.replace(string=text)
    text = text.replace("@", "to")
    text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "" , text)
    return text

def check_text(text):
    p = re.compile(r'^[a-zA-Z0-9\?!\$&\-(),…\.\' ]+$')
    return p.fullmatch(text)

if __name__ == "__main__":
    run()