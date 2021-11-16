import tweepy
import config

def run():
    api = config.get_api()

    for tweet in tweepy.Cursor(api.search_tweets, q="スマブラ").items(10):
        if tweet.in_reply_to_user_id == None:
            continue
        print(tweet.text)
        print(tweet.id)
        print(tweet.user.id)

if __name__ == "__main__":
    run()