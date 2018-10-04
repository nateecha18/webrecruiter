from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View

# Import For Authenticate Account
from django.contrib.auth import (
        authenticate,
        login,
        get_user_model,
        login,
        logout,

        )
from .forms import UserLoginForm
from .models import Profile

def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders': my_orders
	}

	return render(request, "profile.html", context)


def login_view(request):
    print(request.user.is_authenticated,request.user.get_username)
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated,request.user.get_username)
        return redirect('filter')


    return render(request, "login_form.html", {"form":form, "title":title})

def logout_view(request):
    logout(request)
    return redirect('login')
