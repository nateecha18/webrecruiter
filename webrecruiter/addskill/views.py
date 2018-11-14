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
from .models import Skill

import json
from django.shortcuts import HttpResponse
from django.template import loader, RequestContext
from django.template import Context, Template
from django.template.loader import render_to_string
import csv
from request.models import Status,Comment,RequestType,Position,RequestCandidate,RequestInterview,Request
from candidate_cart.models import OrderItem, Order, InterviewStatus
from tor.models import ProjectType,ProjectLevel,PositionProject,Tor,PositionAll



# Create your views here.
User = get_user_model()

def index(request):
    all_skill = Skill.objects.all()
    # print("All Skill : " + str(all_skill))
    skill_name = ['fah']
    for name in all_skill:
        skill_name.append(name.skill_name)
    # print("Skill Name : "+ str(skill_name))
    if request.method == 'POST':
        skill_name = request.POST["skill_name"]
        skill_type = request.POST["skill_type"]
        if skill_name:
            skill = Skill(skill_name=skill_name,skill_type=skill_type)
            skill.save()
        else:
            messages.error(request, all_skill)
            return HttpResponseRedirect(reverse("index"))

        all_skill = Skill.objects.all()

        context = {
            'Skill': all_skill,
        }
        template = loader.get_template("addskill.html")
        return HttpResponse(template.render(context, request))



    return render(request, "addskill.html", {'Skill': all_skill, 'Skill_name' : skill_name})

def submit_skill(request):
    skill_name = request.POST["skill_name"]
    skill_type = request.POST["skill_type"]
    if skill_name:
        skill = Skill(skill_name=skill_name,skill_type=skill_type)
        skill.save()
    else:
        messages.error(request, "Nooo!!")
        return HttpResponseRedirect(reverse("index"))

    all_skill = Skill.objects.all()

    context = {
        'Skill': all_skill,
    }
    template = loader.get_template("addskill.html")
    return HttpResponse(template.render(context, request))


def create_skill(request):
    if request.method == 'POST':
        print("Entryy")
        name = request.POST['name']
        type = request.POST['type']  # name for select in your html is 'skill_type' so use that

        skill = Skill(skill_name=name,skill_type=type)
        skill.save()
        all_skill = Skill.objects.all()

    return HttpResponse('success') # Empty HttpResponse doesn't makes much sense, also for ajax I would recommend JsonResponse

def show_skill(request):
    all_skill = Skill.objects.all().values_list('skill_name','skill_type')

    response_data = {}
    try:
        response_data['result'] = "Success"
        response_data['message'] = list(all_skill)
        print(response_data)

    except Exception as e:
        response_data['result'] = "Fail"
        response_data['message'] = "Fail!"

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def load_interview_status(file_path):
    "this loads position from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    for row in reader:
        interview_status = InterviewStatus(status_id=row['status_id'],status_name=row['status_name'])
        interview_status.save()

def load_project_type(file_path):
    "this loads ProjectType from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    for row in reader:
        project_type = ProjectType(project_type_id=row['project_type_id'],project_type_name=row['project_type_name'])
        project_type.save()

def load_project_level(file_path):
    "this loads ProjectType from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    for row in reader:
        project_level = ProjectLevel(level_id=row['level_id'],level_name=row['level_name'],level_description=row['level_description'])
        project_level.save()

def load_position_existing_project(file_path):
    "this loads existing_project from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    project_type = ProjectType.objects.filter(project_type_name='Existing Project').first()
    for row in reader:
        level = ProjectLevel.objects.filter(level_id=row['level']).first()
        print(row['project_tor_amount'])
        position_existing_project = PositionProject(project_name=row['project_name'],
                                                    project_type=project_type,
                                                    project_site=row['project_site'],
                                                    project_tor_amount=int(row['project_tor_amount']),
                                                    project_now_amount=int(row['project_now_amount']),
                                                    level=level,
                                                    requirement=row['requirement'],
                                                    certification=row['certification'],
                                                    note=row['note'],)
        position_existing_project.save()

def load_position_forecast_project(file_path):
    "this loads forecast_project from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    project_type = ProjectType.objects.filter(project_type_name='Forecast Project').first()
    for row in reader:
        level = ProjectLevel.objects.filter(level_id=row['level']).first()
        print(row['project_tor_amount'])
        position_forecast_project = PositionProject(project_name=row['project_name'],
                                                    project_type=project_type,
                                                    project_site=row['project_site'],
                                                    project_tor_amount=int(row['project_tor_amount']),
                                                    project_now_amount=int(row['project_now_amount']),
                                                    level=level,
                                                    requirement=row['requirement'],
                                                    certification=row['certification'],
                                                    note=row['note'],)
        position_forecast_project.save()

def load_tor(file_path):
    "this loads tor from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    for row in reader:
        tor = Tor(position_name=row['position_name'],
                  position_type=row['position_type'],
                  position_role_des=row['position_role_des'],
                  position_edu_des=row['position_edu_des'],
                  position_exp_des=row['position_exp_des'],
                  position_tor_amount=row['position_tor_amount'],
                  position_now_amount=row['position_now_amount'],)
        tor.save()

def load_position(file_path):
    "this loads Position from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    for row in reader:
        position = PositionAll(position_id=row['position_id'],position_name=row['position_name'])
        position.save()
