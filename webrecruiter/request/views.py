from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View
from account.models import Profile
from rank.models import CandidateRank
from jobapply.models import CandidateBasic
from candidate_cart.models import OrderItem,Order
from rolepermissions.decorators import has_role_decorator
from request.models import Status,ProjectType,LevelRequest,Comment,RequestCandidate
from request.generate_id import generate_request_id
from request.generate_id import generate_comment_id
from request.compare_time import compare_request_now_time
import datetime
from datetime import datetime,date,time,timedelta, timezone
import pytz
import math

# @has_role_decorator('hr')
def index(request):
    request_candidates = RequestCandidate.objects.all()
    context = {
        'RequestCandidates' : request_candidates,
    }
    template = loader.get_template("request.html")
    return HttpResponse(template.render(context, request))

def new_request(request):
    project_types = ProjectType.objects.all()
    levels = LevelRequest.objects.all()
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

        request_candidate = RequestCandidate(request_id=request_id,request_title=request_title,project_name=project_name,
                                             project_site=project_site,tor_employee_amount=tor_employee_amount,
                                             now_employee_amount=now_employee_amount,vacancy_employee_amount=vacancy_employee_amount,
                                             requirement=requirement,certification=certification,note=note,project_type=project_type,
                                             level=level,owner=owner)
        request_candidate.save()


    context = {
        'ProjectTypes' : project_types,
        'Levels' : levels,

    }
    template = loader.get_template("request_candidate.html")
    return HttpResponse(template.render(context, request))


def request_detail(request,request_id):
    selected_request = RequestCandidate.objects.filter(request_id=request_id).first()

    add_request_datetime = selected_request.datetime_add_request
    day_rq,hour_rq,min_rq = compare_request_now_time(add_request_datetime)
    comment_all = selected_request.comment.all()
    print(comment_all)
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
            selected_request.status=status
            comment = Comment(comment_id=comment_id,comment_title=comment_title,comment_detail=comment_detail,owner=owner,status=status)
            comment.save()
        else:
            print("Entry2")
            comment = Comment(comment_id=comment_id,comment_title=comment_title,comment_detail=comment_detail,owner=owner)
            comment.save()
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
    }
    template = loader.get_template("request_detail.html")
    return HttpResponse(template.render(context, request))
