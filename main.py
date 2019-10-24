import json
import times
import tweepy
import message
import datetime
import authentication as auth

followers_list = auth.API.followers_ids("@BotDaAgua")

now_time = datetime.datetime.now().astimezone(times.local_timezone)
print(len(followers_list))
while times.until(now_time):
    dispatch_time = times.time_to_send()
    while True:
        now_time = datetime.datetime.now().astimezone(times.local_timezone)
        if now_time >= dispatch_time and times.pause(now_time):
        # if now_time >= dispatch_time: # and times.pause(now_time):
            for i in range(len(followers_list)):
                try:
                    # auth.API.send_direct_message(followers_list[i], message.message())
                    print("Sent")
                except tweepy.TweepError as TwitterError:
                    error = json.loads(TwitterError.response.text)
                    error_msg = 'Twitter error: ' + error['errors'][0]['message']
                    # auth.API.send_direct_message(auth.user_ids['owner_twitter'], error_msg)
            break
        else:
            # print(dispatch_time-now_time) # For testing purpose
            times.sleep1(60)
