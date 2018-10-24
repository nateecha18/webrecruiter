from django.shortcuts import render

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

# Create your views here.

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
