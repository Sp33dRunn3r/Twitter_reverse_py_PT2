# TWITTER BOT PROJECT:
import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

#Alternative Bot
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        #tweet.retweet()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
