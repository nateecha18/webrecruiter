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

from tor.models import ProjectType,ProjectLevel,Project,PositionField,PositionAll
from account.models import Profile
from request.models import Status,Comment,RequestType,RequestCandidate,RequestInterview,Request
from django.db.models import Q
from django.db.models import Avg, Count, Min, Sum
from collections import Counter



# Create your views here.

def index(request):
    project_all = Project.objects.all()
    all_tor_amount = 0
    all_now_amount = 0
    print("project_all",project_all)
    for project in project_all:
        if project.positions.all():
            all_tor_amount += project.positions.all().aggregate(Sum('position_tor_amount'))['position_tor_amount__sum']
            all_now_amount += project.positions.all().aggregate(Sum('position_now_amount'))['position_now_amount__sum']
    diff_amount = all_tor_amount-all_now_amount
    context={
        'AllProject' : project_all,
        'AllTor' : all_tor_amount,
        'AllNow' : all_now_amount,
        'Diff' : diff_amount,
    }
    return render(request, "tor_management2.html", context)

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
        project_tor_amount = int(request.POST["project_tor_amount"])
        project_now_amount = int(request.POST["project_now_amount"])
        level_id = request.POST["level"]
        level = ProjectLevel.objects.filter(level_id=level_id).first()
        requirement = request.POST["requirement"]
        certification = request.POST["certification"]
        note = request.POST["note"]
        print(project_name,project_site,project_tor_amount,project_now_amount,level,requirement,certification,note)
        print(selected_project.project_name,selected_project.project_site,selected_project.project_tor_amount,selected_project.project_now_amount,selected_project.level,selected_project.requirement,selected_project.certification,selected_project.note)
        status = 0
        if selected_project.project_name != project_name:
            print("project_name")
            selected_project.project_name=project_name
            status += 1
        if selected_project.project_site != project_site:
            print("project_site")
            selected_project.project_site=project_site
            status += 1
        if selected_project.project_tor_amount != project_tor_amount:
            print("project_tor_amount", selected_project.project_tor_amount,type(selected_project.project_tor_amount),project_tor_amount,type(project_tor_amount))
            selected_project.project_tor_amount=project_tor_amount
            status += 1
        if selected_project.project_now_amount != project_now_amount:
            print("project_now_amount")
            selected_project.project_now_amount=project_now_amount
            status += 1
        if selected_project.level != level:
            print("level")
            selected_project.level=level
            status += 1
        if selected_project.requirement != requirement:
            print("requirement")
            selected_project.requirement=requirement
            status += 1
        if selected_project.certification != certification:
            print("certification")
            selected_project.certification=certification
            status += 1
        if selected_project.note != note:
            print("note")
            selected_project.note=note
        if status:
            print("status",status)
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

def create_project(request,position_id=None):
    print("Entry CREATE")
    project_level = ProjectLevel.objects.all()
    selected_tor = Tor.objects.filter(id = position_id).first()
    project_type = ProjectType.objects.all()
    print(selected_tor)
    # return HttpResponse(json.dumps(response_data), content_type="application/json")
    if request.method == 'POST':
        project_type_id = request.POST["project_type_id"]
        project_type = ProjectType.objects.filter(project_type_id=project_type_id).first()
        project_name = request.POST["project_name"]
        project_site = request.POST["project_site"]
        project_tor_amount = int(request.POST["project_tor_amount"])
        project_now_amount = int(request.POST["project_now_amount"])
        level_id = request.POST["level"]
        level = ProjectLevel.objects.filter(level_id=level_id).first()
        requirement = request.POST["requirement"]
        certification = request.POST["certification"]
        note = request.POST["note"]
        print(project_type,project_name,project_site,project_tor_amount,project_now_amount,level,requirement,certification,note)
        project = PositionProject(project_name=project_name,
                                  project_type=project_type,
                                  project_site=project_site,
                                  project_tor_amount=project_tor_amount,
                                  project_now_amount=project_now_amount,
                                  level=level,requirement=requirement,
                                  certification=certification,
                                  note=note,)
        project.save()
        selected_tor.position_project.add(project)

        print("Create! +++++++++",selected_tor)
        return redirect('tor_management')

    context={
        'ProjectTypes' : project_type,
        'SelectedTor' : selected_tor,
        'Levels' : project_level,
    }
    return render(request, 'modal_creat_project.html', context)


def delete_project(request,position_id=None,project_id=None):
    print("Entry DELETE")
    selected_project = PositionProject.objects.filter(id = project_id)
    selected_tor = Tor.objects.filter(id = position_id)
    if selected_project.exists():
        project_to_delete = selected_project[0]
        selected_tor[0].position_project.remove(project_to_delete)

    return redirect('tor_management')

def project(request):
    user = request.user
    project_owner = Profile.objects.filter(user=user).first()
    project_all = Project.objects.filter(owner=project_owner)
    print(project_all)
    context={
        'ProjectOwner' : project_owner,
        'AllProject' : project_all,
    }
    return render(request, 'project.html', context)

