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
