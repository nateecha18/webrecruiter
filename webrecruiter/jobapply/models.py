from django.db import models

# class Candidate_Military(models.Model):
#     """docstring forCandidate_Military."""
#     auto_increment_id = models.AutoField(primary_key=True)
#     military_status = models.CharField(max_length=100,blank=True)
#     military_reason = models.CharField(max_length=250,blank=True)
#
#     def __int__(self):
#         return self.auto_increment_id

# class Candidate_Contact(models.Model):
#     """docstring forCandidate_Contact."""
#     email = models.CharField(max_length=250)
#     mobile_no = models.CharField(max_length=50)
#     home_no = models.CharField(max_length=50)
#     facebook = models.CharField(max_length=150)
#     line = models.CharField(max_length=100)
#
#     def __int__(self):
#         return self.id

# class Candidate_Now_Education(models.Model):
#     """docstring forCandidate_Education."""
#     check_study = models.CharField(max_length=10)
#     nowEdu_level = models.CharField(max_length=250,blank=True)
#     nowEdu_instituteName = models.CharField(max_length=300,blank=True)
#     nowEdu_major = models.CharField(max_length=250,blank=True)
#     nowEdu_gpa = models.CharField(max_length=10,blank=True)
#
#     def __int__(self):
#         return self.id

class Candidate_History_Education(models.Model):
    """docstring forCandidate_History_Education."""
    edu_level = models.CharField(max_length=250,blank=True)
    edu_country = models.CharField(max_length=250,blank=True)
    edu_instituteName = models.CharField(max_length=250,blank=True)
    edu_fromYear = models.CharField(max_length=10,blank=True)
    edu_toYear = models.CharField(max_length=10,blank=True)
    edu_major = models.CharField(max_length=250,blank=True)
    edu_gpa = models.CharField(max_length=10,blank=True)

    def __int__(self):
        return self.id + '-' + self.edu_level

class Candidate_Computer_Skill(models.Model):
    """docstring forCandidate_Computer_Skill."""
    tags = models.CharField(max_length=300,blank=True)

    def __int__(self):
        return self.id + '-' + self.tags

class Candidate_Language_Skill(models.Model):
    """docstring forCandidate_Language_Skill."""
    skill_language = models.CharField(max_length=100,blank=True)
    skill_language_typing = models.IntegerField(blank=True)
    skill_language_listen = models.CharField(max_length=100,blank=True)
    skill_language_speak = models.CharField(max_length=100,blank=True)
    skill_language_read = models.CharField(max_length=100,blank=True)
    skill_language_write = models.CharField(max_length=100,blank=True)

    def __int__(self):
        return self.id + '-' + self.skill_language

class Candidate_Cert_Experience(models.Model):
    """docstring forCandidate_experience."""
    experience_name = models.CharField(max_length=250,blank=True)
    experience_institute = models.CharField(max_length=250,blank=True)
    experience_cert = models.CharField(max_length=250,blank=True)

    def __int__(self):
        return self.id + '-' + self.experience_name

class Candidate_Work_Experience(models.Model):
    """docstring forCandidate_Work_Experience."""
    experience_companyName = models.CharField(max_length=250,blank=True)
    experience_companyType = models.CharField(max_length=250,blank=True)
    experience_companyStartDate = models.DateField(blank=True)
    experience_companyEndDate = models.DateField(blank=True)
    experience_companyPosition = models.CharField(max_length=250,blank=True)
    experience_companySalary = models.IntegerField(blank=True)
    experience_companyReason = models.CharField(max_length=300,blank=True)

    def __int__(self):
        return self.id + '-' + self.experience_companyName

class Candidate_Attachment(models.Model):
    """docstring forAttachment."""
    attach_resume = models.FileField(blank=True)
    attach_transcript = models.FileField(blank=True)

    def __int__(self):
        return self.id

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'webrecruiter/static/uploads/user_{0}/{1}'.format(instance.id_number, filename)

class Candidate_Basic(models.Model):
    """docstring for Candidate_basic."""
    id_number = models.CharField(primary_key=True,max_length=13)
    position = models.CharField(max_length=250,blank=True)
    salary = models.IntegerField(blank=True)
    profile_pic = models.ImageField(upload_to=user_directory_path,blank=True)
    nickname = models.CharField(max_length=100,blank=True)
    name_title = models.CharField(max_length=50,blank=True)
    firstname = models.CharField(max_length=250,blank=True)
    lastname = models.CharField(max_length=250,blank=True)
    bdate = models.DateField(blank=True)
    blood = models.CharField(max_length=5,blank=True)
    nationality = models.CharField(max_length=100,blank=True)
    race = models.CharField(max_length=100,blank=True)
    religion = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=100,blank=True)

    military_status = models.CharField(max_length=100,blank=True)
    military_reason = models.CharField(max_length=250,blank=True)

    email = models.CharField(max_length=250,blank=True)
    mobile_no = models.CharField(max_length=50,blank=True)
    home_no = models.CharField(max_length=50,blank=True)
    facebook = models.CharField(max_length=150,blank=True)
    line = models.CharField(max_length=100,blank=True)

    check_study = models.CharField(max_length=10,blank=True,null=True)
    nowEdu_level = models.CharField(max_length=250,blank=True)
    nowEdu_instituteName = models.CharField(max_length=300,blank=True)
    nowEdu_major = models.CharField(max_length=250,blank=True)
    nowEdu_gpa = models.CharField(max_length=10,blank=True)

    # candidate_military = models.ForeignKey(Candidate_Military, on_delete=models.CASCADE,blank=True)
    # candidate_contact = models.ForeignKey(Candidate_Contact, on_delete=models.CASCADE,blank=True)
    # candidate_now_education = models.ForeignKey(Candidate_Now_Education, on_delete=models.CASCADE,blank=True)

    candidate_history_education = models.ForeignKey(Candidate_History_Education, on_delete=models.CASCADE,blank=True)
    candidate_computer_skill = models.ForeignKey(Candidate_Computer_Skill, on_delete=models.CASCADE,blank=True)
    # candidate_language_skill = models.ForeignKey(Candidate_Language_Skill, on_delete=models.CASCADE,blank=True)
    # candidate_attachment = models.ForeignKey(Candidate_Attachment, on_delete=models.CASCADE,blank=True)
    # candidate_cert_experience = models.ForeignKey(Candidate_Cert_Experience, on_delete=models.CASCADE,blank=True)
    # candidate_work_experience = models.ForeignKey(Candidate_Work_Experience, on_delete=models.CASCADE,blank=True)

    def __int__(self):
        return self.id_number
