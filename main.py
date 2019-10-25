import json
import times
import tweepy
import message
import datetime
# import authentication_h as auth
import authentication as auth # For testing purpose

followers_list = auth.API.followers_ids("@BotDaAgua")

now_time = datetime.datetime.now().astimezone(times.local_timezone)

first_time_flag = True

while times.until(now_time):
    if first_time_flag == True:
        auth.API.send_direct_message(auth.API.get_user(auth.user_ids['owner_twitter']).id, "It's running on heroku")
        print("It's running on heroku")
        first_time_flag = False

    dispatch_time = times.time_to_send()
    while True:
        now_time = datetime.datetime.now().astimezone(times.local_timezone)
        j = 0
        if now_time >= dispatch_time and times.pause(now_time):
            for i in range(len(followers_list)):
                try:
                    auth.API.get_user(followers_list[i]).id
                    auth.API.send_direct_message(auth.API.get_user(followers_list[i]).id, message.message())
                except tweepy.TweepError as TwitterError:
                    error = json.loads(TwitterError.response.text)
                    error_msg = 'Twitter error: ' + error['errors'][0]['message']
                    auth.API.send_direct_message(auth.user_ids['owner_twitter'], error_msg)
                j+=1

            print("Sent for: ", j)
            if j < len(followers_list):
                auth.API.send_direct_message(auth.API.get_user(auth.user_ids['owner_twitter']).id, "Can't sent for all followers, pls check")
            break
        else:
            # print(dispatch_time-now_time) # For testing purpose
            times.sleep1(60)
