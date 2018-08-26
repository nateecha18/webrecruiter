from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views
from .models import Candidate_Basic, Candidate_Military, Candidate_Contact, Candidate_Now_Education,Candidate_History_Education,Candidate_Computer_Skill

# Create your views here.
def index(request):
	template=loader.get_template("index.html")
	return HttpResponse(template.render())

def submit_applyjob(request):
	print("ohh! It's sumbitted!")
	# military Table
	military_status = request.POST.get('military_status')
	military_reason = request.POST.get('military_reason')

	candidate_military = Candidate_Military(military_status=military_status,military_reason=military_reason)
	candidate_military.save()

	# contact Table
	email = request.POST.get('email')
	mobile_no = request.POST.get('mobile_no')
	home_no = request.POST.get('home_no')
	facebook = request.POST.get('facebook')
	line = request.POST.get('line')

	candidate_contact = Candidate_Contact(email=email,mobile_no=mobile_no,home_no=home_no,facebook=facebook,line=line)
	candidate_contact.save()

	# Now_Education Table
	check_study = request.POST.get('check_study')
	print("checked!!!!!!!!!!!!!!!!!!" + str(check_study))
	nowEdu_level = request.POST.get('nowEdu_level')
	nowEdu_instituteName = request.POST.get('nowEdu_instituteName')
	nowEdu_major = request.POST.get('nowEdu_major')
	nowEdu_gpa = request.POST.get('nowEdu_gpa')

	candidate_now_education = Candidate_Now_Education(check_study=check_study,nowEdu_level=nowEdu_level,
	nowEdu_instituteName=nowEdu_instituteName,nowEdu_major=nowEdu_major,nowEdu_gpa=nowEdu_gpa)
	candidate_now_education.save()

	# Candidate_History_Education Table
	edu_level = request.POST.get('edu_level')
	edu_country = request.POST.get('edu_country')
	edu_instituteName = request.POST.get('edu_instituteName')
	edu_fromYear = request.POST.get('edu_fromYear')
	edu_toYear = request.POST.get('edu_toYear')
	edu_major = request.POST.get('edu_major')
	edu_gpa = request.POST.get('edu_gpa')


	candidate_history_education = Candidate_History_Education(edu_level=edu_level,
	edu_country=edu_country,edu_instituteName=edu_instituteName,edu_fromYear=edu_fromYear,edu_toYear=edu_toYear,
	edu_major=edu_major,edu_gpa=edu_gpa)
	candidate_history_education.save()

	# Candidate_Computer_Skill Table
	tags = request.POST.get('tags')

	candidate_computer_skill = Candidate_Computer_Skill(tags=tags)
	candidate_computer_skill.save()

	# basic Table
	id_number = request.POST["id_number"]
	position = request.POST["position"]
	salary = request.POST["salary"]
	profile_pic = request.POST["profile_pic"]
	nickname = request.POST["nickname"]
	name_title = request.POST["name_title"]
	firstname = request.POST["firstname"]
	lastname = request.POST["lastname"]
	bdate = request.POST["bdate"]
	blood = request.POST["blood"]
	nationality = request.POST["nationality"]
	race = request.POST["race"]
	nationality = request.POST["nationality"]
	religion = request.POST["religion"]
	status = request.POST["status"]
	# print("candidate_military" + "-->>>" + str(candidate_military))
	# candidate_military = request.POST.get("candidate_military",False)
	# candidate_contact = request.POST["candidate_contact"]
	# candidate_now_education = request.POST["candidate_now_education"]
	# candidate_history_education = request.POST["candidate_history_education"]
	# candidate_computer_skill = request.POST["candidate_computer_skill"]
	# candidate_language_skill = request.POST["candidate_language_skill"]
	# candidate_attachment = request.POST["candidate_attachment"]
	# candidate_cert_experience = request.POST["candidate_cert_experience"]
	# candidate_work_experience = request.POST["candidate_work_experience"]


	candidate_basic = Candidate_Basic(id_number=id_number,position=position,salary=salary,
	profile_pic=profile_pic,nickname=nickname,name_title=name_title,
	firstname=firstname,lastname=lastname,bdate=bdate,blood=blood,nationality=nationality,
	religion=religion,status=status,candidate_military=candidate_military,candidate_contact=candidate_contact,
	candidate_now_education=candidate_now_education,candidate_history_education=candidate_history_education)
	candidate_basic.save()
	# ,candidate_computer_skill=candidate_computer_skill,
	# candidate_language_skill=candidate_language_skill,candidate_attachment=candidate_attachment,
	# candidate_cert_experience=candidate_cert_experience,candidate_work_experience=candidate_work_experience

	return render(request, "index.html")
