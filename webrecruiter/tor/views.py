from django.shortcuts import render
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

from tor.models import Tor


# Create your views here.

def index(request):
    tor_all = Tor.objects.all()
    return render(request, "tor_management.html", {'Tors' : tor_all,})

def update_tor(request,tor_id=None):
    print("Entry")
    pass
