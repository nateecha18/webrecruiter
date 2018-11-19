import random
import string
from datetime import date
import datetime

from request.models import RequestCandidate,RequestInterview,Request

def generate_request_id():
    amount_request_today = Request.objects.filter(datetime_add_request__gte=datetime.date.today()).count()+1
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return 'RQ{0}{1}-{2}'.format(date_str, rand_str,amount_request_today)

def generate_comment_id(request_id):
    selected_request = Request.objects.filter(request_id=request_id).first()
    print(selected_request)
    amount_comment = (selected_request.comment.count())+1
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    print('{0}CM{1}-{2}'.format(request_id, rand_str,amount_comment))
    return '{0}CM{1}-{2}'.format(request_id, rand_str,amount_comment)
