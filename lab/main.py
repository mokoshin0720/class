import tweepy
import config
import demoji
import re

def run():
    api = config.get_api()
    cnt = 0
    all_list = []

    q = "? -filter:retweets exclude:retweets lang:en"
    for tweet in tweepy.Cursor(api.search_tweets, q=q, result_type="mixed", tweet_mode='extended').items(100):
        conversation_list = []

        if is_valid_tweet(tweet) == False:
            continue

        text = clean_text(tweet.full_text)
        conversation_list.append(text)

        print(text)
        print(get_tweet_url(tweet))
        print("**********************")
        print("** New Conversation **")
        print("**********************")

        turn = 0
        context = []
        while tweet.in_reply_to_status_id != None:
            try:
                if tweet.lang != "en" or turn >= 5:
                    break
                turn += 1
                tweet = searcy_by_id(tweet.in_reply_to_status_id)
                text = clean_text(tweet.full_text)
                context.append(text)

            except Exception as e:
                break

            print(turn)
            print(text)
            print("====================")
        
        conversation_list.append(context)
        all_list.append(conversation_list)
    print(all_list)

def searcy_by_id(id):
    api = config.get_api()

    tweet = api.get_status(id=id, tweet_mode='extended')
    return tweet

def clean_text(text):
    text = demoji.replace(string=text) # 絵文字削除
    text = re.sub(r"@(\w+)", "", text) # @メンション削除
    text = re.sub(r"#(\w+)", "", text) # ハッシュタグ削除
    text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "" , text) # url削除
    return text

def is_valid_tweet(tweet):
    if tweet.in_reply_to_user_id == None:
        return False
    
    if tweet.metadata["iso_language_code"] != "en":
        return False

    return True

def get_tweet_url(tweet):
    user_id = tweet.user.id_str
    tweet_id = tweet.id_str
    url = "https://twitter.com/" + user_id + "/status/" + tweet_id
    return url

if __name__ == "__main__":
    run()