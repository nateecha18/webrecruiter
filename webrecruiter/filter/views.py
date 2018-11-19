from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View
from .models import FilterPosition

from jobapply.utils import render_to_pdf  # created in step 4
from django.shortcuts import render_to_response
from django.template import RequestContext

from jobapply.models import CandidateBasic,CandidateHistoryEducation,CandidateComputerSkill,CandidateLanguageSkill,CandidateCertExperience,CandidateAttachment,CandidateWorkExperience,EducationLevel,Institute,Country,Skill,SkillType

from django.db.models import Q

# Import For Authenticate Account
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from candidate_cart.models import OrderItem, Order
from account.models import Profile
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

import os
from django.conf import settings
from django.template.loader import render_to_string


def get_cart_amount(request):
    user = User.objects.filter(username=request.user.username)

    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    cart_amount = 0
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        cart_amount = user_order_items.count()
    return cart_amount

# Create your views here.
def index(request):
    if request.method == 'POST':
        filter_option = request.POST.getlist('filter_option')

        operator_position = request.POST.getlist('operator_position')
        filter_position = request.POST.getlist('filter_position')

        operator_salary = request.POST.getlist('operator_salary')
        filter_salary = request.POST.getlist('filter_salary')

        operator_gender = request.POST.getlist('operator_gender')
        filter_gender = request.POST.getlist('filter_gender')

        operator_gpa = request.POST.getlist('operator_gpa')
        filter_gpa = request.POST.getlist('filter_gpa')

        operator_status = request.POST.getlist('operator_status')
        filter_status = request.POST.getlist('filter_status')

        operator_edu = request.POST.getlist('operator_edu')

        operator_nationality = request.POST.getlist('operator_nationality')
        filter_nationality = request.POST.getlist('filter_nationality')

        operator_major = request.POST.getlist('operator_major')
        filter_major = request.POST.getlist('filter_major')

        operator_comskill = request.POST.getlist('operator_comskill')
        filter_comskill = []

        print("COMSKILL")
        print("OPERATOR : ",operator_comskill,len(operator_comskill))
        # วน loop เก็บ filter skill
        skill_list = []
        for i in range(1,len(operator_comskill)+1):
            txt = request.POST['tags'+str(i)].replace("\",\"","NaTeChA").replace("[\"","").replace("\"]","")
            skill_list = txt.split("NaTeChA")
            # print(len(skill_list),"+++++++++++++++")

            check_filter = []
            for j in range(0,len(skill_list)):
                # print(j,"This is JJJ!!!")
                if not skill_list[j]=='':
                    # print(skill_list,"___________________________")
                    check_filter.append(skill_list[j])
            if check_filter:
                filter_comskill.append(check_filter)
            else:
                filter_comskill.append('')
        print("TAG : ",filter_comskill,len(filter_comskill))
        print(operator_comskill,"++++++++++++")

        print("Filter List : " + str(filter_option) + "Operator Position : "+ str(operator_position) + " Position : " + str(filter_position))
        position = FilterPosition(operator_position=operator_position,filter_position=filter_position)
        position.save()

        all_candidate = CandidateBasic.objects.all()
        print("!!!!!!!!!!!!!!",all_candidate)
        print("Len Filter : " + str(len(filter_option)))
        # If Filter List is NOT EMPTY
        if filter_option :
            print("len :" + str(len(operator_position)))
            # Filter Position  { Active When OPERATOR POSITION is not emply }
            if operator_position:
                print("Entry Position")
                checkbox_position_set=CandidateBasic.objects.all()
                # before = CandidateBasic.objects.all()
                for i in range(0,len(operator_position)):
                    if filter_position[i]=='':
                        pass
                    else :
                        if (operator_position[i]=='1'):
                            # filter_query = CandidateBasic.objects.filter(position__iexact=filter_position[i]).values_list()
                            # before_list = before.values_list()
                            # print("filter_query",filter_query)
                            # print("before_list",before_list)

                            checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(position__iexact=filter_position[i]))
                        if (operator_position[i]=='2'):
                            checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(~Q(position__iexact=filter_position[i])))
                        if (operator_position[i]=='3'):
                            checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(position__icontains=filter_position[i]))
                            print(str(i) + ":Selected Candidate :" + str(checkbox_position_set))
                        if (operator_position[i]=='4'):
                            checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(~Q(position__icontains=filter_position[i])))
                all_candidate = all_candidate.intersection(checkbox_position_set)
                print(all_candidate)

            # Filter Salary  { Active When OPERATOR SALARY is not emply }
            if operator_salary:
                print("Entry Salary")
                checkbox_salary_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_salary)):
                    if filter_salary[i]=='':
                        pass
                    else :
                        if (operator_salary[i]=='1'):
                            checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary=filter_salary[i]))
                        elif (operator_salary[i]=='2'):
                            checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary__gte=filter_salary[i]))
                        elif (operator_salary[i]=='3'):
                            checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary__lte=filter_salary[i]))
                        elif (operator_salary[i]=='4'):
                            checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary__gt=filter_salary[i]))
                        elif (operator_salary[i]=='5'):
                            checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary__lt=filter_salary[i]))
                all_candidate = all_candidate.intersection(checkbox_salary_set)

            # Filter Gender  { Active When OPERATOR GENDER is not emply }
            if operator_gender:
                print("Entry Gender")
                print("Operator : " + str(operator_gender) + "filter_gpa : " + str(filter_gender))
                checkbox_gender_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_gender)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_gender)))
                    if filter_gender[i]=='':
                        pass
                    else :
                        if (operator_gender[i]=='1'):
                            if (filter_gender[i]=='m'):
                                checkbox_gender_set = checkbox_gender_set.intersection(CandidateBasic.objects.filter(name_title="นาย"))
                            else:
                                checkbox_gender_set = checkbox_gender_set.intersection(CandidateBasic.objects.filter(~Q(name_title="นาย")))
                        elif (operator_gender[i]=='2'):
                            if (filter_gender[i]=='m'):
                                checkbox_gender_set = checkbox_gender_set.intersection(CandidateBasic.objects.filter(~Q(name_title="นาย")))
                            else:
                                checkbox_gender_set = checkbox_gender_set.intersection(CandidateBasic.objects.filter(name_title="นาย"))
                all_candidate = all_candidate.intersection(checkbox_gender_set)

            # Filter GPA  { Active When OPERATOR GPA is not emply }
            if operator_gpa:
                print("Entry GPA")
                print("Operator : " + str(operator_gpa) + "filter_gpa : " + str(filter_gpa))
                checkbox_gpa_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_gpa)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_gpa)))
                    if filter_gpa[i]=='':
                        pass
                    else :
                        if (operator_gpa[i]=='1'):
                            checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa=filter_gpa[i]))
                        elif (operator_gpa[i]=='2'):
                            checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa__gte=filter_gpa[i]))
                        elif (operator_gpa[i]=='3'):
                            checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa__lte=filter_gpa[i]))
                        elif (operator_gpa[i]=='4'):
                            checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa__gt=filter_gpa[i]))
                        elif (operator_gpa[i]=='5'):
                            checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa__lt=filter_gpa[i]))
                all_candidate = all_candidate.intersection(checkbox_gpa_set)

            # Filter Status  { Active When OPERATOR STATUS is not emply }
            if operator_status:
                print("Entry Status")
                print("Operator : " + str(operator_status) + "filter_status : " + str(filter_status))
                checkbox_status_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_status)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_status)))
                    if filter_status[i]=='':
                        pass
                    else :
                        if (operator_status[i]=='1'):
                            checkbox_status_set = checkbox_status_set.intersection(CandidateBasic.objects.filter(status=filter_status[i]))
                        elif (operator_status[i]=='2'):
                            checkbox_status_set = checkbox_status_set.intersection(CandidateBasic.objects.filter(~Q(status=filter_status[i])))
                all_candidate = all_candidate.intersection(checkbox_status_set)

            # Filter Edu  { Active When OPERATOR EDU is not emply }
            if operator_edu:
                print("Entry edu")
                print("Operator : " + str(operator_edu))
                checkbox_edu_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_edu)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_edu)))
                    if (operator_edu[i]=='1'):
                        checkbox_edu_set = checkbox_edu_set.intersection(CandidateBasic.objects.filter(check_study="isStudy_yes"))
                        print("Check Study : "+str((CandidateBasic.objects.filter(check_study="isStudy_yes"))))
                    elif (operator_edu[i]=='2'):
                        checkbox_edu_set = checkbox_edu_set.intersection(CandidateBasic.objects.filter(check_study="isStudy_no"))
                        print("Check Study : "+str((CandidateBasic.objects.filter(check_study="isStudy_no"))))
                all_candidate = all_candidate.intersection(checkbox_edu_set)

            # Filter Nationality  { Active When OPERATOR Nationality is not emply }
            if operator_nationality:
                print("Entry Nationality")
                print("Operator : " + str(operator_nationality) + "filter_nationality : " + str(filter_nationality))
                checkbox_nationality_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_nationality)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_gpa)))
                    if filter_nationality[i]=='':
                        pass
                    else :
                        if (operator_nationality[i]=='1'):
                            checkbox_nationality_set = checkbox_nationality_set.intersection(CandidateBasic.objects.filter(nationality__iexact=filter_nationality[i]))
                        elif (operator_nationality[i]=='2'):
                            checkbox_nationality_set = checkbox_nationality_set.intersection(CandidateBasic.objects.filter(~Q(nationality__iexact=filter_nationality[i])))
                        elif (operator_nationality[i]=='3'):
                            checkbox_nationality_set = checkbox_nationality_set.intersection(CandidateBasic.objects.filter(nationality__icontains=filter_nationality[i]))
                        elif (operator_nationality[i]=='4'):
                            checkbox_nationality_set = checkbox_nationality_set.intersection(CandidateBasic.objects.filter(~Q(nationality__icontains=filter_nationality[i])))
                all_candidate = all_candidate.intersection(checkbox_nationality_set)

            # Filter Major  { Active When OPERATOR Major is not emply }
            if operator_major:
                print("Entry Major")
                print("Operator : " + str(operator_major) + "filter_major : " + str(filter_major))
                checkbox_major_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_major)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_major)))
                    if filter_major[i]=='':
                        pass
                    else :
                        if (operator_major[i]=='1'):
                            checkbox_major_set = checkbox_major_set.intersection(CandidateBasic.objects.filter(nowEdu_major__iexact=filter_major[i]))
                        elif (operator_major[i]=='2'):
                            checkbox_major_set = checkbox_major_set.intersection(CandidateBasic.objects.filter(~Q(nowEdu_major__iexact=filter_major[i])))
                        elif (operator_major[i]=='3'):
                            checkbox_major_set = checkbox_major_set.intersection(CandidateBasic.objects.filter(nowEdu_major__icontains=filter_major[i]))
                        elif (operator_major[i]=='4'):
                            checkbox_major_set = checkbox_major_set.intersection(CandidateBasic.objects.filter(~Q(nowEdu_major__icontains=filter_major[i])))
                all_candidate = all_candidate.intersection(checkbox_major_set)

            # Filter COMSKILL  { Active When OPERATOR COMSKILL is not emply }
            # print("All Candidate ก่อนเข้า Filter Comskill : ", all_candidate)
            if filter_comskill:
                print("Entry Comskill")
                for i in range(0,len(operator_comskill)):
                    if operator_comskill[i] != '0':
                        if filter_comskill[i]:
                            print(operator_comskill[i])
                            if operator_comskill[i]=='1' or operator_comskill[i]=='2':
                                checkbox_comskill_set=CandidateBasic.objects.all()
                                print("Entry condition 1")
                            elif operator_comskill[i]=='3' or operator_comskill[i]=='4':
                                checkbox_comskill_set=CandidateBasic.objects.none()
                                print("Entry condition 2")
                            print("start! ",checkbox_comskill_set,operator_comskill[i])
                            for j in range(0,len(filter_comskill[i])):
                                print(operator_comskill[i],filter_comskill[i][j])
                                if (operator_comskill[i]=='1'):
                                    checkbox_comskill_set = checkbox_comskill_set.intersection(CandidateBasic.objects.filter(candidate_computer_skill__tags__icontains=filter_comskill[i][j]))
                                if (operator_comskill[i]=='2'):
                                    checkbox_comskill_set = checkbox_comskill_set.intersection(CandidateBasic.objects.filter(~Q(candidate_computer_skill__tags__icontains=filter_comskill[i][j])))
                                if (operator_comskill[i]=='3'):
                                    checkbox_comskill_set = checkbox_comskill_set.union(CandidateBasic.objects.filter(candidate_computer_skill__tags__icontains=filter_comskill[i][j]))
                                if (operator_comskill[i]=='4'):
                                    checkbox_comskill_set = checkbox_comskill_set.union(CandidateBasic.objects.filter(~Q(candidate_computer_skill__tags__icontains=filter_comskill[i][j])))
                                print(j,checkbox_comskill_set)
                            all_candidate = checkbox_comskill_set.intersection(all_candidate)
                            print("All Candidate หลังเข้า Filter Comskill : ",i, all_candidate)


        list_skill_name =	[]
        skill_name = Skill.objects.all().values_list('skill_name',flat=True)
        for skill in skill_name:
            list_skill_name.append(skill)
        print("SKILL NAME 2! ______",list_skill_name)
        print(all_candidate)
        cart_amount = get_cart_amount(request)
        context = {
            'Candidate': all_candidate,
            'Cart_amount':cart_amount,
            'Skill' : list_skill_name,
        }
        template = loader.get_template("filter_candidate.html")
        return HttpResponse(template.render(context, request))

    if request.user.is_authenticated:
        skill = Skill.objects.all().values_list('skill_name',flat=True)
        skill_json = json.dumps(list(skill), cls=DjangoJSONEncoder)
        print(skill_json)

        # list_skill_name =	[]
        # skill_name = Skill.objects.all().values_list('skill_name',flat=True)
        # for skill in skill_name:
        #     list_skill_name.append(skill)
        # print("SKILL NAME! ______",list_skill_name)
        all_candidate = CandidateBasic.objects.all()
        cart_amount = get_cart_amount(request)

        return render(request, "filter_candidate.html", {'Candidate': all_candidate,'Cart_amount':cart_amount,"Skill_json":skill_json})
    else:
        return redirect('login')


