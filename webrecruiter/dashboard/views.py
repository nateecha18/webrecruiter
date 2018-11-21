from django.shortcuts import render, redirect, get_object_or_404
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
from tor.models import ProjectType,ProjectLevel,PositionProject,Tor,PositionField,Project,PositionAll

# Create your views here.

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
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

        else:
            return redirect('login')

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

class ChartPositionReq(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        today = datetime.now()
        last_month = today.month - 12 if today.month>1 else 12
        last_month_year = today.year if today.month > last_month else today.year - 1
        print(last_month,last_month_year)

        month_label = []
        count_administrator_req_list = []
        count_account_manager_req_list = []
        count_certified_instructor_req_list = []
        count_internship_req_list = []
        count_marketing_product_req_list = []
        count_network_engineer_req_list = []
        count_network_dev_req_list = []
        count_outsourcing_req_list = []
        count_presale_req_list = []
        count_professional_engineer_req_list = []
        count_project_finance_manager_req_list = []
        count_project_manager_req_list = []
        count_si_engineer_req_list = []
        count_technical_consult_engineer_req_list = []

        amount_administrator_req_list = []
        amount_account_manager_req_list = []
        amount_certified_instructor_req_list = []
        amount_internship_req_list = []
        amount_marketing_product_req_list = []
        amount_network_engineer_req_list = []
        amount_network_dev_req_list = []
        amount_outsourcing_req_list = []
        amount_presale_req_list = []
        amount_professional_engineer_req_list = []
        amount_project_finance_manager_req_list = []
        amount_project_manager_req_list = []
        amount_si_engineer_req_list = []
        amount_technical_consult_engineer_req_list = []

        for m in range(0, 6):
            date_months_ago = datetime.now() - relativedelta(months=m)
            months_ago = date_months_ago.month
            year_ago = date_months_ago.year
            month_label.insert(0,calendar.month_name[months_ago])
            # Request ประเภท Request Candidate
            candidate_request_type = RequestType.objects.filter(request_type_id='1').first()
            # ตำแหน่งงานตำแหน่งต่างๆ
            administrator = PositionAll.objects.filter(position_name='Administrator').first()
            account_manager = PositionAll.objects.filter(position_name='Account Manager').first()
            certified_instructor = PositionAll.objects.filter(position_name='Certified Instructor').first()
            internship = PositionAll.objects.filter(position_name='Internship').first()
            marketing_product = PositionAll.objects.filter(position_name='Marketing Product').first()
            network_engineer = PositionAll.objects.filter(position_name='Network Engineer').first()
            network_dev = PositionAll.objects.filter(position_name='Network Programmability Developer Specialist').first()
            outsourcing = PositionAll.objects.filter(position_name='Outsourcing Engineer').first()
            presale = PositionAll.objects.filter(position_name='Presale').first()
            professional_engineer = PositionAll.objects.filter(position_name='Professional Engineer').first()
            # ยังไม่ได้เอาเข้ากราฟ
            project_finance_manager = PositionAll.objects.filter(position_name='Project Finance Manager').first()
            project_manager = PositionAll.objects.filter(position_name='Project Manager').first()
            si_engineer = PositionAll.objects.filter(position_name='System Integration Engineer').first()
            technical_consult_engineer = PositionAll.objects.filter(position_name='Technical Consultant Engineer - Services').first()

                # เพิ่มตำแหน่งงานอื่นๆ
            administrator_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=administrator,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            administrator_amount = 0
            if administrator_req:
                for req in administrator_req:
                    administrator_amount += req.request_candidate.diff_empty_amount()
            amount_administrator_req_list.insert(0,administrator_amount)
            count_administrator_req_list.insert(0,administrator_req.count())

            account_manager_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=account_manager,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            account_manager_amount = 0
            if account_manager_req:
                for req in account_manager_req:
                    account_manager_amount += req.request_candidate.diff_empty_amount()
            amount_account_manager_req_list.insert(0,account_manager_amount)
            count_account_manager_req_list.insert(0,account_manager_req.count())

            certified_instructor_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=certified_instructor,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            certified_instructor_amount = 0
            if certified_instructor_req:
                for req in certified_instructor_req:
                    certified_instructor_amount += req.request_candidate.diff_empty_amount()
            amount_certified_instructor_req_list.insert(0,certified_instructor_amount)
            count_certified_instructor_req_list.insert(0,certified_instructor_req.count())

            internship_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=internship,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            internship_amount = 0
            if internship_req:
                for req in internship_req:
                    internship_amount += req.request_candidate.diff_empty_amount()
            amount_internship_req_list.insert(0,internship_amount)
            count_internship_req_list.insert(0,internship_req.count())

            marketing_product_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=marketing_product,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            marketing_product_amount = 0
            if marketing_product_req:
                for req in marketing_product_req:
                    marketing_product_amount += req.request_candidate.diff_empty_amount()
            amount_marketing_product_req_list.insert(0,marketing_product_amount)
            count_marketing_product_req_list.insert(0,marketing_product_req.count())

            network_engineer_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=network_engineer,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            network_engineer_amount = 0
            if network_engineer_req:
                for req in network_engineer_req:
                    network_engineer_amount += req.request_candidate.diff_empty_amount()
            amount_network_engineer_req_list.insert(0,network_engineer_amount)
            count_network_engineer_req_list.insert(0,network_engineer_req.count())

            network_dev_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=network_dev,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            network_dev_amount = 0
            if network_dev_req:
                for req in network_dev_req:
                    network_dev_amount += req.request_candidate.diff_empty_amount()
            amount_network_dev_req_list.insert(0,network_dev_amount)
            count_network_dev_req_list.insert(0,network_dev_req.count())

            outsourcing_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=outsourcing,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            outsourcing_amount = 0
            if outsourcing_req:
                for req in outsourcing_req:
                    outsourcing_amount += req.request_candidate.diff_empty_amount()
            amount_outsourcing_req_list.insert(0,outsourcing_amount)
            count_outsourcing_req_list.insert(0,outsourcing_req.count())

            presale_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=presale,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            presale_amount = 0
            if presale_req:
                for req in presale_req:
                    presale_amount += req.request_candidate.diff_empty_amount()
            amount_presale_req_list.insert(0,presale_amount)
            count_presale_req_list.insert(0,presale_req.count())

            professional_engineer_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=professional_engineer,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            professional_engineer_amount = 0
            if professional_engineer_req:
                for req in professional_engineer_req:
                    professional_engineer_amount += req.request_candidate.diff_empty_amount()
            amount_professional_engineer_req_list.insert(0,professional_engineer_amount)
            count_professional_engineer_req_list.insert(0,professional_engineer_req.count())

            project_finance_manager_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=project_finance_manager,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            project_finance_manager_amount = 0
            if project_finance_manager_req:
                for req in project_finance_manager_req:
                    project_finance_manager_amount += req.request_candidate.diff_empty_amount()
            amount_project_finance_manager_req_list.insert(0,project_finance_manager_amount)
            count_project_finance_manager_req_list.insert(0,project_finance_manager_req.count())

            project_manager_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=project_manager,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            project_manager_amount = 0
            if project_manager_req:
                for req in project_manager_req:
                    project_manager_amount += req.request_candidate.diff_empty_amount()
            amount_project_manager_req_list.insert(0,project_manager_amount)
            count_project_manager_req_list.insert(0,project_manager_req.count())

            si_engineer_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=si_engineer,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            si_engineer_amount = 0
            if si_engineer_req:
                for req in si_engineer_req:
                    si_engineer_amount += req.request_candidate.diff_empty_amount()
            amount_si_engineer_req_list.insert(0,si_engineer_amount)
            count_si_engineer_req_list.insert(0,si_engineer_req.count())

            technical_consult_engineer_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=technical_consult_engineer,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago)
            technical_consult_engineer_amount = 0
            if technical_consult_engineer_req:
                for req in technical_consult_engineer_req:
                    technical_consult_engineer_amount += req.request_candidate.diff_empty_amount()
            amount_technical_consult_engineer_req_list.insert(0,technical_consult_engineer_amount)
            count_technical_consult_engineer_req_list.insert(0,technical_consult_engineer_req.count())


        labels = month_label
        count_administrator = count_administrator_req_list
        count_account_manager = count_account_manager_req_list
        count_certified_instructor = count_certified_instructor_req_list
        count_internship = count_internship_req_list
        count_marketing_product = count_marketing_product_req_list
        count_network_engineer = count_network_engineer_req_list
        count_network_dev = count_network_dev_req_list
        count_outsourcing = count_outsourcing_req_list
        count_presale = count_presale_req_list
        count_professional_engineer = count_professional_engineer_req_list
        count_project_finance_manager = count_project_finance_manager_req_list
        count_project_manager = count_project_manager_req_list
        count_si_engineer = count_si_engineer_req_list
        count_technical_consult_engineer = count_technical_consult_engineer_req_list
        # List จำนวนพนักงานที่ขาดในแต่ละเดือน
        amount_administrator = amount_administrator_req_list
        amount_account_manager = amount_account_manager_req_list
        amount_certified_instructor = amount_certified_instructor_req_list
        amount_internship = amount_internship_req_list
        amount_marketing_product = amount_marketing_product_req_list
        amount_network_engineer = amount_network_engineer_req_list
        amount_network_dev = amount_network_dev_req_list
        amount_outsourcing = amount_outsourcing_req_list
        amount_presale = amount_presale_req_list
        amount_professional_engineer = amount_professional_engineer_req_list
        amount_project_finance_manager = amount_project_finance_manager_req_list
        amount_project_manager = amount_project_manager_req_list
        amount_si_engineer = amount_si_engineer_req_list
        amount_technical_consult_engineer = amount_technical_consult_engineer_req_list
        data = {
            "labels" : labels,
            "count_administrator" : count_administrator,
            "count_account_manager" : count_account_manager,
            "count_certified_instructor" : count_certified_instructor,
            "count_internship" : count_internship,
            "count_marketing_product" : count_marketing_product,
            "count_network_engineer" : count_network_engineer,
            "count_network_dev" : count_network_dev,
            "count_outsourcing" : count_outsourcing,
            "count_presale" : count_presale,
            "count_professional_engineer" : count_professional_engineer,
            "count_project_finance_manager" : count_project_finance_manager,
            "count_project_manager" : count_project_manager,
            "count_si_engineer" : count_si_engineer,
            "count_technical_consult_engineer" : count_technical_consult_engineer,

            "amount_administrator" : amount_administrator,
            "amount_account_manager" : amount_account_manager,
            "amount_certified_instructor" : amount_certified_instructor,
            "amount_internship" : amount_internship,
            "amount_marketing_product" : amount_marketing_product,
            "amount_network_engineer" : amount_network_engineer,
            "amount_network_dev" : amount_network_dev,
            "amount_outsourcing" : amount_outsourcing,
            "amount_presale" : amount_presale,
            "amount_professional_engineer" : amount_professional_engineer,
            "amount_project_finance_manager" : amount_project_finance_manager,
            "amount_project_manager" : amount_project_manager,
            "amount_si_engineer" : amount_si_engineer,
            "amount_technical_consult_engineer" : amount_technical_consult_engineer,
        }
        return Response(data)

