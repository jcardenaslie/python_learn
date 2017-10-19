import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    
    try:
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        acces_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_secret = os.environ['TWITTER_ACCESS_SECRET']
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set")
        sys.exit(1)
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(acces_token, acces_secret)

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client