def candidate_detail(request,candidate_id):
    if request.user.is_authenticated:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        cart_amount = get_cart_amount(request)

        selected_candidate = get_object_or_404(CandidateBasic, id_number=candidate_id)

        txt_skill = selected_candidate.candidate_computer_skill.tags.replace("\",\"","NaTeChA").replace("[\"","").replace("\"]","")
        list_skill = txt_skill.split("NaTeChA")

        work_experience = CandidateWorkExperience.objects.filter(owner=selected_candidate)
        cert_experience = CandidateCertExperience.objects.filter(owner=selected_candidate)
        skill_language = CandidateLanguageSkill.objects.filter(owner=selected_candidate)
        attachment = CandidateAttachment.objects.filter(candidate_basic=selected_candidate).first()
        print("ATTACHMENT !!! : " , attachment)
        history_education = CandidateHistoryEducation.objects.filter(owner=selected_candidate)

        if not history_education.exists():
            history_education = CandidateHistoryEducation.objects.none()
        print("History Amount : ",history_education)

        print(list_skill)
        return render(request,
                      'candidate_detail.html',
                      {'Candidate_id': candidate_id,
                       'Selected_candidate' : selected_candidate,
                       'Cart_amount' : cart_amount,
                       'Skills' : list_skill,
                       'HistoryEducation' : history_education,
                       'SkillLanguage' : skill_language,
                       'Attachment' : attachment,
                       'CertExperience' : cert_experience,
                       'WorkExperience' : work_experience,
                       })
    else:
        return redirect('login')

