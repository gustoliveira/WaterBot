import json
import times
import tweepy
import message
import datetime
import authentication as auth

from datetime import datetime
from time import sleep

def error_message(error):
    error_code = error['errors'][0]['code']
    # If occour a 226 or 88 error, "pause" for 28 minutes
    # 88 error: Rate limit exceeded
    if int(error_code) == 226 or int(error_code) == 88:
        print(error['errors'][0]['message'])
        sleep(60*30)
    msg = 'Twitter error: ' + error['errors'][0]['message']
    auth.API.send_direct_message(OwnerUser, msg)
    print(msg)


def main():
    OwnerUser = auth.API.get_user(auth.user_ids['owner_twitter']).id
    auth.API.send_direct_message(OwnerUser, "It's running on heroku")
    print("It's running on heroku")

    while True:
        # Try get owner id, if occur 226 error, "pause" the script for 28 minutes
        # 226 error means the API thinks that it's a automated request
        try:
            auth.API.get_user(auth.user_ids['owner_twitter']).id
        except tweepy.TweepError as TwitterError:
            error = json.loads(TwitterError.response.text)
            error_message(error)

        dispatch_time = times.time_to_send()
        follower_index = 0
        while True:
            now_time = datetime.now().astimezone(times.local_timezone)
            try:
                followers_list = auth.API.followers_ids("@BotDaAgua")
            except tweepy.TweepError as TwitterError:
                error = json.loads(TwitterError.response.text)
                error_message(error)

            if now_time >= dispatch_time and times.pause(now_time):
                for i in range(len(followers_list)):
                    try:
                        auth.API.send_direct_message(followers_list[i], message.message())
                        sleep(2)
                        # print('Sent to: ', auth.API.get_user(followers_list[i]).screen_name, message.message())
                    except tweepy.TweepError as TwitterError:
                        error = json.loads(TwitterError.response.text)
                        error_message(error)

                    follower_index += 1
                break
            else:
                sleep(60)

if __name__ == '__main__':
    main()
