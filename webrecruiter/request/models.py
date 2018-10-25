from django.db import models
from jobapply.models import CandidateBasic
from account.models import Profile

# Create your models here.
class Status(models.Model):
    status_id = models.CharField(max_length=15)
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name

class ProjectType(models.Model):
    project_type_id = models.CharField(max_length=15)
    project_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_type_name

class LevelRequest(models.Model):
    level_id = models.CharField(max_length=15)
    level_name = models.CharField(max_length=100)
    level_description = models.CharField(max_length=200)

    def __str__(self):
        return self.level_name

class RequestCandidate(models.Model):
    request_id = models.CharField(max_length=15)
    request_title = models.CharField(max_length=200, blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    project_type = models.ForeignKey(ProjectType, on_delete=models.SET_NULL, null=True)
    project_site = models.CharField(max_length=100, blank=True, null=True)
    tor_employee_amount = models.IntegerField(blank=True, null=True)
    now_employee_amount = models.IntegerField(blank=True, null=True)
    vacancy_employee_amount = models.IntegerField(blank=True, null=True)
    level = models.ForeignKey(LevelRequest, on_delete=models.SET_NULL, null=True)
    requirement = models.CharField(max_length=300, blank=True, null=True)
    certification = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=300, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True) # คน Request
    date_request = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.request_id

    # def get_candidate_owner(self):
    #     print("_____________________",self.owner.all())
    #     return self.owner.all()

class Comment(models.Model):
    request_owner = models.ForeignKey(RequestCandidate, on_delete=models.SET_NULL, null=True) # Request Candidate Post
    comment_id = models.CharField(max_length=15)
    comment_title = models.CharField(max_length=100)
    comment_detail = models.CharField(max_length=500)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True) # hr ที่สร้าง comment
    date_comment = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.comment_id
