from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View
from jobapply.models import CandidateBasic,CandidateHistoryEducation,CandidateComputerSkill,CandidateLanguageSkill,CandidateCertExperience,CandidateAttachment,CandidateWorkExperience,EducationLevel,Institute,Country,Skill,SkillType,ExtraSkill

from jobapply.utils import render_to_pdf  # created in step 4
from django.shortcuts import render_to_response
from django.template import RequestContext

# from addskill.models import Skill

from django.db.models import Q

import json
import csv

from django.core import serializers
from datetime import datetime
from dateutil.parser import parse

# Create your views here.
def index(request):

        if request.method == 'POST':
            print("ohh! It's sumbitted!")

            # CandidateComputerSkill Table__________________________________________________________________________________
            tags = request.POST.get('tags')
            candidate_computer_skill = CandidateComputerSkill(tags=tags)
            candidate_computer_skill.save()


            # CandidateBasic Table__________________________________________________________________________________________
            id_number = request.POST["id_number"]
            position = request.POST["position"]
            salary = request.POST["salary"]
            profile_pic = request.FILES["profile_pic"]
            nickname = request.POST["nickname"]
            name_title = request.POST["name_title"]
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            bdate = request.POST["bdate"]
            blood = request.POST["blood"]
            race = request.POST["race"]
            nationality = request.POST["nationality"]
            religion = request.POST["religion"]
            status = request.POST["status"]

            military_status = request.POST.get('military_status')
            military_reason = request.POST.get('military_reason')

            email = request.POST.get('email')
            mobile_no = request.POST.get('mobile_no')
            home_no = request.POST.get('home_no')
            facebook = request.POST.get('facebook')
            line = request.POST.get('line')

            check_study = request.POST.get('check_study')
            print("checked!!!!!!!!!!!!!!!!!!" + str(check_study))
            nowEdu_level_value = request.POST.get('nowEdu_level')
            nowEdu_level = EducationLevel.objects.filter(value=nowEdu_level_value).first()
            nowEdu_instituteName = request.POST.get('nowEdu_instituteName')
            nowEdu_major = request.POST.get('nowEdu_major')
            nowEdu_gpa = request.POST.get('nowEdu_gpa')

            candidate_basic = CandidateBasic(id_number=id_number, position=position, salary=salary,
                                             profile_pic=profile_pic, nickname=nickname, name_title=name_title,
                                             firstname=firstname,lastname=lastname, bdate=datetime.strptime(bdate, '%m/%d/%Y'), blood=blood,
                                             nationality=nationality, race=race,
                                             religion=religion, status=status, email=email, mobile_no=mobile_no,
                                             home_no=home_no, facebook=facebook, line=line,
                                             military_status=military_status, military_reason=military_reason,
                                             check_study=check_study, nowEdu_level=nowEdu_level,
                                             nowEdu_instituteName=nowEdu_instituteName, nowEdu_major=nowEdu_major,
                                             nowEdu_gpa=nowEdu_gpa,candidate_computer_skill=candidate_computer_skill)
            candidate_basic.save()
            skill_list = []
            txt = tags.replace("\",\"","NaTeeChABaLaBooDiDo").replace("[\"","").replace("\"]","")
            skill_list = txt.split("NaTeeChABaLaBooDiDo")
            print("_______________",skill_list)
            for i in range(0,len(skill_list)):
                print("______skillList______",skill_list[i])
                if skill_list[i]:
                    print(Skill.objects.filter(skill_name__iexact=skill_list[i]))
                    selected_skill = Skill.objects.filter(skill_name__iexact=skill_list[i]).first()
                    print(selected_skill)
                    if selected_skill:
                        candidate_basic.com_skill.add(selected_skill)
                    else:
                        selected_extra_skill,status = ExtraSkill.objects.get_or_create(extra_skill_name = skill_list[i])
                        if selected_extra_skill:
                            print(selected_extra_skill)
                            candidate_basic.extra_com_skill.add(selected_extra_skill)
            candidate_basic.save()

            # CandidateAttachment___________________________________________________________________________________________
            attach_resume = request.FILES['attach_resume']
            attach_transcript = request.FILES['attach_transcript']
            candidate_attachment = CandidateAttachment(attach_resume=attach_resume,
                                                       attach_transcript=attach_transcript,
                                                       candidate_basic=candidate_basic)
            candidate_attachment.save()


            # CandidateHistoryEducation Table_______________________________________________________________________________
            edu_level_value = request.POST.getlist('edu_level')
            edu_country = request.POST.getlist('edu_country')
            edu_instituteName = request.POST.getlist('edu_instituteName')
            edu_fromYear = request.POST.getlist('edu_fromYear')
            edu_toYear = request.POST.getlist('edu_toYear')
            edu_major = request.POST.getlist('edu_major')
            edu_gpa = request.POST.getlist('edu_gpa')
            for i in range(0,len(edu_level_value)):
                print("เข้ามาเก็บ Histort Education","| รอบที่ : ",i)
                edu_level_value_i = edu_level_value[i]
                edu_level = EducationLevel.objects.filter(value=edu_level_value_i).first()
                candidate = CandidateBasic.objects.filter(id_number=id_number).first()
                country = Country.objects.filter(countryCode=edu_country).first()
                candidate_history_education = CandidateHistoryEducation(edu_level=edu_level,
                                                                        owner=candidate,
                                                                        edu_country=country,
                                                                        edu_instituteName=edu_instituteName[i],
                                                                        edu_fromYear=edu_fromYear[i], edu_toYear=edu_toYear[i],
                                                                        edu_major=edu_major[i], edu_gpa=edu_gpa[i])
                candidate_history_education.save()

            # CandidateLanguageSkill________________________________________________________________________________________
            skill_language = request.POST.getlist('skill_language')
            skill_language_typing = request.POST.getlist('skill_language_typing')
            skill_language_listen = request.POST.getlist('skill_language_listen')
            skill_language_speak = request.POST.getlist('skill_language_speak')
            skill_language_read = request.POST.getlist('skill_language_read')
            skill_language_write = request.POST.getlist('skill_language_write')
            for i in range(0,len(skill_language)):
                candidate = CandidateBasic.objects.filter(id_number=id_number).first()
                candidate_language_skill = CandidateLanguageSkill(skill_language=skill_language[i],
                                                                  owner=candidate,
                                                                  skill_language_typing=skill_language_typing[i+1],
                                                                  skill_language_listen=skill_language_listen[i],
                                                                  skill_language_speak=skill_language_speak[i],
                                                                  skill_language_read=skill_language_read[i],
                                                                  skill_language_write=skill_language_write[i])
                candidate_language_skill.save()

            # CandidateCertExperience_______________________________________________________________________________________
            experience_name = request.POST.getlist('experience_name')
            experience_institute = request.POST.getlist('experience_institute')
            experience_cert = request.POST.getlist('experience_cert')
            for i in range(1,len(experience_name)):
                candidate = CandidateBasic.objects.filter(id_number=id_number).first()
                candidate_cert_experience = CandidateCertExperience(experience_name=experience_name[i],
                                                                    owner=candidate,
                                                                    experience_institute=experience_institute[i],
                                                                    experience_cert=experience_cert[i])
                candidate_cert_experience.save()

            # CandidateWorkExperience_______________________________________________________________________________________
            experience_companyName = request.POST.getlist('experience_companyName')
            experience_companyType = request.POST.getlist('experience_companyType')
            experience_companyStartDate = request.POST.getlist('experience_companyStartDate')
            experience_companyEndDate = request.POST.getlist('experience_companyEndDate')
            experience_companyPosition = request.POST.getlist('experience_companyPosition')
            experience_companySalary = request.POST.getlist('experience_companySalary')
            experience_companyReason = request.POST.getlist('experience_companyReason')
            for i in range(1,len(experience_companyName)):
                candidate = CandidateBasic.objects.filter(id_number=id_number).first()
                candidate_work_experience = CandidateWorkExperience(experience_companyName=experience_companyName[i],
                                                                    owner=candidate,
                                                                    experience_companyType=experience_companyType[i],
                                                                    experience_companyStartDate=experience_companyStartDate[i],
                                                                    experience_companyEndDate=experience_companyEndDate[i],
                                                                    experience_companyPosition=experience_companyPosition[i],
                                                                    experience_companySalary=experience_companySalary[i],
                                                                    experience_companyReason=experience_companyReason[i])
                candidate_work_experience.save()

            country = Country.objects.all()
            education_level = EducationLevel.objects.all()
            context = {
                'Levels' : education_level,
                'Country': country,
            }
            template = loader.get_template("index.html")
            return HttpResponse(template.render(context, request))

        # CandidateBasic.objects.all().delete()
        # CandidateHistoryEducation.objects.all().delete()
        # CandidateComputerSkill.objects.all().delete()
        # CandidateLanguageSkill.objects.all().delete()
        # CandidateCertExperience.objects.all().delete()
        # CandidateAttachment.objects.all().delete()
        # CandidateWorkExperience.objects.all().delete()
        skill_name = list(Skill.objects.all().values_list('skill_name',flat=True))
        country = Country.objects.all()
        education_level = EducationLevel.objects.all()
        context = {
            'Levels' : education_level,
            'Country': country,
            'Skill' : skill_name,
        }
        template = loader.get_template("index.html")
        return HttpResponse(template.render(context, request))
        # return render('index.html', context_instance=RequestContext(request))

# Class สร้าง PDF
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        all_candidate = CandidateBasic.objects.all()
        print(str(all_candidate))
        # template = loader.get_template('invoice.html')
        context = {
            'invoice_id': 123,
            'customer_name': 'John Cooper',
            'amount': 139.99,
            'today': "Today",
            'Candidate': all_candidate,

        }
        # html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % "1234"
            content = "inline; filename='%s'" % filename
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % filename
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def show_list(request):
    all_candidate = CandidateBasic.objects.all()
    return render(request, "show.html", {'Candidate': all_candidate})

def load_country(file_path):
    "this loads country from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    for row in reader:
        country = Country(countryCode=row['countryCode'],currencyCode=row['currencyCode'],countryNameENG=row['countryNameENG'],countryNameTH=row['countryNameTH'])
        country.save()

def load_institute(file_path):
    "this loads institute from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    for row in reader:
        institute = Institute(name=row['name'])
        institute.save()

def get_institute(request):
    if request.is_ajax():
        query = request.GET.get('term', '')
        institutes = Institute.objects.filter(name__icontains = query )
        results = []
        for institute in institutes:
            institute_json = institute.name
            results.append(institute_json)
        data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
