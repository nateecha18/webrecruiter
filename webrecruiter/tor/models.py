from django.db import models

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
    project_type = models.CharField(max_length=100, blank=True, null=True)
    project_site = models.CharField(max_length=100, blank=True, null=True)
    tor_employee_amount = models.IntegerField(blank=True, null=True)
    now_employee_amount = models.IntegerField(blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True)
    requirement = models.CharField(max_length=300, blank=True, null=True)
    certification = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.position_name



class Tor(models.Model):
    position_name = models.CharField(max_length=50, blank=True, null=True)
    position_type = models.CharField(max_length=50, blank=True, null=True)
    # แผนก
    job_section = models.CharField(max_length=50, blank=True, null=True)
    # ฝ่าย
    job_field = models.CharField(max_length=50, blank=True, null=True)
    position_tor_amount = models.IntegerField(blank=True, null=True)
    position_now_amount = models.IntegerField(blank=True, null=True)
    position_project = models.ManyToManyField(PositionProject,blank=True)

    def __str__(self):
        return self.position_name

    def diff_empty_amount(self):
        return self.position_tor_amount - self.position_now_amount
