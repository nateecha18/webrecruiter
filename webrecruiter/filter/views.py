from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

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

from jobapply.models import CandidateBasic,ConvertDatabase
from django.db.models import Q

# Import For Authenticate Account
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from candidate_cart.models import OrderItem, Order
from account.models import Profile


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
        list = []
        for i in range(1,len(operator_comskill)+1):
            txt = request.POST['tags'+str(i)].replace("\",\"","NaTeChA").replace("[\"","").replace("\"]","")
            list = txt.split("NaTeChA")
            # print(len(list),"+++++++++++++++")

            check_filter = []
            for j in range(0,len(list)):
                # print(j,"This is JJJ!!!")
                if not list[j]=='':
                    # print(list,"___________________________")
                    check_filter.append(list[j])
            if check_filter:
                filter_comskill.append(check_filter)
            else:
                filter_comskill.append('')
        print("TAG : ",filter_comskill,len(filter_comskill))
        print(operator_comskill,"++++++++++++")



        # list = array(request.POST['tags1'])
        # print(list)



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
            print("All Candidate ก่อนเข้า Filter Comskill : ", all_candidate)
            if filter_comskill:
                print("Entry Comskill")
                for i in range(0,len(operator_comskill)):
                    if filter_comskill[i]:
                        print(operator_comskill[i])
                        if operator_comskill[i]=='1' or operator_comskill[i]=='2':
                            checkbox_comskill_set=CandidateBasic.objects.all()
                            print("Entry condition 1")
                        elif operator_comskill[i]=='3' or operator_comskill[i]=='4':
                            checkbox_comskill_set=CandidateBasic.objects.none()
                            print("Entry condition 2")
                        print("NONE :",CandidateBasic.objects.none())
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



        # if (checkbox_position!='1' and checkbox_salary!='1' and checkbox_blood!='1' and checkbox_gpa!='1' and checkbox_gender!='1') :
        #     all_candidate = CandidateBasic.objects.all()
        cart_amount = get_cart_amount(request)
        context = {
            'Candidate': all_candidate,
            'Cart_amount':cart_amount,
        }
        template = loader.get_template("filter_candidate.html")
        return HttpResponse(template.render(context, request))

    if request.user.is_authenticated:
        all_candidate = CandidateBasic.objects.all()
        cart_amount = get_cart_amount(request)

        return render(request, "filter_candidate.html", {'Candidate': all_candidate,'Cart_amount':cart_amount})
    else:
        return redirect('login')


def candidate_detail(request,candidate_id):
    if request.user.is_authenticated:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        cart_amount = get_cart_amount(request)

        selected_candidate = get_object_or_404(CandidateBasic, id_number=candidate_id)

        txt_skill = selected_candidate.candidate_computer_skill.tags.replace("\",\"","NaTeChA").replace("[\"","").replace("\"]","")
        list_skill = txt_skill.split("NaTeChA")
        print(list_skill)
        convert_database = ConvertDatabase.objects.filter(database=selected_candidate.nowEdu_level)[0].converted
        return render(request,
                      'candidate_detail.html',
                      {'Candidate_id': candidate_id,
                       'Selected_candidate' : selected_candidate,
                       'Cart_amount' : cart_amount,
                       'Skills' : list_skill,
                       'ConvertDatabase' : convert_database})
    else:
        return redirect('login')
