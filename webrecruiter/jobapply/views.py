from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

# Create your views here.
def index(request):
	template=loader.get_template("index.html")
	return HttpResponse(template.render())
