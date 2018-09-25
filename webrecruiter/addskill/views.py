from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views
from .models import Skill

# Create your views here.

def index(request):
    all_skill = Skill.objects.all()
    print("All Skill : " + str(all_skill))

    skill_name = ['fah']
    for name in all_skill:
        skill_name.append(name.skill_name)
    print("Skill Name : "+ str(skill_name))


    return render(request, "addskill.html", {'Skill': all_skill, 'Skill_name' : skill_name})

def submit_skill(request):
    skill_name = request.POST["skill_name"]
    skill_type = request.POST["skill_type"]

    skill = Skill(skill_name=skill_name,skill_type=skill_type)
    skill.save()

    all_skill = Skill.objects.all()

    context = {
        'Skill': all_skill,
    }
    template = loader.get_template("addskill.html")
    return HttpResponse(template.render(context, request))
