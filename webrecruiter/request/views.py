from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View
from account.models import Profile
from rank.models import CandidateRank
from jobapply.models import CandidateBasic
from candidate_cart.models import OrderItem, Order, InterviewStatus, InterviewStatusLog
from rolepermissions.decorators import has_role_decorator
from rolepermissions.checkers import has_role
from request.models import Status,ProjectType,LevelRequest,Comment,RequestType,RequestCandidate,RequestInterview,Request,Position
from request.generate_id import generate_request_id
from request.generate_id import generate_comment_id
from request.compare_time import compare_request_now_time
import datetime
from datetime import datetime,date,time,timedelta, timezone
import pytz
import math
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib.auth.models import User


def get_cart_amount(request):
    user = User.objects.filter(username=request.user.username)

    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    cart_amount = 0
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        cart_amount = user_order_items.count()
    return cart_amount

def get_open_request(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(~Q(status_id='3'))
        open_request = Request.objects.filter(~Q(status_id='3')).count()
        close_request = Request.objects.filter(status_id='3').count()

    else:
        request_all = Request.objects.filter(Q(owner=user_profile),~Q(status_id='3'))
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id='3')).count()
        close_request = Request.objects.filter(owner=user_profile,status_id='3').count()
    return request_all,open_request,close_request

def get_close_request(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(status_id='3')
        open_request = Request.objects.filter(~Q(status_id='3')).count()
        close_request = Request.objects.filter(status_id='3').count()

    else:
        request_all = Request.objects.filter(owner=user_profile,status_id='3')
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id='3')).count()
        close_request = Request.objects.filter(owner=user_profile,status_id='3').count()
    return request_all,open_request,close_request

def get_close_request_interview(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(status_id='3',request_type='2')
        open_request = Request.objects.filter(~Q(status_id='3'),Q(request_type='2')).count()
        close_request = Request.objects.filter(status_id='3',request_type='2').count()

    else:
        request_all = Request.objects.filter(owner=user_profile,status_id='3',request_type='2')
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id='3'),Q(request_type='2')).count()
        close_request = Request.objects.filter(owner=user_profile,status_id='3',request_type='2').count()
    return request_all,open_request,close_request

def get_open_request_interview(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(~Q(status_id='3'),Q(request_type='2'))
        open_request = Request.objects.filter(~Q(status_id='3'),Q(request_type='2')).count()
        close_request = Request.objects.filter(status_id='3',request_type='2').count()

    else:
        request_all = Request.objects.filter(Q(owner=user_profile),~Q(status_id='3'),Q(request_type='2'))
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id='3'),Q(request_type='2')).count()
        close_request = Request.objects.filter(owner=user_profile,status_id='3',request_type='2').count()
    return request_all,open_request,close_request

def get_close_request_candidate(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(status_id='3',request_type='1')
        open_request = Request.objects.filter(~Q(status_id='3'),Q(request_type='1')).count()
        close_request = Request.objects.filter(status_id='3',request_type='1').count()

    else:
        request_all = Request.objects.filter(owner=user_profile,status_id='3',request_type='1')
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id='3'),Q(request_type='1')).count()
        close_request = Request.objects.filter(owner=user_profile,status_id='3',request_type='1').count()
    return request_all,open_request,close_request

def get_open_request_candidate(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(~Q(status_id='3'),Q(request_type='1'))
        open_request = Request.objects.filter(~Q(status_id='3'),Q(request_type='1')).count()
        close_request = Request.objects.filter(status_id='3',request_type='1').count()

    else:
        request_all = Request.objects.filter(Q(owner=user_profile),~Q(status_id='3'),Q(request_type='1'))
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id='3'),Q(request_type='1')).count()
        close_request = Request.objects.filter(owner=user_profile,status_id='3',request_type='1').count()
    return request_all,open_request,close_request

# ______________________________________________________________________________________________________________________________________________

def index(request):
    request_all,open_request,close_request = get_open_request(request)
    cart_amount = get_cart_amount(request)
    context = {
        'All_requests' : request_all,
        'Open_request_amount' : open_request,
        'Close_request_amount' : close_request,
        'Cart_amount':cart_amount,
    }
    template = loader.get_template("request.html")
    return HttpResponse(template.render(context, request))

