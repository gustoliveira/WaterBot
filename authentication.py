import os
import tweepy
import pyrebase

import os

# All twitter tokens, provided when creating an app on the developer site
twitter_key = {
        'CONSUMER_KEY': os.environ['CONSUMER_KEY'],
        'CONSUMER_SECRET':os.environ['CONSUMER_SECRET'],
        'ACCESS_KEY':os.environ['ACCESS_KEY'],
        'ACCESS_SECRET':os.environ['ACCESS_SECRET']
        }

# Personal information, all accounts to which messages will be sent
user_ids = {
        'owner_twitter':os.environ['owner_twitter'],
        'fb_email':os.environ['fb_email'], # firebase email registered
        'fb_password':os.environ['fb_password'] # firebase password registered
        }

# All firebase configuration and keys
firebaseConfig = {
        'apiKey': os.environ["apiKey"],
        'authDomain': os.environ["authDomain"],
        'databaseURL': os.environ["databaseURL"],
        'projectId': os.environ["projectId"],
        'storageBucket': os.environ["storageBucket"],
        'messagingSenderId': os.environ["messagingSenderId"],
        'appId': os.environ["appId"],
        'measurementId': os.environ["measurementId"]
        }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(user_ids['fb_email'], user_ids['fb_password'])
db = firebase.database()

auth = tweepy.OAuthHandler(twitter_key['CONSUMER_KEY'], twitter_key['CONSUMER_SECRET'])
auth.set_access_token(twitter_key['ACCESS_KEY'], twitter_key['ACCESS_SECRET'])
API = tweepy.API(auth)