def add_project(request):
    project_level = ProjectLevel.objects.all()
    project_type = ProjectType.objects.all()
    user = request.user
    project_owner = Profile.objects.filter(user=user).first()
    project_all = Project.objects.filter(owner=project_owner)
    print(project_all)
    if request.method == 'POST':
        print("POST")
        project_type_id = request.POST["project_type_id"]
        project_type = ProjectType.objects.filter(project_type_id=project_type_id).first()
        print(project_type,"!!!!!!!!!!!")
        project_name = request.POST["project_name"]
        project_site = request.POST["project_site"]
        level_id = request.POST["level"]
        level = ProjectLevel.objects.filter(level_id=level_id).first()
        print(project_type,project_name,project_site,level)
        print(type(project_type))
        print(type(level))

        project = Project(owner=project_owner,
                          project_name=project_name,
                          level=level,
                          project_type=project_type,
                          project_site=project_site,
                          )
        project.save()
        return redirect('project')
    context={
        'ProjectTypes' : project_type,
        'Levels' : project_level,
        'ProjectOwner' : project_owner,
        'AllProject' : project_all,
    }
    return render(request, 'modal_add_project.html', context)

def add_position(request,project_id=None):
    print(project_id)
    selected_project = Project.objects.filter(id=project_id).first()
    old_position = selected_project.positions.all()
    old_position_list = []
    for position in old_position:
        old_position_list.append(int(position.position_name.position_id))
    position_all = PositionAll.objects.filter(~Q(position_id__in=old_position_list))
    if request.method == 'POST':
        position_id = request.POST["position_id"]
        position_name = PositionAll.objects.filter(position_id=position_id).first()
        position_type = request.POST["position_type"]
        position_tor_amount = int(request.POST["position_tor_amount"])
        print(position_name,position_type,position_tor_amount,)
        position = PositionField(position_name=position_name,
                                 position_type=position_type,
                                 position_tor_amount=position_tor_amount,
                                 position_now_amount=position_tor_amount,)
        position.save()
        selected_project.positions.add(position)
        return redirect('project')
    context={
        'AllPosition' : position_all,
        'SelectedProject' : selected_project,
    }
    return render(request, 'modal_add_position.html', context)

def remove_position(request,project_id=None,position_id=None):
    project = Project.objects.filter(id=project_id).first()
    selected_position = PositionField.objects.filter(id=position_id).first()
    project.positions.remove(selected_position)
    # selected_position.delete()
    print("Entry DELETE",project,selected_position)
    # selected_project = PositionProject.objects.filter(id = project_id)
    # selected_tor = Tor.objects.filter(id = position_id)
    # if selected_project.exists():
    #     project_to_delete = selected_project[0]
    #     selected_tor[0].position_project.remove(project_to_delete)

    return redirect('project')

def export_employee_amount_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="existing_project.csv"'

    writer = csv.writer(response)
    writer.writerow(['No', 'Existing Project', 'Site', 'จำนวนตาม Tor','จำนวนตามจริง','จำนวนที่ขาด','ความเร่งด่วน','Certification','Requirment','หมายเหตุ'])
    project_all = []
    for p in Project.objects.all():
        project = []
        project.append(p.id)
        project.append(p.project_name)
        project.append(p.project_site)
        project.append(p.tor_amount()['position_tor_amount__sum'] if p.tor_amount()['position_tor_amount__sum'] else 0)
        project.append(p.now_amount()['position_now_amount__sum'] if p.now_amount()['position_now_amount__sum'] else 0)
        project.append(p.diff_empty_amount())
        project.append(p.level.level_id)
        position_all = p.positions.all()
        empty_position = dict()
        requirement_position = dict()
        certification_position = dict()
        for position in position_all:
            requests = Request.objects.filter(request_candidate__position=position,request_candidate__is_full=False)
            # ___________________ เก็บ REQUIREMENT
            request_req = dict()
            request_cert = dict()

            for request in requests:
                # ถ้ามี requirement ของ Position นี้อยู่แล้วให้เข้า IF
                if request_req.get(request.request_candidate.requirement):
                    request_req[request.request_candidate.requirement] += request.request_candidate.diff_empty_amount_now()
                # ถ้าไม่มีเข้า ELSE
                else:
                    request_req[request.request_candidate.requirement] = request.request_candidate.diff_empty_amount_now()

                # ถ้ามี Certification ของ Position นี้อยู่แล้วให้เข้า IF
                if request_cert.get(request.request_candidate.certification):
                    request_cert[request.request_candidate.certification] += request.request_candidate.diff_empty_amount_now()
                # ถ้าไม่มีเข้า ELSE
                else:
                    request_cert[request.request_candidate.certification] = request.request_candidate.diff_empty_amount_now()
            if request_req:
                requirement_position[position.position_name.position_name] = request_req
            print("requirement_position!!!!",requirement_position)

            if request_cert:
                certification_position[position.position_name.position_name] = request_cert
            print("certification_position!!!!",certification_position)

            if position.diff_position_empty_amount():
                empty_position[position.position_name.position_name] = position.diff_position_empty_amount()

        certification_position_list = []
        for key1, value1 in certification_position.items():
            for key2, value2 in value1.items():
                certification_position_list.append(str(key2)+"  ("+str(key1)+"x"+str(value2)+")")
        project.append(",".join(certification_position_list))

        requirement_position_list = []
        for key1, value1 in requirement_position.items():
            for key2, value2 in value1.items():
                requirement_position_list.append(str(key2)+"  ("+str(key1)+"x"+str(value2)+")")
        project.append(",".join(requirement_position_list))
        empty_position_list = []
        for key, value in empty_position.items():
            empty_position_list.append(str(key)+str(value))
        project.append(",".join(empty_position_list))



        writer.writerow(project)

    # Or if you want to write something else write like this

    return response
