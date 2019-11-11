import json
import times
import tweepy
import message
import datetime
import authentication_h as auth

OwnerUser = auth.API.get_user(auth.user_ids['owner_twitter']).id
auth.API.send_direct_message(OwnerUser, "It's running on heroku")
# print("It's running on heroku")

while True:
    try:
        auth.API.get_user(auth.user_ids['owner_twitter']).id
    except tweepy.TweepError as TwitterError:
        error = json.loads(TwitterError.response.text)
        error_code = 'Twitter error: ' + error['errors'][0]['code']
        if int(error_code) == 226:
            times.sleep1(60*30)

    dispatch_time = times.time_to_send()
    k = 0
    while True:
        now_time = datetime.datetime.now().astimezone(times.local_timezone)
        followers_list = auth.API.followers_ids("@BotDaAgua")
        if now_time >= dispatch_time and times.pause(now_time):
            for i in range(len(followers_list)):
                try:
                    auth.API.send_direct_message(followers_list[i], message.message())
                    times.sleep1(2)
                    # print('Sent to: ', auth.API.get_user(followers_list[i]).screen_name, message.message())
                except tweepy.TweepError as TwitterError:
                    error = json.loads(TwitterError.response.text)
                    error_code = 'Twitter error: ' + error['errors'][0]['code']
                    if int(error_code) == 226:
                        print(error['errors'][0]['message'])
                        times.sleep1(60*30)
                    msg = 'Twitter error: ' + error['errors'][0]['message']
                    auth.API.send_direct_message(OwnerUser, msg)
                k += 1

            # auth.API.send_direct_message(OwnerUser, k)
            print("Sent to ", k, "users")
            break
        else:
            times.sleep1(60)

