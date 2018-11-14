from request.models import Status,Comment,RequestCandidate
import datetime
from datetime import datetime,date,time,timedelta, timezone
import pytz
import math

def compare_request_now_time(datetime_action):

    tz = pytz.timezone('Asia/Bangkok')
    delta = datetime.now(tz=tz) - datetime_action
    sec = timedelta(seconds=delta.seconds)
    time = datetime(1,1,1) + sec
    if (time.day-1) == 0:
        day_rq = ''
    else:
        day_rq = time.day-1
    if (time.hour) == 0:
        hour_rq = ''
    else:
        hour_rq = time.hour
    if (time.minute) == 0:
        min_rq = ''
    else:
        min_rq = time.minute

    print("DAYS:HOURS:MIN:SEC")
    print("%d:%d:%d:%d" % (time.day-1, time.hour, time.minute, time.second))
    print(datetime_action)

    return day_rq,hour_rq,min_rq
