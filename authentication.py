import os
import tweepy

# All twitter tokens, provided when creating an app on the developer site
twitter_key = {
        'CONSUMER_KEY': os.environ['CONSUMER_KEY'],
        'CONSUMER_SECRET':os.environ['CONSUMER_SECRET'],
        'ACCESS_KEY':os.environ['ACCESS_KEY'],
        'ACCESS_SECRET':os.environ['ACCESS_SECRET']
        }

# Personal information, all accounts to which messages will be sent
user_ids = {
        'owner_twitter':os.environ['owner_twitter']
        }

auth = tweepy.OAuthHandler(twitter_key['CONSUMER_KEY'], twitter_key['CONSUMER_SECRET'])
auth.set_access_token(twitter_key['ACCESS_KEY'], twitter_key['ACCESS_SECRET'])
API = tweepy.API(auth)
