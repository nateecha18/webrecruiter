from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View
from .models import CandidateBasic,CandidateHistoryEducation,CandidateComputerSkill,CandidateLanguageSkill,CandidateCertExperience,CandidateAttachment,CandidateWorkExperience

from jobapply.utils import render_to_pdf  # created in step 4
from django.shortcuts import render_to_response
from django.template import RequestContext

from addskill.models import Skill




# Create your views here.
def index(request):
    all_skill = Skill.objects.all()
    skill_name = ['fah']
    for name in all_skill:
        skill_name.append(name.skill_name)
    print("Skill Name : "+ str(skill_name))

    context = {}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))
    # return render('index.html', context_instance=RequestContext(request))


def submit_applyjob(request):
    print("ohh! It's sumbitted!")

    # CandidateHistoryEducation Table_______________________________________________________________________________
    edu_level = request.POST.getlist('edu_level')
    print(edu_level,"____________________-",len(edu_level))
    edu_country = request.POST.getlist('edu_country')
    edu_instituteName = request.POST.getlist('edu_instituteName')
    edu_fromYear = request.POST.getlist('edu_fromYear')
    edu_toYear = request.POST.getlist('edu_toYear')
    edu_major = request.POST.getlist('edu_major')
    edu_gpa = request.POST.getlist('edu_gpa')
    candidate_history_education = CandidateHistoryEducation(edu_level=edu_level,
                                                            edu_country=edu_country,
                                                            edu_instituteName=edu_instituteName,
                                                            edu_fromYear=edu_fromYear, edu_toYear=edu_toYear,
                                                            edu_major=edu_major, edu_gpa=edu_gpa)
    candidate_history_education.save()


    # CandidateComputerSkill Table__________________________________________________________________________________
    tags = request.POST.get('tags')
    candidate_computer_skill = CandidateComputerSkill(tags=tags)
    candidate_computer_skill.save()


    # CandidateLanguageSkill________________________________________________________________________________________
    skill_language = request.POST.getlist('skill_language')
    skill_language_typing = request.POST.getlist('skill_language_typing')
    skill_language_listen = request.POST.getlist('skill_language_listen')
    skill_language_speak = request.POST.getlist('skill_language_speak')
    skill_language_read = request.POST.getlist('skill_language_read')
    skill_language_write = request.POST.getlist('skill_language_write')
    candidate_language_skill = CandidateLanguageSkill(skill_language=skill_language,
                                                      skill_language_typing=skill_language_typing,
                                                      skill_language_listen=skill_language_listen,
                                                      skill_language_speak=skill_language_speak,
                                                      skill_language_read=skill_language_read,
                                                      skill_language_write=skill_language_write)
    candidate_language_skill.save()


    # CandidateCertExperience_______________________________________________________________________________________
    experience_name = request.POST.getlist('experience_name')
    experience_institute = request.POST.getlist('experience_institute')
    experience_cert = request.POST.getlist('experience_cert')
    candidate_cert_experience = CandidateCertExperience(experience_name=experience_name,
                                                        experience_institute=experience_institute,
                                                        experience_cert=experience_cert)
    candidate_cert_experience.save()


    # CandidateWorkExperience_______________________________________________________________________________________
    experience_companyName = request.POST.getlist('experience_companyName')
    experience_companyType = request.POST.getlist('experience_companyType')
    experience_companyStartDate = request.POST.getlist('experience_companyStartDate')
    experience_companyEndDate = request.POST.getlist('experience_companyEndDate')
    experience_companyPosition = request.POST.getlist('experience_companyPosition')
    experience_companySalary = request.POST.getlist('experience_companySalary')
    experience_companyReason = request.POST.getlist('experience_companyReason')
    candidate_work_experience = CandidateWorkExperience(experience_companyName=experience_companyName,
                                                        experience_companyType=experience_companyType,
                                                        experience_companyStartDate=experience_companyStartDate,
                                                        experience_companyEndDate=experience_companyEndDate,
                                                        experience_companyPosition=experience_companyPosition,
                                                        experience_companySalary=experience_companySalary,
                                                        experience_companyReason=experience_companyReason)
    candidate_work_experience.save()


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
    nowEdu_level = request.POST.get('nowEdu_level')
    nowEdu_instituteName = request.POST.get('nowEdu_instituteName')
    nowEdu_major = request.POST.get('nowEdu_major')
    nowEdu_gpa = request.POST.get('nowEdu_gpa')

    candidate_basic = CandidateBasic(id_number=id_number, position=position, salary=salary,
                                     profile_pic=profile_pic, nickname=nickname, name_title=name_title,
                                     firstname=firstname,lastname=lastname, bdate=bdate, blood=blood,
                                     nationality=nationality, race=race,
                                     religion=religion, status=status, email=email, mobile_no=mobile_no,
                                     home_no=home_no, facebook=facebook, line=line,
                                     military_status=military_status, military_reason=military_reason,
                                     check_study=check_study, nowEdu_level=nowEdu_level,
                                     nowEdu_instituteName=nowEdu_instituteName, nowEdu_major=nowEdu_major,
                                     nowEdu_gpa=nowEdu_gpa,
                                     candidate_computer_skill=candidate_computer_skill,
                                     candidate_history_education=candidate_history_education,
                                     candidate_language_skill=candidate_language_skill,
                                     candidate_cert_experience=candidate_cert_experience,candidate_work_experience=candidate_work_experience)
    candidate_basic.save()
    # candidate_attachment=candidate_attachment

    # CandidateAttachment___________________________________________________________________________________________
    attach_resume = request.FILES['attach_resume']
    attach_transcript = request.FILES['attach_transcript']
    candidate_attachment = CandidateAttachment(attach_resume=attach_resume,
                                               attach_transcript=attach_transcript,
                                               candidate_basic=candidate_basic)
    candidate_attachment.save()


    context = {}
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))


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
