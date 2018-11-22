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
from request.models import Status,Comment,RequestType,RequestCandidate,RequestInterview,Request,UpdateAmountLog
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
from tor.models import ProjectType,ProjectLevel,PositionField,Project,PositionAll
from urllib.request import urlopen


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
    status_close = Status.objects.filter(status_name='Closed').first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(~Q(status_id=status_close))
        open_request = Request.objects.filter(~Q(status_id=status_close)).count()
        close_request = Request.objects.filter(status_id=status_close).count()

    else:
        request_all = Request.objects.filter(Q(owner=user_profile),~Q(status_id=status_close))
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id=status_close)).count()
        close_request = Request.objects.filter(owner=user_profile,status_id=status_close).count()
    return request_all,open_request,close_request

def get_close_request(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()
    status_close = Status.objects.filter(status_name='Closed').first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(status_id=status_close)
        open_request = Request.objects.filter(~Q(status_id=status_close)).count()
        close_request = Request.objects.filter(status_id=status_close).count()

    else:
        request_all = Request.objects.filter(owner=user_profile,status_id=status_close)
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id=status_close)).count()
        close_request = Request.objects.filter(owner=user_profile,status_id=status_close).count()
    return request_all,open_request,close_request

def get_close_request_interview(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()
    request_type_interview = RequestType.objects.filter(request_type_name='RequestInterview').first()
    status_close = Status.objects.filter(status_name='Closed').first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(status_id=status_close,request_type=request_type_interview)
        open_request = Request.objects.filter(~Q(status_id=status_close),Q(request_type=request_type_interview)).count()
        close_request = Request.objects.filter(status_id=status_close,request_type=request_type_interview).count()

    else:
        request_all = Request.objects.filter(owner=user_profile,status_id=status_close,request_type=request_type_interview)
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id=status_close),Q(request_type=request_type_interview)).count()
        close_request = Request.objects.filter(owner=user_profile,status_id=status_close,request_type=request_type_interview).count()
    return request_all,open_request,close_request

def get_open_request_interview(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()
    request_type_interview = RequestType.objects.filter(request_type_name='RequestInterview').first()
    status_close = Status.objects.filter(status_name='Closed').first()


    if has_role(user, 'hr'):
        print("HR")
        request_all = Request.objects.filter(~Q(status_id=status_close),Q(request_type=request_type_interview))
        open_request = Request.objects.filter(~Q(status_id=status_close),Q(request_type=request_type_interview)).count()
        close_request = Request.objects.filter(status_id=status_close,request_type=request_type_interview).count()

    else:
        request_all = Request.objects.filter(Q(owner=user_profile),~Q(status_id=status_close),Q(request_type=request_type_interview))
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id=status_close),Q(request_type=request_type_interview)).count()
        close_request = Request.objects.filter(owner=user_profile,status_id=status_close,request_type=request_type_interview).count()
    return request_all,open_request,close_request

def get_close_request_candidate(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()
    request_type_candidate = RequestType.objects.filter(request_type_name='RequestCandidate').first()
    status_close = Status.objects.filter(status_name='Closed').first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(status_id=status_close,request_type=request_type_candidate)
        open_request = Request.objects.filter(~Q(status_id=status_close),Q(request_type=request_type_candidate)).count()
        close_request = Request.objects.filter(status_id=status_close,request_type=request_type_candidate).count()

    else:
        request_all = Request.objects.filter(owner=user_profile,status_id=status_close,request_type=request_type_candidate)
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id=status_close),Q(request_type=request_type_candidate)).count()
        close_request = Request.objects.filter(owner=user_profile,status_id=status_close,request_type=request_type_candidate).count()
    return request_all,open_request,close_request

