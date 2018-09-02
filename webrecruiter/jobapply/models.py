
from django.db import models


class CandidateHistoryEducation(models.Model):
    """docstring forCandidate_History_Education."""
    edu_level = models.CharField(max_length=250, blank=True, null=True)
    edu_country = models.CharField(max_length=250, blank=True, null=True)
    edu_instituteName = models.CharField(max_length=250, blank=True, null=True)
    edu_fromYear = models.CharField(max_length=10, blank=True, null=True)
    edu_toYear = models.CharField(max_length=10, blank=True, null=True)
    edu_major = models.CharField(max_length=250, blank=True, null=True)
    edu_gpa = models.CharField(max_length=10, blank=True, null=True)

    def __int__(self):
        return self.id + '-' + self.edu_level


class CandidateComputerSkill(models.Model):
    """docstring forCandidate_Computer_Skill."""
    tags = models.CharField(max_length=300, blank=True)

    def __int__(self):
        return self.id + '-' + self.tags


class CandidateLanguageSkill(models.Model):
    """docstring forCandidate_Language_Skill."""
    skill_language = models.CharField(max_length=100, blank=True)
    skill_language_typing = models.CharField(max_length=10,blank=True)
    skill_language_listen = models.CharField(max_length=100, blank=True)
    skill_language_speak = models.CharField(max_length=100, blank=True)
    skill_language_read = models.CharField(max_length=100, blank=True)
    skill_language_write = models.CharField(max_length=100, blank=True)

    def __int__(self):
        return self.id + '-' + self.skill_language


class CandidateCertExperience(models.Model):
    """docstring forCandidate_experience."""
    experience_name = models.CharField(max_length=250, blank=True)
    experience_institute = models.CharField(max_length=250, blank=True)
    experience_cert = models.CharField(max_length=250, blank=True)

    def __int__(self):
        return self.id + '-' + self.experience_name


class CandidateWorkExperience(models.Model):
    """docstring forCandidate_Work_Experience."""
    experience_companyName = models.CharField(max_length=250, blank=True)
    experience_companyType = models.CharField(max_length=250, blank=True)
    experience_companyStartDate = models.CharField(max_length=20, blank=True)
    experience_companyEndDate = models.CharField(max_length=20, blank=True)
    experience_companyPosition = models.CharField(max_length=250, blank=True)
    experience_companySalary = models.CharField(max_length=15,blank=True)
    experience_companyReason = models.CharField(max_length=300, blank=True)

    def __int__(self):
        return self.id + '-' + self.experience_companyName

# def user_attachment_directory_path(instance, filename):
#     # file will be uploaded to webrecruiter/static/uploads/candidate_<ID_NUMBER>/attachment/<FILENAME>
#     return 'webrecruiter/static/uploads/candidate_{0}/attachment/{1}'.format(instance.candidate_basic.id_number, filename)


# class CandidateAttachment(models.Model):
#     """docstring forAttachment."""
#     candidate_basic = models.ForeignKey(CandidateBasic, on_delete=models.CASCADE, blank=True)
#     attach_resume = models.FileField(upload_to=user_attachment_directory_path,blank=True)
#     attach_transcript = models.FileField(upload_to=user_attachment_directory_path,blank=True)
#
#
#     def __int__(self):
#         return self.id


def user_picture_directory_path(instance, filename):
    # file will be uploaded to webrecruiter/static/uploads/candidate_<ID_NUMBER>/picture/<FILENAME>
    return 'webrecruiter/static/uploads/candidate_{0}/picture/{1}'.format(instance.id_number, filename)


class CandidateBasic(models.Model):
    """docstring for Candidate_basic."""
    id_number = models.CharField(primary_key=True, max_length=13)
    position = models.CharField(max_length=250, blank=True)
    salary = models.IntegerField(blank=True)
    profile_pic = models.ImageField(upload_to=user_picture_directory_path, blank=True)
    nickname = models.CharField(max_length=100, blank=True)
    name_title = models.CharField(max_length=50, blank=True)
    firstname = models.CharField(max_length=250, blank=True)
    lastname = models.CharField(max_length=250, blank=True)
    bdate = models.DateField(blank=True)
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
    nowEdu_level = models.CharField(max_length=250, blank=True, null=True)
    nowEdu_instituteName = models.CharField(max_length=300, blank=True, null=True)
    nowEdu_major = models.CharField(max_length=250, blank=True, null=True)
    nowEdu_gpa = models.CharField(max_length=10, blank=True, null=True)

    candidate_history_education = models.ForeignKey(CandidateHistoryEducation, on_delete=models.CASCADE, blank=True)
    candidate_computer_skill = models.ForeignKey(CandidateComputerSkill, on_delete=models.CASCADE, blank=True)
    candidate_language_skill = models.ForeignKey(CandidateLanguageSkill, on_delete=models.CASCADE,blank=True,null=True)
    # candidate_attachment = models.ForeignKey(CandidateAttachment, on_delete=models.CASCADE,blank=True,null=True)
    candidate_cert_experience = models.ForeignKey(CandidateCertExperience, on_delete=models.CASCADE,blank=True,null=True)
    candidate_work_experience = models.ForeignKey(CandidateWorkExperience, on_delete=models.CASCADE,blank=True,null=True)

    def __int__(self):
        return self.id_number

def user_attachment_directory_path(instance, filename):
    # file will be uploaded to webrecruiter/static/uploads/candidate_<ID_NUMBER>/attachment/<FILENAME>
    return 'webrecruiter/static/uploads/candidate_{0}/attachment/{1}'.format(instance.candidate_basic.id_number, filename)

class CandidateAttachment(models.Model):
    """docstring forAttachment."""
    candidate_basic = models.ForeignKey(CandidateBasic, on_delete=models.CASCADE, blank=True, null=True)
    attach_resume = models.FileField(upload_to=user_attachment_directory_path,blank=True)
    attach_transcript = models.FileField(upload_to=user_attachment_directory_path,blank=True)


    def __int__(self):
        return self.id