def intersection_queryset(before,filter):
    before_list = set(before.values_list('id_number',flat=True))
    filter_query = set(filter.values_list('id_number',flat=True))
    print("filter_query",filter_query)
    print("before_list",before_list)
    intersection_query = list(before_list.intersection(filter_query))
    print("intersection",intersection_query)
    result = CandidateBasic.objects.filter(id_number__in=intersection_query)
    return result

def query_age(operator,age):
    print("!!!!!!!!!!!!!!!!!!")
    all_candidate = CandidateBasic.objects.all()
    result = []
    if (operator=='1'):
        for candidate in all_candidate:
            print("AGE : ",candidate.calculate_age() )
            if candidate.calculate_age() == int(age):
                result.append(candidate.id_number)
    elif (operator=='2'):
        for candidate in all_candidate:
            print("AGE : ",candidate.calculate_age() )
            if candidate.calculate_age() >= int(age):
                result.append(candidate.id_number)
    elif (operator=='3'):
        for candidate in all_candidate:
            print("AGE : ",candidate.calculate_age() )
            if candidate.calculate_age() <= int(age):
                result.append(candidate.id_number)
    elif (operator=='4'):
        for candidate in all_candidate:
            print("AGE : ",candidate.calculate_age() )
            if candidate.calculate_age() > int(age):
                result.append(candidate.id_number)
    elif (operator=='5'):
        for candidate in all_candidate:
            print("AGE : ",candidate.calculate_age() )
            if candidate.calculate_age() < int(age):
                result.append(candidate.id_number)
    result_candidate = CandidateBasic.objects.filter(id_number__in=result)
    return result_candidate

