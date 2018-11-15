from django.db import models
from django.db.models import Avg, Count, Min, Sum
from account.models import Profile
from jobapply.models import CandidateBasic

# Create your models here.

class ProjectType(models.Model):
    project_type_id = models.CharField(max_length=15)
    project_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_type_name

class ProjectLevel(models.Model):
    level_id = models.CharField(max_length=15)
    level_name = models.CharField(max_length=100)
    level_description = models.CharField(max_length=200)

    def __str__(self):
        return self.level_name

class PositionProject(models.Model):
    project_name = models.CharField(max_length=100, blank=True, null=True)
    project_type = models.ForeignKey(ProjectType, on_delete=models.SET_NULL, null=True)
    project_site = models.CharField(max_length=100, blank=True, null=True)
    project_tor_amount = models.IntegerField(blank=True, null=True)
    project_now_amount = models.IntegerField(blank=True, null=True)
    level = models.ForeignKey(ProjectLevel, on_delete=models.SET_NULL, null=True)
    requirement = models.CharField(max_length=300, blank=True, null=True)
    certification = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=300, blank=True, null=True)
    datetime_add_project = models.DateTimeField(auto_now_add=True)
    datetime_update_project = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

    def diff_project_empty_amount(self):
        return self.project_tor_amount - self.project_now_amount



class Tor(models.Model):
    position_name = models.CharField(max_length=150, blank=True, null=True)
    position_type = models.CharField(max_length=50, blank=True, null=True)
    position_role_des = models.CharField(max_length=500, blank=True, null=True)
    position_edu_des = models.CharField(max_length=500, blank=True, null=True)
    position_exp_des = models.CharField(max_length=500, blank=True, null=True)
    position_tor_amount = models.IntegerField(blank=True, null=True)
    position_now_amount = models.IntegerField(blank=True, null=True)
    position_project = models.ManyToManyField(PositionProject,blank=True)
    datetime_add_position = models.DateTimeField(auto_now_add=True)
    datetime_update_position = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position_name

    def get_existing_project(self):
        existing = ProjectType.objects.filter(project_type_name='Existing Project').first()
        print(existing)
        existing_project = self.position_project.filter(project_type=existing)
        print(existing_project)
        return existing_project

    def get_forecast_project(self):
        forecast = ProjectType.objects.filter(project_type_name='Forecast Project').first()
        print(forecast)
        forecast_project = self.position_project.filter(project_type=forecast)
        print(forecast_project)
        return forecast_project

    def tor_amount(self):
        existing = ProjectType.objects.filter(project_type_name='Existing Project').first()
        sum_result = self.position_project.filter(project_type=existing).aggregate(Sum('project_tor_amount'))
        return sum_result

    def now_amount(self):
        existing = ProjectType.objects.filter(project_type_name='Existing Project').first()
        sum_result = self.position_project.filter(project_type=existing).aggregate(Sum('project_now_amount'))
        return sum_result

    def diff_empty_amount(self):
        existing = ProjectType.objects.filter(project_type_name='Existing Project').first()
        tor_amount = self.position_project.filter(project_type=existing).aggregate(Sum('project_tor_amount'))['project_tor_amount__sum']
        if not tor_amount:
            tor_amount = 0;
        now_amount = self.position_project.filter(project_type=existing).aggregate(Sum('project_now_amount'))['project_now_amount__sum']
        if not now_amount:
            now_amount = 0;
        diff = tor_amount - now_amount
        print(diff)
        return diff

# _________________________EDITED_______________________

class PositionAll(models.Model):
    position_id = models.CharField(max_length=5)
    position_name = models.CharField(max_length=150)

    def __str__(self):
        return self.position_name


class PositionField(models.Model):
    position_name = models.ForeignKey(PositionAll, on_delete=models.SET_NULL, null=True, related_name='Position_In_Project')
    position_type = models.CharField(max_length=50, blank=True, null=True)
    position_tor_amount = models.IntegerField(blank=True, null=True)
    position_now_amount = models.IntegerField(blank=True, null=True)
    datetime_add_position = models.DateTimeField(auto_now_add=True)
    datetime_update_position = models.DateTimeField(auto_now=True)
    requirement = models.CharField(max_length=300, blank=True, null=True)
    certification = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.position_name.position_name

    def diff_position_empty_amount(self):
        return self.position_tor_amount - self.position_now_amount

class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='Owner_Project')
    project_name = models.CharField(max_length=100, blank=True, null=True)
    project_type = models.ForeignKey(ProjectType, on_delete=models.SET_NULL, null=True)
    project_site = models.CharField(max_length=100, blank=True, null=True)
    level = models.ForeignKey(ProjectLevel, on_delete=models.SET_NULL, null=True)
    positions = models.ManyToManyField(PositionField,blank=True)
    datetime_add_project = models.DateTimeField(auto_now_add=True)
    datetime_update_project = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

    def get_position(self):
        position = self.positions.all()
        return position

    def tor_amount(self):
        print("_________________________________")
        sum_result = self.positions.all().aggregate(Sum('position_tor_amount'))
        print(sum_result)
        return sum_result

    def now_amount(self):
        sum_result = self.positions.all().aggregate(Sum('position_now_amount'))
        return sum_result

    def diff_empty_amount(self):
        # existing = ProjectType.objects.filter(project_type_name='Existing Project').first()
        tor_amount = self.positions.all().aggregate(Sum('position_tor_amount'))['position_tor_amount__sum']
        if not tor_amount:
            tor_amount = 0;
        now_amount = self.positions.all().aggregate(Sum('position_now_amount'))['position_now_amount__sum']
        if not now_amount:
            now_amount = 0;
        diff = tor_amount - now_amount
        print("DIFFFFF",diff)
        return diff