def get_open_request_candidate(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()
    request_type_candidate = RequestType.objects.filter(request_type_name='RequestCandidate').first()
    status_close = Status.objects.filter(status_name='Closed').first()

    if has_role(user, 'hr'):
        request_all = Request.objects.filter(~Q(status_id=status_close),Q(request_type=request_type_candidate))
        open_request = Request.objects.filter(~Q(status_id=status_close),Q(request_type=request_type_candidate)).count()
        close_request = Request.objects.filter(status_id=status_close,request_type=request_type_candidate).count()

    else:
        request_all = Request.objects.filter(Q(owner=user_profile),~Q(status_id=status_close),Q(request_type=request_type_candidate))
        open_request = Request.objects.filter(Q(owner=user_profile),~Q(status_id=status_close),Q(request_type=request_type_candidate)).count()
        close_request = Request.objects.filter(owner=user_profile,status_id=status_close,request_type=request_type_candidate).count()
    return request_all,open_request,close_request

# ______________________________________________________________________________________________________________________________________________

def index(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')

def request_interview(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')

def request_candidate(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')

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
    # project_types = ProjectType.objects.all()
    # levels = LevelRequest.objects.all()
    positions = PositionAll.objects.all()
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()

    if has_role(user, 'hr'):
        all_project = Project.objects.all()
    else:
        all_project = Project.objects.filter(owner=user_profile)

    if request.method == 'POST':
        request_id = generate_request_id()
        print("request_id",request_id)
        request_title = request.POST.get('request_title')
        project_id = request.POST.get('project_name')
        project = Project.objects.filter(id=project_id).first()
        print(project_id,"project",project)
        position_id = request.POST.get('position_name')
        position = PositionField.objects.filter(id=position_id)
        print(position_id,"position",position)
        tor_employee_amount = position.first().position_tor_amount
        empty_employee_amount = int(request.POST.get('empty_employee_amount'))
        now_employee_amount = position.first().position_now_amount-empty_employee_amount
        requirement = request.POST.get('requirement')
        certification = request.POST.get('certification')
        note = request.POST.get('note')

        owner = get_object_or_404(Profile, user=request.user)
        status = get_object_or_404(Status, status_id='1')
        request_type = get_object_or_404(RequestType, request_type_id='1')

        print(request_title,tor_employee_amount,empty_employee_amount,requirement,certification,note)
        print(owner,status,request_type)
        request_candidate = RequestCandidate(project=project,
                                             position=position.first(),
                                             tor_employee_amount=tor_employee_amount,
                                             now_employee_amount=now_employee_amount,
                                             empty_employee_amount = empty_employee_amount,
                                             requirement=requirement,
                                             certification=certification,
                                             note=note,)
        request_candidate.save()
        print("now_employee_amount",int(now_employee_amount))
        print(position.first().position_now_amount)
        request_detail = Request(request_id=request_id,
                                 request_type=request_type,
                                 request_candidate=request_candidate,
                                 request_title=request_title,
                                 request_position=position.first().position_name,
                                 owner=owner,status=status)
        request_detail.save()
        position.update(position_now_amount=int(now_employee_amount),
                        requirement=requirement,
                        certification=certification,
                        note=note,)
        return redirect('request_candidate')

    context = {
        'AllProject' : all_project,
        'Positions' : positions,

    }
    template = loader.get_template("create_new_request_candidate.html")
    return HttpResponse(template.render(context, request))

def get_position(request,project_id=None):
    selected_project = Project.objects.filter(id=project_id).first()
    all_position = selected_project.positions.all()
    context={
        'AllPosition' : all_position,
        'SelectedProject' : selected_project,
    }
    return render(request, 'select_option_position.html', context)

def get_position_detail(request,position_id=None):
    selected_position = PositionField.objects.filter(id=position_id).first()
    context={
        'PositionDetail' : selected_position,
    }
    return render(request, 'position_detail.html', context)

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
        comment_title = ''
        comment_detail = request.POST.get('comment_detail')
        status_id = request.POST.get('status')
        owner = get_object_or_404(Profile, user=request.user)
        if status_id:
            print("Entry1")
            status = Status.objects.filter(status_id=status_id).first()
            if status != last_status:
                comment_title = 'Status changed from {0} to {1} by {2}'.format(last_status.status_name,status.status_name,owner.user.first_name)
                print("Not Same Status")
                selected_request.status=status
        if selected_request.request_type.request_type_id == '1':
            checkbox_update_amount = request.POST.get('checkbox_update_amount')
            if checkbox_update_amount:
                update_amount = int(request.POST.get('update_amount'))
                comment_title = 'สรรหาพนักงานเพิ่ม {0} คน'.format(update_amount)
        comment = Comment(comment_id=comment_id,comment_title=comment_title,comment_detail=comment_detail,owner=owner,status=status)
        comment.save()
        # อัพเดต Candidate Status
        request_type_candidate = RequestType.objects.filter(request_type_name='RequestCandidate').first()
        if selected_request.request_type.request_type_id == '1':
            diff_amount = selected_request.request_candidate.tor_employee_amount - selected_request.request_candidate.now_employee_amount
            selected_position = selected_request.request_candidate.position
            checkbox_update_amount = request.POST.get('checkbox_update_amount')
            print(checkbox_update_amount)
            if checkbox_update_amount:
                print("Checkbox Selected!!")
                update_amount = int(request.POST.get('update_amount'))
                print(update_amount)
                update_amount_log = UpdateAmountLog(added_amount=update_amount,comment=comment)
                print(update_amount_log)
                update_amount_log.save()
                print(selected_position.position_now_amount)
                selected_position.position_now_amount = selected_position.position_now_amount+update_amount
                print(selected_position.position_now_amount )
                selected_position.save()
                selected_request.request_candidate.update_amount_log.add(update_amount_log)


        if selected_request.request_type.request_type_id == '2':
            print("REQUEST INTERVIEW")
            order_items = selected_request.request_interview.order.items.filter(~Q(interview_status__status_name__in = ['CANCLED','HIRED','NOT HIRED']))
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
                    order_items.update(interview_status=interview_status,is_interviewed=True)
                    update_interview_log(request,owner,interview_status,order_items)
        # else:
        #     print("Entry2")
        #     comment = Comment(comment_id=comment_id,comment_title=comment_title,comment_detail=comment_detail,owner=owner)
        #     comment.save()
        selected_request.last_comment_owner = owner
        selected_request.comment.add(comment)
        selected_request.save()
        if selected_request.request_type.request_type_id == '1':
            if selected_request.request_candidate.diff_empty_amount_now() == 0:
                selected_request.request_candidate.is_full = True
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

def update_interview_status(request,request_id):
    user_profile = get_object_or_404(Profile, user=request.user)
    selected_request = Request.objects.filter(request_id=request_id).first()
    order_items = selected_request.request_interview.order.items.all()
    interview_status = InterviewStatus.objects.filter(status_id__in=['4','6','7'])
    if request.method == 'POST':
        update_status = request.POST.getlist('update_status')
        print("+++++",update_status)
        for each_update in update_status:
            if not each_update=='0':
                splited_update = each_update.split('_')
                order_item_id = splited_update[0]
                status_name = splited_update[1]
                print(order_item_id,status_name)
                order_item = OrderItem.objects.filter(id=order_item_id).first()
                selected_status = InterviewStatus.objects.filter(status_name=status_name).first()
                # อัพเดตสถานะ
                order_item.interview_status = selected_status
                # Add Status Log user by user
                interview_status_log = InterviewStatusLog(updater=user_profile,interview_status=selected_status)
                interview_status_log.save()
                order_item.interview_status_log.add(interview_status_log)
                order_item.save()
        return (redirect('request_detail', request_id=request_id))

    context={
        'Selected_request' : selected_request,
        'order_items' : order_items,
        'InterviewStatus' : interview_status,
    }
    return render(request, 'modal_update_interview_status.html', context)
