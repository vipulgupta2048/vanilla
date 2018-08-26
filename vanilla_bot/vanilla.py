import time
import tweepy

# Twitter Access Tokens
from config import *

# Connecting to twitter service
AUTH = tweepy.OAuthHandler(consumer_key, consumer_secret)
AUTH.set_access_token(access_token, access_token_secret)
API = tweepy.API(AUTH)

print("Finding Tweets with Vanilla \n")
while True:
    for searchterm in searchterms:
        for tweet in tweepy.Cursor(API.search, q=searchterm):
            tweet.retweet()
            tweet.favorite()
            print("retweeted")
            #time.sleep(15)
