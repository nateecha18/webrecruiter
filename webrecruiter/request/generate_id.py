import random
import string
from datetime import date
import datetime

from request.models import RequestCandidate

def generate_request_id():
    amount_request_today = RequestCandidate.objects.filter(date_request__gte=datetime.date.today()).count()+1
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return 'RQ{0}{1}-{2}'.format(date_str, rand_str,amount_request_today)
