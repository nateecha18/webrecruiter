from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# REST FRAMWORK IMPORT
from rest_framework.views import APIView
from rest_framework.response import Response
# END REST FRAMWORK IMPORT
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import admin, messages
from django.urls import path, reverse
from . import views

import json
from django.shortcuts import HttpResponse
from django.template import loader, RequestContext
from django.template import Context, Template
from django.template.loader import render_to_string

from account.models import Profile
from jobapply.models import CandidateBasic

from candidate_cart.extras import generate_order_id
from candidate_cart.models import OrderItem, Order
from request.models import Status,Comment,RequestType,RequestCandidate,RequestInterview,Request
from request.generate_id import generate_request_id
import datetime
from dateutil.relativedelta import *
import calendar
from rolepermissions.decorators import has_role_decorator
from rolepermissions.checkers import has_role
from django.utils import timezone
import pytz
from datetime import datetime, timedelta, time
from django.db.models import Q

# Create your views here.

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_profile = Profile.objects.filter(user=user).first()
        request_candidate_type = RequestType.objects.filter(request_type_id='1').first()
        request_interview_type = RequestType.objects.filter(request_type_id='2').first()
        status_close = Status.objects.filter(status_name='Closed').first()
        status_open = Status.objects.filter(status_name='Opened').first()


        candidate = CandidateBasic.objects.all()
        request_all = Request.objects.filter(owner=user_profile)
        if has_role(user, 'hr'):
            request_candidate = Request.objects.filter(request_type=request_candidate_type)
            request_candidate_open = Request.objects.filter(request_type=request_candidate_type,status=status_open)
            request_candidate_close = Request.objects.filter(request_type=request_candidate_type,status=status_close)
            request_interview = Request.objects.filter(request_type=request_interview_type)
            request_interview_open = Request.objects.filter(request_type=request_interview_type,status=status_open)
            request_interview_close = Request.objects.filter(request_type=request_interview_type,status=status_close)

        else:
            request_candidate = Request.objects.filter(owner=user_profile,request_type=request_candidate_type)
            request_candidate_open = Request.objects.filter(owner=user_profile,request_type=request_candidate_type,status=status_open)
            request_candidate_close = Request.objects.filter(owner=user_profile,request_type=request_candidate_type,status=status_close)
            request_interview = Request.objects.filter(owner=user_profile,request_type=request_interview_type)
            request_interview_open = Request.objects.filter(owner=user_profile,request_type=request_interview_type,status=status_open)
            request_interview_close = Request.objects.filter(owner=user_profile,request_type=request_interview_type,status=status_close)

        print(timezone.now())
        today = datetime.now()
        today_date = datetime.now().date()
        tomorrow = today_date + timedelta(1)
        today_start = datetime.combine(today_date, time())
        today_end = datetime.combine(tomorrow, time())

        print(today,"hhhh",today_date,"hhhh",tomorrow,"hhhh",today_start,"hhhh",today_end)
        candidate_today = CandidateBasic.objects.filter(date_apply__gt=today_date)
        print("++++++++++++++++++++",candidate_today)
        context = {
            'candidates' : candidate,
            'candidate_today' : candidate_today,
            'request_candidate' : request_candidate,
            'request_candidate_open' : request_candidate_open,
            'request_candidate_close' : request_candidate_close,
            'request_interview' : request_interview,
            'request_interview_open' : request_interview_open,
            'request_interview_close' : request_interview_close,

        }
        return render(request,"dashboard.html",context)

# class BackwardMonth(month_back):
#     date_months_ago = datetime.datetime.now() - relativedelta(months=month_back)
#     print(date_months_ago)
#     return date_months_ago.month ,date_months_ago.year


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        today = datetime.now()
        last_month = today.month - 12 if today.month>1 else 12
        last_month_year = today.year if today.month > last_month else today.year - 1
        print(last_month,last_month_year)

        month_label = []
        count_candidate_data = []
        for m in range(0, 6):
            date_months_ago = datetime.now() - relativedelta(months=m)
            months_ago = date_months_ago.month
            year_ago = date_months_ago.year
            month_label.insert(0,calendar.month_name[months_ago])
            candidate_count = CandidateBasic.objects.filter(date_apply__month=months_ago,date_apply__year=year_ago).count()
            count_candidate_data.insert(0,candidate_count)
            print ("Backward {0} month | Month {1} , Year {2}".format(m,months_ago,year_ago))
            print(month_label)
            print(count_candidate_data)

        labels = month_label
        default = count_candidate_data
        data = {
            "labels" : labels,
            "default" : default,
        }
        return Response(data)