class ChartPositionReqAmount(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        today = datetime.now()
        last_month = today.month - 12 if today.month>1 else 12
        last_month_year = today.year if today.month > last_month else today.year - 1
        print(last_month,last_month_year)

        month_label = []
        count_administrator_req_list = []
        count_account_manager_req_list = []
        count_certified_instructor_req_list = []
        count_internship_req_list = []
        count_marketing_product_req_list = []
        count_network_engineer_req_list = []
        count_network_dev_req_list = []
        count_outsourcing_req_list = []
        count_presale_req_list = []
        count_professional_engineer_req_list = []
        count_project_finance_manager_req_list = []
        count_project_manager_req_list = []
        count_si_engineer_req_list = []
        count_technical_consult_engineer_req_list = []

        print("EHEREEEESTART!!!")
        for m in range(0, 6):
            print("2/รอบที่",m)
            date_months_ago = datetime.now() - relativedelta(months=m)
            months_ago = date_months_ago.month
            year_ago = date_months_ago.year
            month_label.insert(0,calendar.month_name[months_ago])
            # Request ประเภท Request Candidate
            candidate_request_type = RequestType.objects.filter(request_type_id='1').first()
            # ตำแหน่งงานตำแหน่งต่างๆ
            administrator = PositionAll.objects.filter(position_name='Administrator').first()
            account_manager = PositionAll.objects.filter(position_name='Account Manager').first()
            certified_instructor = PositionAll.objects.filter(position_name='Certified Instructor').first()
            internship = PositionAll.objects.filter(position_name='Internship').first()
            marketing_product = PositionAll.objects.filter(position_name='Marketing Product').first()
            network_engineer = PositionAll.objects.filter(position_name='Network Engineer').first()
            network_dev = PositionAll.objects.filter(position_name='Network Programmability Developer Specialist').first()
            outsourcing = PositionAll.objects.filter(position_name='Outsourcing Engineer').first()
            presale = PositionAll.objects.filter(position_name='Presale').first()
            professional_engineer = PositionAll.objects.filter(position_name='Professional Engineer').first()
            # ยังไม่ได้เอาเข้ากราฟ
            project_finance_manager = PositionAll.objects.filter(position_name='Project Finance Manager').first()
            project_manager = PositionAll.objects.filter(position_name='Project Manager').first()
            si_engineer = PositionAll.objects.filter(position_name='System Integration Engineer').first()
            technical_consult_engineer = PositionAll.objects.filter(position_name='Technical Consultant Engineer - Services').first()

                # เพิ่มตำแหน่งงานอื่นๆ
            count_administrator_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=administrator,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_administrator_req_list.insert(0,count_administrator_req)

            count_account_manager_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=account_manager,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_account_manager_req_list.insert(0,count_account_manager_req)

            count_certified_instructor_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=certified_instructor,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_certified_instructor_req_list.insert(0,count_certified_instructor_req)

            count_internship_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=internship,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_internship_req_list.insert(0,count_internship_req)

            count_marketing_product_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=marketing_product,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_marketing_product_req_list.insert(0,count_marketing_product_req)

            count_network_engineer_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=network_engineer,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_network_engineer_req_list.insert(0,count_network_engineer_req)

            count_network_dev_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=network_dev,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_network_dev_req_list.insert(0,count_network_dev_req)

            count_outsourcing_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=outsourcing,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_outsourcing_req_list.insert(0,count_outsourcing_req)

            count_presale_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=presale,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_presale_req_list.insert(0,count_presale_req)

            count_professional_engineer_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=professional_engineer,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_professional_engineer_req_list.insert(0,count_professional_engineer_req)

            count_project_finance_manager_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=project_finance_manager,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_project_finance_manager_req_list.insert(0,count_project_finance_manager_req)

            count_project_manager_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=project_manager,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_project_manager_req_list.insert(0,count_project_manager_req)

            count_si_engineer_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=si_engineer,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_si_engineer_req_list.insert(0,count_si_engineer_req)

            count_technical_consult_engineer_req = Request.objects.filter(request_type=candidate_request_type,request_candidate__position__position_name=technical_consult_engineer,datetime_add_request__month=months_ago,datetime_add_request__year=year_ago).count()
            count_technical_consult_engineer_req_list.insert(0,count_technical_consult_engineer_req)


        labels = month_label
        count_administrator = count_administrator_req_list
        count_account_manager = count_account_manager_req_list
        count_certified_instructor = count_certified_instructor_req_list
        count_internship = count_internship_req_list
        count_marketing_product = count_marketing_product_req_list
        count_network_engineer = count_network_engineer_req_list
        count_network_dev = count_network_dev_req_list
        count_outsourcing = count_outsourcing_req_list
        count_presale = count_presale_req_list
        count_professional_engineer = count_professional_engineer_req_list
        count_project_finance_manager = count_project_finance_manager_req_list
        count_project_manager = count_project_manager_req_list
        count_si_engineer = count_si_engineer_req_list
        count_technical_consult_engineer = count_technical_consult_engineer_req_list
        data = {
            "labels" : labels,
            "count_administrator" : count_administrator,
            "count_account_manager" : count_account_manager,
            "count_certified_instructor" : count_certified_instructor,
            "count_internship" : count_internship,
            "count_marketing_product" : count_marketing_product,
            "count_network_engineer" : count_network_engineer,
            "count_network_dev" : count_network_dev,
            "count_outsourcing" : count_outsourcing,
            "count_presale" : count_presale,
            "count_professional_engineer" : count_professional_engineer,
            "count_project_finance_manager" : count_project_finance_manager,
            "count_project_manager" : count_project_manager,
            "count_si_engineer" : count_si_engineer,
            "count_technical_consult_engineer" : count_technical_consult_engineer,
        }
        return Response(data)
