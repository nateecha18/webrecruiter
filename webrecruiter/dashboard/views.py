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

import json
from django.shortcuts import HttpResponse
from django.template import loader, RequestContext
from django.template import Context, Template
from django.template.loader import render_to_string

from account.models import Profile
from jobapply.models import CandidateBasic

from candidate_cart.extras import generate_order_id
from candidate_cart.models import OrderItem, Order
from request.models import Status,ProjectType,LevelRequest,Comment,RequestType,RequestCandidate,RequestInterview,Request
from request.generate_id import generate_request_id
# Create your views here.

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_profile = Profile.objects.filter(user=user).first()
        request_candidate_type = RequestType.objects.filter(request_type_id='1').first()
        request_interview_type = RequestType.objects.filter(request_type_id='2').first()

        candidate = CandidateBasic.objects.all()
        request_all = Request.objects.filter(owner=user_profile)
        request_candidate = Request.objects.filter(owner=user_profile,request_type=request_candidate_type)
        request_interview = Request.objects.filter(owner=user_profile,request_type=request_interview_type)

        context = {
            'candidates' : candidate,
            'request_candidate' : request_candidate,
            'request_interview' : request_interview,
        }
        return render(request,"dashboard.html",context)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        user_count = User.objects.all().count()
        labels = ["User Number", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default = [user_count,123,456,789,101,112]
        data = {
            "labels" : labels,
            "default" : default,
        }
        return Response(data)