def test_ajax(request):
    if request.method == 'POST':
        print("Entryy")
        filter_option = json.loads(request.POST.get('filter_option'))

        operator_position = json.loads(request.POST.get('operator_position'))
        filter_position = json.loads(request.POST.get('filter_position'))

        operator_salary = json.loads(request.POST.get('operator_salary'))
        filter_salary = json.loads(request.POST.get('filter_salary'))

        operator_gender = json.loads(request.POST.get('operator_gender'))
        filter_gender = json.loads(request.POST.get('filter_gender'))

        operator_gpa = json.loads(request.POST.get('operator_gpa'))
        filter_gpa = json.loads(request.POST.get('filter_gpa'))

        operator_status = json.loads(request.POST.get('operator_status'))
        filter_status = json.loads(request.POST.get('filter_status'))

        operator_edu = json.loads(request.POST.get('operator_edu'))

        operator_nationality = json.loads(request.POST.get('operator_nationality'))
        filter_nationality = json.loads(request.POST.get('filter_nationality'))

        operator_major = json.loads(request.POST.get('operator_major'))
        filter_major = json.loads(request.POST.get('filter_major'))

        operator_comskill = json.loads(request.POST.get('operator_comskill'))
        filter_comskill_txt = json.loads(request.POST.get('filter_comskill'))

        operator_language = json.loads(request.POST.get('operator_language'))
        filter_language = json.loads(request.POST.get('filter_language'))

        operator_university = json.loads(request.POST.get('operator_university'))
        filter_university = json.loads(request.POST.get('filter_university'))

        operator_age = json.loads(request.POST.get('operator_age'))
        filter_age = json.loads(request.POST.get('filter_age'))

        operator_experience = json.loads(request.POST.get('operator_experience'))
        filter_experience = json.loads(request.POST.get('filter_experience'))

        operator_workexp = json.loads(request.POST.get('operator_workexp'))
        filter_workexp = json.loads(request.POST.get('filter_workexp'))

        # วน loop เก็บ filter skill
        filter_comskill = []
        for comskill_set in filter_comskill_txt:
            txt = comskill_set.replace("\",\"","NaTeChA").replace("[\"","").replace("\"]","")
            skill_list = txt.split("NaTeChA")
            print(len(skill_list),"+++++++++++++++")

            check_comskill = []
            for j in range(0,len(skill_list)):
                # print(j,"This is JJJ!!!")
                if not skill_list[j]=='':
                    # print(skill_list,"___________________________")
                    check_comskill.append(skill_list[j])
            if check_comskill:
                filter_comskill.append(check_comskill)
            else:
                filter_comskill.append('')




        print("filter_option",filter_option)
        print("operator_position",operator_position)
        print("filter_position",filter_position)
        print("operator_salary",operator_salary)
        print("filter_salary",filter_salary)
        print("operator_gender",operator_gender)
        print("filter_gender",filter_gender)
        print("operator_gpa",operator_gpa)
        print("filter_gpa",filter_gpa)
        print("operator_status",operator_status)
        print("filter_status",filter_status)
        print("operator_edu",operator_edu)
        print("operator_nationality",operator_nationality)
        print("filter_nationality",filter_nationality)
        print("operator_major",operator_major)
        print("filter_major",filter_major)
        print("operator_comskill",operator_comskill)
        print("filter_comskill",filter_comskill,filter_comskill_txt)
        print("operator_language",operator_language)
        print("filter_language",filter_language)
        print("operator_university",operator_university)
        print("filter_university",filter_university)
        print("operator_age",operator_age)
        print("filter_age",filter_age)
        print("operator_experience",operator_experience)
        print("filter_experience",filter_experience)
        print("operator_workexp",operator_workexp)
        print("filter_workexp",filter_workexp)

        all_candidate = CandidateBasic.objects.all()
        print("Len Filter : " + str(len(filter_option)))
        # If Filter List is NOT EMPTY
        if filter_option :
            print("len :" + str(len(operator_position)))
            # Filter Position  { Active When OPERATOR POSITION is not emply }
            if operator_position:
                print("Entry Position")
                checkbox_position_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_position)):
                    if filter_position[i]=='' or operator_position[i]==None:
                        pass
                    else :
                        if (operator_position[i]=='1'):
                            checkbox_position_set = intersection_queryset(checkbox_position_set,CandidateBasic.objects.filter(position__iexact=filter_position[i]))
                            print("QUERYYYYYYY!!!!!!",checkbox_position_set)
                            # checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(position__iexact=filter_position[i]))
                        if (operator_position[i]=='2'):
                            checkbox_position_set = intersection_queryset(checkbox_position_set,CandidateBasic.objects.filter(~Q(position__iexact=filter_position[i])))
                            # checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(~Q(position__iexact=filter_position[i])))
                        if (operator_position[i]=='3'):
                            checkbox_position_set = intersection_queryset(checkbox_position_set,CandidateBasic.objects.filter(position__icontains=filter_position[i]))
                            # checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(position__icontains=filter_position[i]))
                            print(str(i) + ":Selected Candidate :" + str(checkbox_position_set))
                        if (operator_position[i]=='4'):
                            checkbox_position_set = intersection_queryset(checkbox_position_set,CandidateBasic.objects.filter(~Q(position__icontains=filter_position[i])))
                            # checkbox_position_set = checkbox_position_set.intersection(CandidateBasic.objects.filter(~Q(position__icontains=filter_position[i])))
                print("FINSIDHHHHHH",checkbox_position_set)
                all_candidate = intersection_queryset(all_candidate,checkbox_position_set)
                print("all_candidate!!!!!!!!!!!",all_candidate)
                # all_candidate = all_candidate.intersection(checkbox_position_set)
            # Filter Salary  { Active When OPERATOR SALARY is not emply }
            if operator_salary:
                print("Entry Salary")
                checkbox_salary_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_salary)):
                    if filter_salary[i]=='' or operator_salary[i]==None:
                        pass
                    else :
                        if (operator_salary[i]=='1'):
                            checkbox_salary_set = intersection_queryset(checkbox_salary_set,CandidateBasic.objects.filter(salary=filter_salary[i]))
                            # checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary=filter_salary[i]))
                        elif (operator_salary[i]=='2'):
                            checkbox_salary_set = intersection_queryset(checkbox_salary_set,CandidateBasic.objects.filter(salary__gte=filter_salary[i]))
                            # checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary__gte=filter_salary[i]))
                        elif (operator_salary[i]=='3'):
                            checkbox_salary_set = intersection_queryset(checkbox_salary_set,CandidateBasic.objects.filter(salary__lte=filter_salary[i]))
                            # checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary__lte=filter_salary[i]))
                        elif (operator_salary[i]=='4'):
                            checkbox_salary_set = intersection_queryset(checkbox_salary_set,CandidateBasic.objects.filter(salary__gt=filter_salary[i]))
                            # checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary__gt=filter_salary[i]))
                        elif (operator_salary[i]=='5'):
                            checkbox_salary_set = intersection_queryset(checkbox_salary_set,CandidateBasic.objects.filter(salary__lt=filter_salary[i]))
                            # checkbox_salary_set = checkbox_salary_set.intersection(CandidateBasic.objects.filter(salary__lt=filter_salary[i]))
                all_candidate = intersection_queryset(all_candidate,checkbox_salary_set)
                # all_candidate = all_candidate.intersection(checkbox_salary_set)
            print("all_candidate222!!!!!!!!!!!",all_candidate)
            # Filter Gender  { Active When OPERATOR GENDER is not emply }
            if operator_gender:
                print("Entry Gender")
                print("Operator : " + str(operator_gender) + "filter_gpa : " + str(filter_gender))
                checkbox_gender_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_gender)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_gender)))
                    if filter_gender[i]=='' or operator_gender[i]==None:
                        pass
                    else :
                        if (operator_gender[i]=='1'):
                            if (filter_gender[i]=='m'):
                                checkbox_gender_set = intersection_queryset(checkbox_gender_set,CandidateBasic.objects.filter(name_title="นาย"))
                                # checkbox_gender_set = checkbox_gender_set.intersection(CandidateBasic.objects.filter(name_title="นาย"))
                            elif (filter_gender[i]=='w'):
                                checkbox_gender_set = intersection_queryset(checkbox_gender_set,CandidateBasic.objects.filter(~Q(name_title="นาย")))
                                # checkbox_gender_set = checkbox_gender_set.intersection(CandidateBasic.objects.filter(~Q(name_title="นาย")))
                        elif (operator_gender[i]=='2'):
                            if (filter_gender[i]=='m'):
                                checkbox_gender_set = intersection_queryset(checkbox_gender_set,CandidateBasic.objects.filter(~Q(name_title="นาย")))
                                # checkbox_gender_set = checkbox_gender_set.intersection(CandidateBasic.objects.filter(~Q(name_title="นาย")))
                            elif (filter_gender[i]=='w'):
                                checkbox_gender_set = intersection_queryset(checkbox_gender_set,CandidateBasic.objects.filter(name_title="นาย"))
                                # checkbox_gender_set = checkbox_gender_set.intersection(CandidateBasic.objects.filter(name_title="นาย"))
                all_candidate = intersection_queryset(all_candidate,checkbox_gender_set)
                print("all_candidate333!!!!!!!!!!!",all_candidate)
                # all_candidate = all_candidate.intersection(checkbox_gender_set)

            # Filter GPA  { Active When OPERATOR GPA is not emply }
            if operator_gpa:
                print("Entry GPA")
                print("Operator : " + str(operator_gpa) + "filter_gpa : " + str(filter_gpa))
                checkbox_gpa_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_gpa)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_gpa)))
                    if filter_gpa[i]=='' or operator_gpa[i]==None:
                        pass
                    else :
                        if (operator_gpa[i]=='1'):
                            checkbox_gpa_set = intersection_queryset(checkbox_gpa_set,CandidateBasic.objects.filter(nowEdu_gpa=filter_gpa[i]))
                            # checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa=filter_gpa[i]))
                        elif (operator_gpa[i]=='2'):
                            checkbox_gpa_set = intersection_queryset(checkbox_gpa_set,CandidateBasic.objects.filter(nowEdu_gpa__gte=filter_gpa[i]))
                            # checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa__gte=filter_gpa[i]))
                        elif (operator_gpa[i]=='3'):
                            checkbox_gpa_set = intersection_queryset(checkbox_gpa_set,CandidateBasic.objects.filter(nowEdu_gpa__lte=filter_gpa[i]))
                            # checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa__lte=filter_gpa[i]))
                        elif (operator_gpa[i]=='4'):
                            checkbox_gpa_set = intersection_queryset(checkbox_gpa_set,CandidateBasic.objects.filter(nowEdu_gpa__gt=filter_gpa[i]))
                            # checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa__gt=filter_gpa[i]))
                        elif (operator_gpa[i]=='5'):
                            checkbox_gpa_set = intersection_queryset(checkbox_gpa_set,CandidateBasic.objects.filter(nowEdu_gpa__lt=filter_gpa[i]))
                            # checkbox_gpa_set = checkbox_gpa_set.intersection(CandidateBasic.objects.filter(nowEdu_gpa__lt=filter_gpa[i]))
                all_candidate = intersection_queryset(all_candidate,checkbox_gpa_set)
                print("all_candidate444!!!!!!!!!!!",all_candidate)
                # all_candidate = all_candidate.intersection(checkbox_gpa_set)

            # Filter Status  { Active When OPERATOR STATUS is not emply }
            if operator_status:
                print("Entry Status")
                print("Operator : " + str(operator_status) + "filter_status : " + str(filter_status))
                checkbox_status_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_status)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_status)))
                    if filter_status[i]=='' or operator_status[i]==None:
                        pass
                    else :
                        if (operator_status[i]=='1'):
                            checkbox_status_set = intersection_queryset(checkbox_status_set,CandidateBasic.objects.filter(status=filter_status[i]))
                            # checkbox_status_set = checkbox_status_set.intersection(CandidateBasic.objects.filter(status=filter_status[i]))
                        elif (operator_status[i]=='2'):
                            checkbox_status_set = intersection_queryset(checkbox_status_set,CandidateBasic.objects.filter(~Q(status=filter_status[i])))
                            # checkbox_status_set = checkbox_status_set.intersection(CandidateBasic.objects.filter(~Q(status=filter_status[i])))
                all_candidate = intersection_queryset(all_candidate,checkbox_status_set)
                print("all_candidate555!!!!!!!!!!!",all_candidate)
                # all_candidate = all_candidate.intersection(checkbox_status_set)

            # Filter Edu  { Active When OPERATOR EDU is not emply }
            if operator_edu:
                print("Entry edu")
                print("Operator : " + str(operator_edu))
                checkbox_edu_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_edu)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_edu)))
                    if (operator_edu[i]=='1'):
                        checkbox_edu_set = intersection_queryset(checkbox_edu_set,CandidateBasic.objects.filter(check_study="isStudy_yes"))
                        # checkbox_edu_set = checkbox_edu_set.intersection(CandidateBasic.objects.filter(check_study="isStudy_yes"))
                        print("Check Study : "+str((CandidateBasic.objects.filter(check_study="isStudy_yes"))))
                    elif (operator_edu[i]=='2'):
                        checkbox_edu_set = intersection_queryset(checkbox_edu_set,CandidateBasic.objects.filter(check_study="isStudy_no"))
                        # checkbox_edu_set = checkbox_edu_set.intersection(CandidateBasic.objects.filter(check_study="isStudy_no"))
                        print("Check Study : "+str((CandidateBasic.objects.filter(check_study="isStudy_no"))))
                # all_candidate = all_candidate.intersection(checkbox_edu_set)
                all_candidate = intersection_queryset(all_candidate,checkbox_edu_set)
                print("all_candidate666!!!!!!!!!!!",all_candidate)

            # Filter Nationality  { Active When OPERATOR Nationality is not emply }
            if operator_nationality:
                print("Entry Nationality")
                print("Operator : " + str(operator_nationality) + "filter_nationality : " + str(filter_nationality))
                checkbox_nationality_set=CandidateBasic.objects.all()
                for i in range(0,len(operator_nationality)):
                    print("I : "+str(i) + "   Len : " + str(len(operator_gpa)))
                    if filter_nationality[i]=='' or operator_nationality[i]==None:
                        pass
                    else :
                        if (operator_nationality[i]=='1'):
                            checkbox_nationality_set = intersection_queryset(checkbox_nationality_set,CandidateBasic.objects.filter(nationality__iexact=filter_nationality[i]))
                            # checkbox_nationality_set = checkbox_nationality_set.intersection(CandidateBasic.objects.filter(nationality__iexact=filter_nationality[i]))
                        elif (operator_nationality[i]=='2'):
                            checkbox_nationality_set = intersection_queryset(checkbox_nationality_set,CandidateBasic.objects.filter(~Q(nationality__iexact=filter_nationality[i])))
                            # checkbox_nationality_set = checkbox_nationality_set.intersection(CandidateBasic.objects.filter(~Q(nationality__iexact=filter_nationality[i])))
                        elif (operator_nationality[i]=='3'):
                            checkbox_nationality_set = intersection_queryset(checkbox_nationality_set,CandidateBasic.objects.filter(nationality__icontains=filter_nationality[i]))
                            # checkbox_nationality_set = checkbox_nationality_set.intersection(CandidateBasic.objects.filter(nationality__icontains=filter_nationality[i]))
                        elif (operator_nationality[i]=='4'):
                            checkbox_nationality_set = intersection_queryset(checkbox_nationality_set,CandidateBasic.objects.filter(~Q(nationality__icontains=filter_nationality[i])))
                            # checkbox_nationality_set = checkbox_nationality_set.intersection(CandidateBasic.objects.filter(~Q(nationality__icontains=filter_nationality[i])))
                # all_candidate = all_candidate.intersection(checkbox_nationality_set)
                all_candidate = intersection_queryset(all_candidate,checkbox_nationality_set)
                print("all_candidate777!!!!!!!!!!!",all_candidate)

                # Filter Major  { Active When OPERATOR Major is not emply }
                if operator_major:
                    print("Entry Major")
                    print("Operator : " + str(operator_major) + "filter_major : " + str(filter_major))
                    checkbox_major_set=CandidateBasic.objects.all()
                    for i in range(0,len(operator_major)):
                        print("I : "+str(i) + "   Len : " + str(len(operator_major)))
                        if filter_major[i]=='' or operator_major[i]==None:
                            pass
                        else :
                            if (operator_major[i]=='1'):
                                checkbox_major_set = intersection_queryset(checkbox_major_set,CandidateBasic.objects.filter(nowEdu_major__iexact=filter_major[i]))
                                # checkbox_major_set = checkbox_major_set.intersection(CandidateBasic.objects.filter(nowEdu_major__iexact=filter_major[i]))
                            elif (operator_major[i]=='2'):
                                checkbox_major_set = intersection_queryset(checkbox_major_set,CandidateBasic.objects.filter(~Q(nowEdu_major__iexact=filter_major[i])))
                                # checkbox_major_set = checkbox_major_set.intersection(CandidateBasic.objects.filter(~Q(nowEdu_major__iexact=filter_major[i])))
                            elif (operator_major[i]=='3'):
                                checkbox_major_set = intersection_queryset(checkbox_major_set,CandidateBasic.objects.filter(nowEdu_major__icontains=filter_major[i]))
                                # checkbox_major_set = checkbox_major_set.intersection(CandidateBasic.objects.filter(nowEdu_major__icontains=filter_major[i]))
                            elif (operator_major[i]=='4'):
                                checkbox_major_set = intersection_queryset(checkbox_major_set,CandidateBasic.objects.filter(~Q(nowEdu_major__icontains=filter_major[i])))
                                # checkbox_major_set = checkbox_major_set.intersection(CandidateBasic.objects.filter(~Q(nowEdu_major__icontains=filter_major[i])))
                    # all_candidate = all_candidate.intersection(checkbox_major_set)
                    all_candidate = intersection_queryset(all_candidate,checkbox_major_set)
                    print("all_candidate888!!!!!!!!!!!",all_candidate)

                # Filter COMSKILL  { Active When OPERATOR COMSKILL is not emply }
                print("All Candidate ก่อนเข้า Filter Comskill : ", all_candidate)
                if filter_comskill:
                    print("Entry Comskill")
                    for i in range(0,len(operator_comskill)):
                        print(operator_comskill[i],None,operator_comskill[i] != None)
                        if operator_comskill[i] != '0' and operator_comskill[i] != None:
                            if filter_comskill[i]:
                                print(operator_comskill[i],'_____')
                                if operator_comskill[i]=='1' or operator_comskill[i]=='2':
                                    checkbox_comskill_set=CandidateBasic.objects.all()
                                    print("Entry condition 1")
                                elif operator_comskill[i]=='3' or operator_comskill[i]=='4':
                                    checkbox_comskill_set=CandidateBasic.objects.none()
                                    print("Entry condition 2")
                                print("start! ",checkbox_comskill_set,operator_comskill[i])
                                for j in range(0,len(filter_comskill[i])):
                                    print(operator_comskill[i],filter_comskill[i][j])
                                    if filter_comskill[i][j] != '[]':
                                        if (operator_comskill[i]=='1'):
                                            checkbox_comskill_set = intersection_queryset(checkbox_comskill_set,CandidateBasic.objects.filter(candidate_computer_skill__tags__icontains=filter_comskill[i][j]))
                                            # checkbox_comskill_set = checkbox_comskill_set.intersection(CandidateBasic.objects.filter(candidate_computer_skill__tags__icontains=filter_comskill[i][j]))
                                        if (operator_comskill[i]=='2'):
                                            checkbox_comskill_set = intersection_queryset(checkbox_comskill_set,CandidateBasic.objects.filter(~Q(candidate_computer_skill__tags__icontains=filter_comskill[i][j])))
                                            # checkbox_comskill_set = checkbox_comskill_set.intersection(CandidateBasic.objects.filter(~Q(candidate_computer_skill__tags__icontains=filter_comskill[i][j])))
                                        if (operator_comskill[i]=='3'):
                                            checkbox_comskill_set = checkbox_comskill_set.union(CandidateBasic.objects.filter(candidate_computer_skill__tags__icontains=filter_comskill[i][j]))
                                        if (operator_comskill[i]=='4'):
                                            checkbox_comskill_set = checkbox_comskill_set.union(CandidateBasic.objects.filter(~Q(candidate_computer_skill__tags__icontains=filter_comskill[i][j])))
                                        print(j,checkbox_comskill_set)
                                # all_candidate = checkbox_comskill_set.intersection(all_candidate)
                                all_candidate = intersection_queryset(all_candidate,checkbox_comskill_set)
                                print("all_candidate999!!!!!!!!!!!",all_candidate)
                                print("All Candidate หลังเข้า Filter Comskill : ",i, all_candidate)

                # Filter Language  { Active When OPERATOR GENDER is not emply }
                if operator_language:
                    print("Entry Language")
                    print("Operator : " + str(operator_language) + "filter_gpa : " + str(filter_language))
                    checkbox_language_set=CandidateBasic.objects.all()
                    for i in range(0,len(operator_language)):
                        language_set = CandidateLanguageSkill.objects.none()
                        print("I : "+str(i) + "   Len : " + str(len(operator_language)))
                        if filter_language[i]=='' or operator_language[i]==None:
                            pass
                        else :
                            print(operator_language[i],"______")
                            if (operator_language[i]=='1'):
                                language_set = CandidateLanguageSkill.objects.filter(skill_language=filter_language[i])
                                candidate_set = CandidateBasic.objects.none()
                                for candidate in language_set:
                                    candidate_set = candidate_set.union(CandidateBasic.objects.filter(id_number=candidate.owner.id_number))
                                checkbox_language_set = intersection_queryset(checkbox_language_set,candidate_set)
                                # checkbox_language_set = checkbox_language_set.intersection(candidate_set)
                            elif (operator_language[i]=='2'):
                                block_candidate = CandidateLanguageSkill.objects.filter(Q(skill_language=filter_language[i])).values_list('owner',flat=True)
                                candidate_set = CandidateBasic.objects.filter(~Q(id_number__in=block_candidate))
                                checkbox_language_set = intersection_queryset(checkbox_language_set,candidate_set)
                                # checkbox_language_set = checkbox_language_set.intersection(candidate_set)
                    print(i,"checkbox_language_set",checkbox_language_set)
                    # all_candidate = all_candidate.intersection(checkbox_language_set)
                    all_candidate = intersection_queryset(all_candidate,checkbox_language_set)
                    print("all_candidate10 10 10!!!!!!!!!!!",all_candidate)

                # Filter University  { Active When OPERATOR University is not emply }
                if operator_university:
                    print("Entry University")
                    print("Operator : " + str(operator_university) + "filter_university : " + str(filter_university))
                    checkbox_university_set=CandidateBasic.objects.all()
                    for i in range(0,len(operator_university)):
                        print("I : "+str(i) + "   Len : " + str(len(operator_university)))
                        if filter_university[i]=='' or operator_university[i]==None:
                            pass
                        else :
                            if (operator_university[i]=='1'):
                                checkbox_university_set = intersection_queryset(checkbox_university_set,CandidateBasic.objects.filter(nowEdu_instituteName__iexact=filter_university[i]))
                            elif (operator_university[i]=='2'):
                                checkbox_university_set = intersection_queryset(checkbox_university_set,CandidateBasic.objects.filter(~Q(nowEdu_instituteName__iexact=filter_university[i])))
                            elif (operator_university[i]=='3'):
                                checkbox_university_set = intersection_queryset(checkbox_university_set,CandidateBasic.objects.filter(nowEdu_instituteName__icontains=filter_university[i]))
                            elif (operator_university[i]=='4'):
                                checkbox_university_set = intersection_queryset(checkbox_university_set,CandidateBasic.objects.filter(~Q(nowEdu_instituteName__icontains=filter_university[i])))
                    all_candidate = intersection_queryset(all_candidate,checkbox_university_set)
                    print("all_candidate11 11 11 !!!!!!!!!!!",all_candidate)

                # Filter Age  { Active When OPERATOR AGE is not emply }
                if operator_age:
                    print("Entry Age")
                    checkbox_age_set=CandidateBasic.objects.all()
                    for i in range(0,len(operator_age)):
                        if filter_age[i]=='' or operator_age[i]==None:
                            pass
                        else :
                            if (operator_age[i]=='1'):
                                checkbox_age_set = intersection_queryset(checkbox_age_set,query_age('1',filter_age[i]))
                            elif (operator_age[i]=='2'):
                                checkbox_age_set = intersection_queryset(checkbox_age_set,query_age('2',filter_age[i]))
                            elif (operator_age[i]=='3'):
                                checkbox_age_set = intersection_queryset(checkbox_age_set,query_age('3',filter_age[i]))
                            elif (operator_age[i]=='4'):
                                checkbox_age_set = intersection_queryset(checkbox_age_set,query_age('4',filter_age[i]))
                            elif (operator_age[i]=='5'):
                                checkbox_age_set = intersection_queryset(checkbox_age_set,query_age('5',filter_age[i]))
                    all_candidate = intersection_queryset(all_candidate,checkbox_age_set)
                    # all_candidate = all_candidate.intersection(checkbox_salary_set)
                print("all_candidate12 12 12!!!!!!!!!!!",all_candidate)

                # Filter Experience  { Active When OPERATOR EXPERIENCE is not emply }
                if operator_experience:
                    print("Entry Experience")
                    print("Operator : " + str(operator_experience) + "filter_experience : " + str(filter_experience))
                    checkbox_experience_set=CandidateBasic.objects.all()
                    for i in range(0,len(operator_experience)):
                        experience_set = CandidateCertExperience.objects.none()
                        print("I : "+str(i) + "   Len : " + str(len(operator_experience)))
                        if filter_experience[i]=='' or operator_experience[i]==None:
                            pass
                        else :
                            print(operator_experience[i],"______")
                            if (operator_experience[i]=='1'):
                                experience_set = CandidateCertExperience.objects.filter(experience_name=filter_experience[i])
                                candidate_set = CandidateBasic.objects.none()
                                for candidate in experience_set:
                                    candidate_set = candidate_set.union(CandidateBasic.objects.filter(id_number=candidate.owner.id_number))
                                checkbox_experience_set = intersection_queryset(checkbox_experience_set,candidate_set)
                            elif (operator_experience[i]=='2'):
                                block_candidate = CandidateCertExperience.objects.filter(Q(experience_name=filter_experience[i])).values_list('owner',flat=True)
                                candidate_set = CandidateBasic.objects.filter(~Q(id_number__in=block_candidate))
                                checkbox_experience_set = intersection_queryset(checkbox_experience_set,candidate_set)
                            elif (operator_experience[i]=='3'):
                                experience_set = CandidateCertExperience.objects.filter(experience_name__icontains=filter_experience[i])
                                print("CONTAINNN!!!!!",experience_set)
                                candidate_set = CandidateBasic.objects.none()
                                for candidate in experience_set:
                                    candidate_set = candidate_set.union(CandidateBasic.objects.filter(id_number=candidate.owner.id_number))
                                checkbox_experience_set = intersection_queryset(checkbox_experience_set,candidate_set)
                            elif (operator_experience[i]=='4'):
                                block_candidate = CandidateCertExperience.objects.filter(Q(experience_name__icontains=filter_experience[i])).values_list('owner',flat=True)
                                candidate_set = CandidateBasic.objects.filter(~Q(id_number__in=block_candidate))
                                checkbox_experience_set = intersection_queryset(checkbox_experience_set,candidate_set)
                    print(i,"checkbox_experience_set",checkbox_experience_set)
                    all_candidate = intersection_queryset(all_candidate,checkbox_experience_set)
                    print("all_candidate13 13 13!!!!!!!!!!!",all_candidate)

                # Filter workexp  { Active When OPERATOR WORK EXPERIENCE is not emply }
                if operator_workexp:
                    print("Entry Workexp")
                    print("Operator : " + str(operator_workexp) + "filter_workexp : " + str(filter_workexp))
                    checkbox_workexp_set=CandidateBasic.objects.all()
                    for i in range(0,len(operator_workexp)):
                        workexp_set = CandidateWorkExperience.objects.none()
                        print("I : "+str(i) + "   Len : " + str(len(operator_workexp)))
                        if filter_workexp[i]=='' or operator_workexp[i]==None:
                            pass
                        else :
                            print(operator_workexp[i],"______")
                            if (operator_workexp[i]=='1'):
                                workexp_set = CandidateWorkExperience.objects.filter(experience_companyPosition=filter_workexp[i])
                                candidate_set = CandidateBasic.objects.none()
                                for candidate in workexp_set:
                                    candidate_set = candidate_set.union(CandidateBasic.objects.filter(id_number=candidate.owner.id_number))
                                checkbox_workexp_set = intersection_queryset(checkbox_workexp_set,candidate_set)
                            elif (operator_workexp[i]=='2'):
                                block_candidate = CandidateWorkExperience.objects.filter(Q(experience_companyPosition=filter_workexp[i])).values_list('owner',flat=True)
                                candidate_set = CandidateBasic.objects.filter(~Q(id_number__in=block_candidate))
                                checkbox_workexp_set = intersection_queryset(checkbox_workexp_set,candidate_set)
                            elif (operator_workexp[i]=='3'):
                                workexp_set = CandidateWorkExperience.objects.filter(experience_companyPosition__icontains=filter_workexp[i])
                                print("CONTAINNN!!!!!",workexp_set)
                                candidate_set = CandidateBasic.objects.none()
                                for candidate in workexp_set:
                                    candidate_set = candidate_set.union(CandidateBasic.objects.filter(id_number=candidate.owner.id_number))
                                checkbox_workexp_set = intersection_queryset(checkbox_workexp_set,candidate_set)
                            elif (operator_workexp[i]=='4'):
                                block_candidate = CandidateWorkExperience.objects.filter(Q(experience_companyPosition__icontains=filter_workexp[i])).values_list('owner',flat=True)
                                candidate_set = CandidateBasic.objects.filter(~Q(id_number__in=block_candidate))
                                checkbox_workexp_set = intersection_queryset(checkbox_workexp_set,candidate_set)
                    print(i,"checkbox_workexp_set",checkbox_workexp_set)
                    all_candidate = intersection_queryset(all_candidate,checkbox_workexp_set)
                    print("all_candidate14 14 14!!!!!!!!!!!",all_candidate)







    # return HttpResponse(json.dumps(response_data), content_type="application/json")
        html = render_to_string('filtered_candidate.html' , {'Candidate' :all_candidate },request=request)
    return JsonResponse({'html' : html})


def download_resume(request,selected_candidate):
    candidate = CandidateBasic.objects.filter(id_number=selected_candidate).first()
    path = str(CandidateAttachment.objects.filter(candidate_basic=candidate).first().attach_resume)
    print("เข้าโว้ยยยยย")
    print(path)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print(path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def download_transcript(request,selected_candidate):
    candidate = CandidateBasic.objects.filter(id_number=selected_candidate).first()
    path = str(CandidateAttachment.objects.filter(candidate_basic=candidate).first().attach_transcript)
    print("เข้าโว้ยยยยย")
    print(path)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print(path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
