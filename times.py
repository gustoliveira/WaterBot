import time
import random
from pytz import timezone
from datetime import datetime, timedelta

local_timezone = timezone('America/Bahia')

def today():
    now_time = datetime.now()
    day = str(now_time.astimezone(local_timezone).day)
    month = str(now_time.astimezone(local_timezone).month)
    year = str(now_time.astimezone(local_timezone).year)
    return (year + '/' + month + '/' + day)

def pause(now_time):
    aux_ini = str(today() + ' 02:00')
    aux_fim = str(today() + ' 06:00')
    start_pause = datetime.strptime(aux_ini, '%Y/%m/%d %H:%M').astimezone(local_timezone)
    end_pause = datetime.strptime(aux_fim, '%Y/%m/%d %H:%M').astimezone(local_timezone)
    if now_time >= start_pause and now_time <= end_pause:
        time.sleep(60*5)
        return False
    else:
        return True

def time_to_send():
    delivery_time_ahead = datetime.now().astimezone(local_timezone) + timedelta(minutes=random.randrange(40, 50))
    delivery_str = datetime.strftime(delivery_time_ahead, '%Y/%m/%d %H:%M')
    return datetime.strptime(delivery_str, '%Y/%m/%d %H:%M').astimezone(local_timezone)
    # return datetime.now().astimezone(local_timezone)+timedelta(seconds=10) # For testing purpose

def sleep1(i):
    time.sleep(i)