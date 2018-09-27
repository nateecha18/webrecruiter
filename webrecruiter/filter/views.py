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


        print("Filter List : " + str(filter_option) + "Operator Position : "+ str(operator_position) + " Position : " + str(filter_position))
        position = FilterPosition(operator_position=operator_position,filter_position=filter_position)
        position.save()

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
                    if filter_position[i]=='':
                        pass
                    else :
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




        # if (checkbox_position!='1' and checkbox_salary!='1' and checkbox_blood!='1' and checkbox_gpa!='1' and checkbox_gender!='1') :
        #     all_candidate = CandidateBasic.objects.all()
        context = {
            'Candidate': all_candidate,
        }
        template = loader.get_template("filter_candidate.html")
        return HttpResponse(template.render(context, request))

    all_candidate = CandidateBasic.objects.all()
    print("All Can : " + str(all_candidate))
    return render(request, "filter_candidate.html", {'Candidate': all_candidate})

def submit_filter(request):
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


    print("Filter List : " + str(filter_option) + "Operator Position : "+ str(operator_position) + " Position : " + str(filter_position))
    position = FilterPosition(operator_position=operator_position,filter_position=filter_position)
    position.save()

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
                if filter_position[i]=='':
                    pass
                else :
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




    # if (checkbox_position!='1' and checkbox_salary!='1' and checkbox_blood!='1' and checkbox_gpa!='1' and checkbox_gender!='1') :
    #     all_candidate = CandidateBasic.objects.all()
    context = {
        'Candidate': all_candidate,
    }
    template = loader.get_template("filter_candidate.html")
    return HttpResponse(template.render(context, request))
