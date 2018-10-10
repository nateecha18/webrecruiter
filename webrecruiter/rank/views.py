from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View
from rank.models import CandidateRank



# Create your views here.
def index(request):
    rank = CandidateRank.objects.all()
    context = {
        'rank' : rank
    }
    template = loader.get_template("rank.html")
    return HttpResponse(template.render(context, request))
    # return render('index.html', context_instance=RequestContext(request))
