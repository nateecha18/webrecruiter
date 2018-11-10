from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
# REST FRAMWORK IMPORT
from rest_framework.views import APIView
from rest_framework.response import Response
# END REST FRAMWORK IMPORT
# from django.contrib.auth import get_user_model
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
import csv

from tor.models import ProjectType,ProjectLevel,PositionProject,Tor



# Create your views here.

def index(request):
    tor_all = Tor.objects.all()
    return render(request, "tor_management.html", {'Tors' : tor_all,})

def update_project(request,project_id=None):
    print("Entry UPDATE")
    project_level = ProjectLevel.objects.all()
    selected_project = PositionProject.objects.filter(id = project_id).first()
    print(selected_project)
    # return HttpResponse(json.dumps(response_data), content_type="application/json")
    if request.method == 'POST':
        selected_project_for_edit = PositionProject.objects.filter(id = project_id)
        project_name = request.POST["project_name"]
        project_site = request.POST["project_site"]
        project_tor_amount = request.POST["project_tor_amount"]
        project_now_amount = request.POST["project_now_amount"]
        level_id = request.POST["level"]
        level = ProjectLevel.objects.filter(level_id=level_id).first()
        requirement = request.POST["requirement"]
        certification = request.POST["certification"]
        note = request.POST["note"]
        print(project_name,project_site,project_tor_amount,project_now_amount,level,requirement,certification,note)
        print(selected_project.project_name,selected_project.project_site,selected_project.project_tor_amount,selected_project.project_now_amount,selected_project.level,selected_project.requirement,selected_project.certification,selected_project.note)
        # if selected_project.project_name != project_name:
        #     selected_project_for_edit.update(project_name=project_name)
        # if selected_project.project_site != project_site:
        #     selected_project_for_edit.update(project_site=project_site)
        # if selected_project.project_tor_amount != project_tor_amount:
        #     selected_project_for_edit.update(project_tor_amount=project_tor_amount)
        # if selected_project.project_now_amount != project_now_amount:
        #     selected_project_for_edit.update(project_now_amount=project_now_amount)
        # if selected_project.level != level:
        #     selected_project_for_edit.update(level=level)
        # if selected_project.requirement != requirement:
        #     selected_project_for_edit.update(requirement=requirement)
        # if selected_project.certification != certification:
        #     selected_project_for_edit.update(certification=certification)
        # if selected_project.note != note:
        #     selected_project_for_edit.update(note=note)
        status = 0
        if selected_project.project_name != project_name:
            selected_project.project_name=project_name
            status += 1
        if selected_project.project_site != project_site:
            selected_project.project_site=project_site
            status += 1
        if selected_project.project_tor_amount != project_tor_amount:
            selected_project.project_tor_amount=project_tor_amount
            status += 1
        if selected_project.project_now_amount != project_now_amount:
            selected_project.project_now_amount=project_now_amount
            status += 1
        if selected_project.level != level:
            selected_project.level=level
            status += 1
        if selected_project.requirement != requirement:
            selected_project.requirement=requirement
            status += 1
        if selected_project.certification != certification:
            selected_project.certification=certification
            status += 1
        if selected_project.note != note:
            selected_project.note=note
        if status:
            selected_project.save()

        print("Edited +++++++++",project_id)
        return redirect('tor_management')
    context={
        'SelectedProject' :selected_project,
        'Levels' : project_level,
    }
    return render(request, 'modal.html', context)
    # html = render_to_string('modal.html' , {'SelectedProject' :selected_project },request=request)
    # return JsonResponse({'html' : html})
