import json
import times
import tweepy
import message
import authentication as auth

from datetime import datetime
from time import sleep

import os
os.environ["apiKey"] = 'AIzaSyDRT0Bx9ro-IVv-w3xmMj7CaOqgZ1IM8jM'
os.environ["authDomain"] = 'rememberbot-f5d7b.firebaseapp.com'
os.environ["databaseURL"] = 'https://rememberbot-f5d7b.firebaseio.com'
os.environ["projectId"] = 'rememberbot-f5d7b'
os.environ["storageBucket"] = 'rememberbot-f5d7b.appspot.com'
os.environ["messagingSenderId"] = '502104489587'
os.environ["appId"] = '1:502104489587:web:bd9e8a851cb9baaa77b406'
os.environ["measurementId"] = 'G-8Q89DBCG4T'

os.environ['fb_email'] = "gustoliveira.projetos@gmail.com"
os.environ['fb_password'] = "mamabuseta"
os.environ['owner_twitter'] = "@gvst_oliveira"

os.environ['CONSUMER_KEY'] = "JfbzuNBurIGSQBLqOrQ3lhGZJ"
os.environ['CONSUMER_SECRET'] = "TSHFSmf9z6cf8Qhuujln88sg4MBgx3MGRX8EruSWnm2dhviMko"
os.environ['ACCESS_KEY'] = "1159671170721046528-N4hn4QLKT5UENQhpMUhikZ83F3S6Ve"
os.environ['ACCESS_SECRET'] = "6aAP7EeqNPVZSSNpnBCcDhKp91uVr1gvAUAGqYQdzdx6y"

def error_message(message, text):
    print("Entrou em error_message função")
    error = json.loads(text)
    error_code = error['errors'][0]['code']
    # If occour a 226 or 88 error, "pause" for 28 minutes
    # 88 error: Rate limit exceeded
    if int(error_code) == 226 or int(error_code) == 88:
        print(error['errors'][0]['message'])
    error_msg = message + error['errors'][0]['message']
    print(error_msg)
    sleep(60*28)

print("Entrou em main")
OwnerUser = auth.API.get_user(auth.user_ids['owner_twitter']).id
auth.API.send_direct_message(OwnerUser, "It's alive")

while True:
    print("Entrou primeiro true")
    # Try get owner id, if occur 226 error, "pause" the script for 28 minutes
    # 226 error means the API thinks that it's a automated request
    try:
        auth.API.get_user(auth.user_ids['owner_twitter']).id
        print("Conseguiu pegar id")
    except tweepy.TweepError as TwitterError:
        print("Não conseguiu pegar id")
        error = json.loads(TwitterError.response.text)
        error_code = error['errors'][0]['code']
        if int(error_code) == 226:
            sleep(60*28)

    dispatch_time = times.time_to_send()
    follower_index = 0
    while True:
        print("Entrou segundo true")

        now_time = datetime.now().astimezone(times.local_timezone)

        if now_time >= dispatch_time and not times.is_paused(now_time):
            print("Entrou no if do segundo true")
            try:
                followers_list = auth.API.followers_ids("@BotDaAgua")
                print("Conseguiu lista de seguidores")
            except tweepy.TweepError as TwitterError:
                error_message('Não conseguiu lista de seguidores\nList_of_followers Twitter Error: ',
                                TwitterError.response.text)
                continue
            print("É hora de enviar crianças")
            for i in range(len(followers_list)):
                try:
                    auth.API.send_direct_message(followers_list[i], message.message())
                    print("Sent ", follower_index)
                    sleep(2)
                except tweepy.TweepError as TwitterError:
                    error_message('SendToUSer_Twitter_Error: ',
                                    TwitterError.response.text)

                follower_index += 1
            print("Enviou pra geral")
            break

    sleep(60*5)
    OwnerUser = auth.API.get_user(auth.user_ids['owner_twitter']).id
