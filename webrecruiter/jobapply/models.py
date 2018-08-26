from django.db import models

class Candidate_Military(models.Model):
    """docstring forCandidate_Military."""
    auto_increment_id = models.AutoField(primary_key=True)
    military_status = models.CharField(max_length=100,null=True)
    military_reason = models.CharField(max_length=250,null=True)

    def __int__(self):
        return self.auto_increment_id

class Candidate_Contact(models.Model):
    """docstring forCandidate_Contact."""
    email = models.CharField(max_length=250)
    mobile_no = models.CharField(max_length=50)
    home_no = models.CharField(max_length=50)
    facebook = models.CharField(max_length=150)
    line = models.CharField(max_length=100)

    def __int__(self):
        return self.id

class Candidate_Now_Education(models.Model):
    """docstring forCandidate_Education."""
    check_study = models.CharField(max_length=10)
    nowEdu_level = models.CharField(max_length=250,null=True)
    nowEdu_instituteName = models.CharField(max_length=300,null=True)
    nowEdu_major = models.CharField(max_length=250,null=True)
    nowEdu_gpa = models.CharField(max_length=10,null=True)

    def __int__(self):
        return self.id

class Candidate_History_Education(models.Model):
    """docstring forCandidate_History_Education."""
    edu_level = models.CharField(max_length=250,null=True)
    edu_country = models.CharField(max_length=250,null=True)
    edu_instituteName = models.CharField(max_length=250,null=True)
    edu_fromYear = models.CharField(max_length=10,null=True)
    edu_toYear = models.CharField(max_length=10,null=True)
    edu_major = models.CharField(max_length=250,null=True)
    edu_gpa = models.CharField(max_length=10,null=True)

    def __int__(self):
        return self.id + '-' + self.edu_level

class Candidate_Computer_Skill(models.Model):
    """docstring forCandidate_Computer_Skill."""
    tags = models.CharField(max_length=300)

    def __int__(self):
        return self.id + '-' + self.tags

class Candidate_Language_Skill(models.Model):
    """docstring forCandidate_Language_Skill."""
    skill_language = models.CharField(max_length=100)
    skill_language_typing = models.IntegerField()
    skill_language_listen = models.CharField(max_length=100)
    skill_language_speak = models.CharField(max_length=100)
    skill_language_read = models.CharField(max_length=100)
    skill_language_write = models.CharField(max_length=100)

    def __int__(self):
        return self.id + '-' + self.skill_language

class Candidate_Cert_Experience(models.Model):
    """docstring forCandidate_experience."""
    experience_name = models.CharField(max_length=250)
    experience_institute = models.CharField(max_length=250)
    experience_cert = models.CharField(max_length=250)

    def __int__(self):
        return self.id + '-' + self.experience_name

class Candidate_Work_Experience(models.Model):
    """docstring forCandidate_Work_Experience."""
    experience_companyName = models.CharField(max_length=250)
    experience_companyType = models.CharField(max_length=250)
    experience_companyStartDate = models.DateField()
    experience_companyEndDate = models.DateField()
    experience_companyPosition = models.CharField(max_length=250)
    experience_companySalary = models.IntegerField()
    experience_companyReason = models.CharField(max_length=300)

    def __int__(self):
        return self.id + '-' + self.experience_companyName

class Candidate_Attachment(models.Model):
    """docstring forAttachment."""
    attach_resume = models.FileField()
    attach_transcript = models.FileField()

    def __int__(self):
        return self.id

class Candidate_Basic(models.Model):
    """docstring for Candidate_basic."""
    id_number = models.CharField(primary_key=True,max_length=13)
    position = models.CharField(max_length=250,null=True)
    salary = models.IntegerField(null=True)
    profile_pic = models.ImageField(null=True)
    nickname = models.CharField(max_length=100,null=True)
    name_title = models.CharField(max_length=50,null=True)
    firstname = models.CharField(max_length=250,null=True)
    lastname = models.CharField(max_length=250,null=True)
    bdate = models.DateField(null=True)
    blood = models.CharField(max_length=5,null=True)
    nationality = models.CharField(max_length=100,null=True)
    race = models.CharField(max_length=100,null=True)
    nationality = models.CharField(max_length=100,null=True)
    religion = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    candidate_military = models.ForeignKey(Candidate_Military, on_delete=models.CASCADE,null=True)
    candidate_contact = models.ForeignKey(Candidate_Contact, on_delete=models.CASCADE,null=True)
    candidate_now_education = models.ForeignKey(Candidate_Now_Education, on_delete=models.CASCADE,null=True)
    candidate_history_education = models.ForeignKey(Candidate_History_Education, on_delete=models.CASCADE,null=True)
    candidate_computer_skill = models.ForeignKey(Candidate_Computer_Skill, on_delete=models.CASCADE,null=True)
    candidate_language_skill = models.ForeignKey(Candidate_Language_Skill, on_delete=models.CASCADE,null=True)
    candidate_attachment = models.ForeignKey(Candidate_Attachment, on_delete=models.CASCADE,null=True)
    candidate_cert_experience = models.ForeignKey(Candidate_Cert_Experience, on_delete=models.CASCADE,null=True)
    candidate_work_experience = models.ForeignKey(Candidate_Work_Experience, on_delete=models.CASCADE,null=True)

    def __int__(self):
        return self.id_number
