# Importing libraies
import time
import tweepy
import re
import json

# Twitter Access Tokens
from config import *

# Connecting/Authenticating our module with Twitter API
AUTH = tweepy.OAuthHandler(consumer_key, consumer_secret)
AUTH.set_access_token(access_token, access_token_secret)
API = tweepy.API(AUTH)

for searchterm in searchterms:
    for tweet in tweepy.Cursor(API.search, q = searchterm).items(0):
        print(tweet)
        break


#~ a = API.user_timeline(["vipulgupta2048",1])
#print(a)





# Magic Begins here
#~ print("Finding Tweets with Vanilla \n")
#~ while True:
    #~ for searchterm in searchterms:

        #~  #~ print(tweet.id)
            #~ print("retweeted")
