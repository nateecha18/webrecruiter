from django.shortcuts import render, redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View

from jobapply.utils import render_to_pdf  # created in step 4
from django.shortcuts import render_to_response
from django.template import RequestContext

from jobapply.models import CandidateBasic
from django.db.models import Q

# Import For Authenticate Account
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm


class  UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # display blank form
    def get (self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # เนื่องจาก Password มันไม่ใช่ PlainText มันถูก Hash มาแล้ว จึงไม่สามารถเปลี่ยน Password ได้โดยตรง
            user.set_password(password)
            user.save()

            # return User objact if credentials are correct (เช็ค user/pass ว่าถูกต้องมั้ย)
            user = authenticate(username=username,password=password)
            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('filter')

        return render(request, self.template_name, {'form':form})
