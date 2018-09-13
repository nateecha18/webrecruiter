from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View
from .models import FilterPosition


from jobapply.utils import render_to_pdf  # created in step 4
from django.shortcuts import render_to_response
from django.template import RequestContext

from jobapply.models import CandidateBasic
from django.db.models import Q


# Create your views here.
def index(request):
    all_candidate = CandidateBasic.objects.all()
    print("All Can : " + str(all_candidate))
    return render(request, "dashboard.html", {'Candidate': all_candidate})

def submit_filter(request):

    checkbox_position = request.POST.get('checkbox_position', False)
    operator_position = request.POST.getlist('operator_position')
    filter_position = request.POST.getlist('filter_position')
    print("Position : " + str(filter_position))

    checkbox_salary = request.POST.get('checkbox_salary', False)
    operator_salary = request.POST["operator_salary"]
    filter_salary = request.POST["filter_salary"]

    checkbox_blood = request.POST.get('checkbox_blood', False)
    operator_blood = request.POST["operator_blood"]
    filter_blood = request.POST["filter_blood"]

    checkbox_gpa = request.POST.get('checkbox_gpa', False)
    operator_gpa = request.POST["operator_gpa"]
    filter_gpa = request.POST["filter_gpa"]

    checkbox_gender = request.POST.get('checkbox_gender', False)
    operator_gender = request.POST["operator_gender"]
    filter_gender = request.POST["filter_gender"]


    position = FilterPosition(checkbox_position=checkbox_position,operator_position=operator_position,filter_position=filter_position)
    position.save()

    all_candidate = CandidateBasic.objects.all()
    if (checkbox_position=='1') :
        checkbox_position_set=CandidateBasic.objects.all()
        print("len :" + str(len(operator_position)))
        for i in range(0,len(operator_position)):
            if (operator_position[i]=='1'):
                checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(position__iexact=filter_position[i]))
            if (operator_position[i]=='2'):
                checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(~Q(position__iexact=filter_position[i])))
            if (operator_position[i]=='3'):
                checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(position__icontains=filter_position[i]))
                print(str(i) + ":Selected Candidate :" + str(checkbox_position_set))
            if (operator_position[i]=='4'):
                checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(~Q(position__icontains=filter_position[i])))
        all_candidate = all_candidate.intersection(checkbox_position_set)

    print("Check Position1 : " + str(all_candidate))

    if (checkbox_salary=='1') :
        print("Check Position2 : " + str(all_candidate))
        if (operator_salary=='1'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(salary=filter_salary))
        elif (operator_salary=='2'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(salary__gte=filter_salary))
        elif (operator_salary=='3'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(salary__lte=filter_salary))
        elif (operator_salary=='4'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(salary__gt=filter_salary))
        elif (operator_salary=='5'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(salary__lt=filter_salary))
    print("Check Salary : " + str(all_candidate))

    if (checkbox_blood=='1') :
        if (operator_blood=='1'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(blood__icontains=filter_blood))
        elif (operator_blood=='2'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(~Q(blood__icontains=filter_blood)))

    if (checkbox_gpa=='1') :
        if (operator_gpa=='1'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(nowEdu_gpa=filter_gpa))
        elif (operator_gpa=='2'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(nowEdu_gpa__gte=filter_gpa))
        elif (operator_gpa=='3'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(nowEdu_gpa__lte=filter_gpa))
        elif (operator_gpa=='4'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(nowEdu_gpa__gt=filter_gpa))
        elif (operator_gpa=='5'):
            all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(nowEdu_gpa__lt=filter_gpa))

    if (checkbox_gender=='1') :
        if (operator_gender=='1'):
            if (filter_gender=='m'):
                print("______________________GENDER : M  / IS________________________")
                all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(name_title="นาย"))
                print("Selected Candidate Gender"+str(all_candidate))
            else:
                all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(~Q(name_title="นาย")))
        elif (operator_gender=='2'):
            if (filter_gender=='m'):
                all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(~Q(name_title="นาย")))
            else:
                all_candidate = all_candidate.intersection(CandidateBasic.objects.filter(name_title="นาย"))

    if (checkbox_position!='1' and checkbox_salary!='1' and checkbox_blood!='1' and checkbox_gpa!='1' and checkbox_gender!='1') :
        all_candidate = CandidateBasic.objects.all()
    context = {
        'Candidate': all_candidate,
    }
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render(context, request))
