
from django.db import models
from datetime import datetime, timedelta, time

class SkillType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.type_name

class Skill(models.Model):
    skill_name = models.CharField(primary_key=True,max_length=200)
    skill_type = models.ForeignKey(SkillType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.skill_name

class ExtraSkill(models.Model):
    extra_skill_name = models.CharField(primary_key=True,max_length=200)

    def __str__(self):
        return self.extra_skill_name

class EducationLevel(models.Model):
    value = models.CharField(primary_key=True,max_length=200)
    education_level = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.value

class Country(models.Model):
    countryCode = models.CharField(primary_key=True,max_length=5)
    currencyCode = models.CharField(max_length=3, blank=True, null=True)
    countryNameENG = models.CharField(max_length=200, blank=True, null=True)
    countryNameTH = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.countryNameTH

class Institute(models.Model):
    name = models.CharField(primary_key=True,max_length=250)

    def __str__(self):
        return self.name

class CandidateComputerSkill(models.Model):
    """docstring forCandidate_Computer_Skill."""
    tags = models.CharField(max_length=250, blank=True, null=True)

    def __int__(self):
        return self.id + '-' + self.tags

def user_picture_directory_path(instance, filename):
    # file will be uploaded to webrecruiter/static/uploads/candidate_<ID_NUMBER>/picture/<FILENAME>
    return 'uploads/candidate_{0}/picture/{1}'.format(instance.id_number, filename)


class CandidateBasic(models.Model):
    """docstring for Candidate_basic."""
    id_number = models.CharField(primary_key=True, max_length=13)
    date_apply = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=250, blank=True)
    salary = models.IntegerField(blank=True)
    profile_pic = models.ImageField(upload_to=user_picture_directory_path, blank=True,max_length=500)
    nickname = models.CharField(max_length=100, blank=True)
    name_title = models.CharField(max_length=50, blank=True)
    firstname = models.CharField(max_length=250, blank=True)
    lastname = models.CharField(max_length=250, blank=True)
    bdate = models.DateTimeField(default=datetime.now)
    blood = models.CharField(max_length=5, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    race = models.CharField(max_length=100, blank=True)
    religion = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)

    military_status = models.CharField(max_length=100, blank=True, null=True)
    military_reason = models.CharField(max_length=250, blank=True, null=True)

    email = models.CharField(max_length=250, blank=True)
    mobile_no = models.CharField(max_length=50, blank=True)
    home_no = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    line = models.CharField(max_length=100, blank=True)

    check_study = models.CharField(max_length=20, blank=True, null=True)
    nowEdu_level = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, null=True)
    nowEdu_instituteName = models.CharField(max_length=250, blank=True, null=True)
    nowEdu_major = models.CharField(max_length=250, blank=True, null=True)
    nowEdu_gpa = models.CharField(max_length=10, blank=True, null=True)

    # candidate_history_education = models.ManyToManyField(CandidateHistoryEducation)
    candidate_computer_skill = models.ForeignKey(CandidateComputerSkill, on_delete=models.CASCADE, blank=True)
    com_skill = models.ManyToManyField(Skill, blank=True)
    extra_com_skill = models.ManyToManyField(ExtraSkill, blank=True)

    def __str__(self):
        return 'CandidateBasic : {0}'.format(self.id_number)

    def calculate_age(self):
        today = datetime.today()
        return today.year - self.bdate.year - ((today.month, today.day) < (self.bdate.month, self.bdate.day))


def user_attachment_directory_path(instance, filename):
    # file will be uploaded to webrecruiter/static/uploads/candidate_<ID_NUMBER>/attachment/<FILENAME>
    return 'uploads/candidate_{0}/attachment/{1}'.format(instance.candidate_basic.id_number, filename)

class CandidateAttachment(models.Model):
    """docstring forAttachment."""
    candidate_basic = models.ForeignKey(CandidateBasic, on_delete=models.CASCADE, blank=True, null=True)
    attach_resume = models.FileField(upload_to=user_attachment_directory_path,blank=True)
    attach_transcript = models.FileField(upload_to=user_attachment_directory_path,blank=True)


    def __str__(self):
        return 'Attachment : {0}'.format(self.candidate_basic.id_number)

class CandidateHistoryEducation(models.Model):
    """docstring forCandidate_History_Education."""
    owner = models.ForeignKey(CandidateBasic, on_delete=models.SET_NULL, null=True)
    edu_level = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, null=True)
    edu_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    edu_instituteName = models.CharField(max_length=250, blank=True, null=True)
    edu_fromYear = models.CharField(max_length=10, blank=True, null=True)
    edu_toYear = models.CharField(max_length=10, blank=True, null=True)
    edu_major = models.CharField(max_length=250, blank=True, null=True)
    edu_gpa = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return '{0} ( {1} - {2} {3} )'.format(self.id, self.owner.firstname,self.edu_level.education_level,self.edu_fromYear)


class CandidateLanguageSkill(models.Model):
    """docstring forCandidate_Language_Skill."""
    owner = models.ForeignKey(CandidateBasic, on_delete=models.SET_NULL, null=True)
    skill_language = models.CharField(max_length=100, blank=True)
    skill_language_typing = models.CharField(max_length=10,blank=True)
    skill_language_listen = models.CharField(max_length=100, blank=True)
    skill_language_speak = models.CharField(max_length=100, blank=True)
    skill_language_read = models.CharField(max_length=100, blank=True)
    skill_language_write = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{0} ( {1} - {2} )'.format(self.id, self.owner.firstname,self.skill_language)

class CandidateCertExperience(models.Model):
    """docstring forCandidate_experience."""
    owner = models.ForeignKey(CandidateBasic, on_delete=models.SET_NULL, null=True)
    experience_name = models.CharField(max_length=250, blank=True)
    experience_institute = models.CharField(max_length=250, blank=True)
    experience_cert = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return '{0} ( {1} - {2} )'.format(self.id, self.owner.firstname,self.experience_name)

class CandidateWorkExperience(models.Model):
    """docstring forCandidate_Work_Experience."""
    owner = models.ForeignKey(CandidateBasic, on_delete=models.SET_NULL, null=True)
    experience_companyName = models.CharField(max_length=250, blank=True)
    experience_companyType = models.CharField(max_length=250, blank=True)
    experience_companyStartDate = models.CharField(max_length=20, blank=True)
    experience_companyEndDate = models.CharField(max_length=20, blank=True)
    experience_companyPosition = models.CharField(max_length=250, blank=True)
    experience_companySalary = models.CharField(max_length=15,blank=True)
    experience_companyReason = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return '{0} ( {1} - {2} )'.format(self.id, self.owner.firstname,self.experience_companyName)