def request_interview(request):
    request_all,open_request,close_request = get_open_request_interview(request)
    cart_amount = get_cart_amount(request)
    context = {
        'All_requests' : request_all,
        'Open_request_amount' : open_request,
        'Close_request_amount' : close_request,
        'Cart_amount':cart_amount,
    }
    template = loader.get_template("request_interview.html")
    return HttpResponse(template.render(context, request))

def request_candidate(request):
    request_all,open_request,close_request = get_open_request_candidate(request)
    cart_amount = get_cart_amount(request)
    context = {
        'All_requests' : request_all,
        'Open_request_amount' : open_request,
        'Close_request_amount' : close_request,
        'Cart_amount':cart_amount,
    }
    template = loader.get_template("request_candidate.html")
    return HttpResponse(template.render(context, request))

def show_close_request(request):
    if request.method == 'GET':
        request_all,open_request,close_request = get_close_request(request)
        html = render_to_string('request_table.html' , {
                                                        'All_requests' : request_all,
                                                        'Open_request_amount' : open_request,
                                                        'Close_request_amount' : close_request,
                                                        },request=request)
    return JsonResponse({'html' : html})

def show_open_request(request):
    if request.method == 'GET':
        request_all,open_request,close_request = get_open_request(request)
        html = render_to_string('request_table.html' , {
                                                        'All_requests' : request_all,
                                                        'Open_request_amount' : open_request,
                                                        'Close_request_amount' : close_request,
                                                        },request=request)
    return JsonResponse({'html' : html})

def show_close_request_interview(request):
    if request.method == 'GET':
        request_all,open_request,close_request = get_close_request_interview(request)
        html = render_to_string('request_interview_table.html' , {
                                                                  'All_requests' : request_all,
                                                                  'Open_request_amount' : open_request,
                                                                  'Close_request_amount' : close_request,
                                                                  },request=request)
    return JsonResponse({'html' : html})

def show_open_request_interview(request):
    if request.method == 'GET':
        request_all,open_request,close_request = get_open_request_interview(request)
        html = render_to_string('request_interview_table.html' , {
                                                                  'All_requests' : request_all,
                                                                  'Open_request_amount' : open_request,
                                                                  'Close_request_amount' : close_request,
                                                                  },request=request)
    return JsonResponse({'html' : html})

def show_close_request_candidate(request):
    if request.method == 'GET':
        request_all,open_request,close_request = get_close_request_candidate(request)
        html = render_to_string('request_candidate_table.html' , {
                                                                  'All_requests' : request_all,
                                                                  'Open_request_amount' : open_request,
                                                                  'Close_request_amount' : close_request,
                                                                  },request=request)
    return JsonResponse({'html' : html})

def show_open_request_candidate(request):
    if request.method == 'GET':
        request_all,open_request,close_request = get_open_request_candidate(request)
        html = render_to_string('request_candidate_table.html' , {
                                                                  'All_requests' : request_all,
                                                                  'Open_request_amount' : open_request,
                                                                  'Close_request_amount' : close_request,
                                                                  },request=request)
    return JsonResponse({'html' : html})

# ______________________________________________________________________________________________________________________________________________

