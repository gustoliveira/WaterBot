import json
import times
import tweepy
import message
import authentication as auth

from datetime import datetime
from time import sleep

def error_message(message, text):
    error = json.loads(text)
    error_code = error['errors'][0]['code']
    # If occour a 226 or 88 error, "pause" for 28 minutes
    # 88 error: Rate limit exceeded
    if int(error_code) == 226 or int(error_code) == 88:
        sleep(60*28)
    error_msg = message + error['errors'][0]['message']
    print(error_msg)

OwnerUser = auth.API.get_user(auth.user_ids['owner_twitter']).id
auth.API.send_direct_message(OwnerUser, "It's alive")

while True:
    # Try get owner id, if occur 226 error, "pause" the script for 28 minutes
    # 226 error means the API thinks that it's a automated request
    try:
        auth.API.get_user(auth.user_ids['owner_twitter']).id
    except tweepy.TweepError as TwitterError:
        error = json.loads(TwitterError.response.text)
        error_code = error['errors'][0]['code']
        if int(error_code) == 226:
            sleep(60*28)

    dispatch_time = times.time_to_send()
    follower_index = 0
    while True:

        now_time = datetime.now().astimezone(times.local_timezone)

        if now_time >= dispatch_time and not times.is_paused(now_time):
            try:
                followers_list = auth.API.followers_ids("@BotDaAgua")
            except tweepy.TweepError as TwitterError:
                error_message('Não conseguiu lista de seguidores\nList_of_followers Twitter Error: ',
                                TwitterError.response.text)
                continue
            for i in range(len(followers_list)):
                try:
                    auth.API.send_direct_message(followers_list[i], message.message())
                    sleep(2)
                except tweepy.TweepError as TwitterError:
                    error_message('SendToUSer_Twitter_Error: ',
                                    TwitterError.response.text)

                follower_index += 1
            break

    sleep(60*5)
    OwnerUser = auth.API.get_user(auth.user_ids['owner_twitter']).id
