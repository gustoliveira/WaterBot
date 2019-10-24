import os
import tweepy
import pyrebase

# All twitter tokens, provided when creating an app on the developer site
twitter_key = {
        'CONSUMER_KEY':os.getenv('CONSUMER_KEY', 'Token Not found'),
        'CONSUMER_SECRET':os.getenv('CONSUMER_SECRET','Token Not found'),
        'ACCESS_KEY':os.getenv('ACCESS_KEY', 'Token Not found'),
        'ACCESS_SECRET':os.getenv('ACCESS_SECRET', 'Token Not found')
        }

# Personal information, all accounts to which messages will be sent
user_ids = {
        'owner_twitter': os.getenv('@gvst_oliveira', 'Token Not found'), # Enter your twitter user_name. Ex: @Twitter
        'fb_email':os.getenv('fb_email', 'Token Not found'), # firebase email registered
        'fb_password':os.getenv('fb_password', 'Token Not found') # firebase password registered
        }

# All firebase configuration and keys
firebaseConfig = {
        'apiKey':os.getenv('apiKey', 'Token Not found'),
        'authDomain':os.getenv('authDomain', 'Token Not found'),
        'databaseURL':os.getenv('databaseURL', 'Token Not found'),
        'projectId':os.getenv('projectId', 'Token Not found'),
        'storageBucket':os.getenv('storageBucket', 'Token Not found'),
        'messagingSenderId':os.getenv('messagingSenderId', 'Token Not found'),
        'appId':os.getenv('appId', 'Token Not found'),
        'measurementId':os.getenv('measurementId', 'Token Not found'),
        }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(user_ids['fb_email'], user_ids['fb_password'])
db = firebase.database()

auth = tweepy.OAuthHandler(twitter_key['CONSUMER_KEY'], twitter_key['CONSUMER_SECRET'])
auth.set_access_token(twitter_key['ACCESS_KEY'], twitter_key['ACCESS_SECRET'])
API = tweepy.API(auth)



# https://stackoverflow.com/questions/51227159/how-do-i-set-environment-variables-in-pipenv