def new_request_candidate(request):
    project_types = ProjectType.objects.all()
    levels = LevelRequest.objects.all()
    positions = Position.objects.all()

    if request.method == 'POST':
        request_id = generate_request_id()
        request_title = request.POST.get('request_title')
        project_name = request.POST.get('project_name')
        project_site = request.POST.get('project_site')
        tor_employee_amount = request.POST.get('tor_employee_amount')
        now_employee_amount = request.POST.get('now_employee_amount')
        vacancy_employee_amount = request.POST.get('vacancy_employee_amount')
        requirement = request.POST.get('requirement')
        certification = request.POST.get('certification')
        note = request.POST.get('note')

        project_type_id = request.POST.get('project_type')
        project_type = get_object_or_404(ProjectType, project_type_id=project_type_id)
        level_id = request.POST.get('level')
        level = get_object_or_404(LevelRequest, level_id=level_id)
        owner = get_object_or_404(Profile, user=request.user)
        status = get_object_or_404(Status, status_id='1')
        request_type = get_object_or_404(RequestType, request_type_id='1')

        request_position_id = request.POST.get('request_position')
        request_position_other = request.POST.get('request_position_other_name')
        print(request_position_id,"||||||||||",request_position_other)
        request_position = get_object_or_404(Position, position_id=request_position_id)


        request_candidate = RequestCandidate(project_name=project_name,
                                             project_site=project_site,tor_employee_amount=tor_employee_amount,
                                             now_employee_amount=now_employee_amount,vacancy_employee_amount=vacancy_employee_amount,
                                             requirement=requirement,certification=certification,note=note,project_type=project_type,
                                             level=level)
        request_candidate.save()

        request_detail = Request(request_id=request_id,request_type=request_type,request_candidate=request_candidate,request_title=request_title,request_position=request_position,request_position_other=request_position_other,owner=owner,status=status)
        request_detail.save()

    context = {
        'ProjectTypes' : project_types,
        'Levels' : levels,
        'Positions' : positions,

    }
    template = loader.get_template("new_request_candidate.html")
    return HttpResponse(template.render(context, request))

def update_interview_log(request,user_profile,interview_status,order_items):
    interview_status_log = InterviewStatusLog(updater=user_profile,interview_status=interview_status)
    interview_status_log.save()
    for order_item in order_items:
        order_item.interview_status_log.add(interview_status_log)
        order_item.save()

def request_detail(request,request_id):
    selected_request = Request.objects.filter(request_id=request_id).first()

    add_request_datetime = selected_request.datetime_add_request
    day_rq,hour_rq,min_rq = compare_request_now_time(add_request_datetime)
    comment_all = selected_request.comment.all()

    last_status = selected_request.status
    status_all = Status.objects.all()

    if request.method == 'POST':
        comment_id = generate_comment_id(request_id)
        comment_title = request.POST.get('comment_title')
        comment_detail = request.POST.get('comment_detail')
        status_id = request.POST.get('status')
        owner = get_object_or_404(Profile, user=request.user)
        if status_id:
            print("Entry1")
            status = Status.objects.filter(status_id=status_id).first()
            if status != last_status:
                status_comment = 'Status changed from {0} to {1} by {2}'.format(last_status.status_name,status.status_name,owner.user.first_name)
                comment_detail = status_comment + comment_detail
                print(comment_detail)
                print("Not Same Status")
                selected_request.status=status
            comment = Comment(comment_id=comment_id,comment_title=comment_title,comment_detail=comment_detail,owner=owner,status=status)
            comment.save()
        # อัพเดต Candidate Status
        if selected_request.request_type.request_type_id == '2':
            print("REQUEST INTERVIEW")
            order_items = selected_request.request_interview.order.items.all()
            print(order_items)
            if status != last_status:
                if status.status_id == '2':
                    interview_status = InterviewStatus.objects.filter(status_name='IN PROGRESS').first()
                    print(interview_status)
                    order_items.update(interview_status=interview_status)
                    update_interview_log(request,owner,interview_status,order_items)
                if status.status_id == '1':
                    interview_status = InterviewStatus.objects.filter(status_name='IN REQUEST').first()
                    print(interview_status)
                    order_items.update(interview_status=interview_status)
                    update_interview_log(request,owner,interview_status,order_items)
                if status.status_id == '3':
                    interview_status = InterviewStatus.objects.filter(status_name='INTERVIEWED').first()
                    print(interview_status)
                    order_items.update(interview_status=interview_status)
                    update_interview_log(request,owner,interview_status,order_items)
        # else:
        #     print("Entry2")
        #     comment = Comment(comment_id=comment_id,comment_title=comment_title,comment_detail=comment_detail,owner=owner)
        #     comment.save()
        selected_request.last_comment_owner = owner
        selected_request.comment.add(comment)
        selected_request.save()


    context = {
        'Selected_request' : selected_request,
        'Day' : day_rq,
        'Hour' : hour_rq,
        'Min' : min_rq,
        'Comments' : comment_all,
        'Status' : status_all,
        'LastStatus' : last_status.status_name,
    }
    template = loader.get_template("request_detail.html")
    return HttpResponse(template.render(context, request))
