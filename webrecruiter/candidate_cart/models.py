from __future__ import unicode_literals

from django.db import models

from account.models import Profile
from jobapply.models import CandidateBasic

class InterviewStatus(models.Model):
    status_id = models.CharField(max_length=4,primary_key=True)
    status_name = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.status_name

class InterviewStatusLog(models.Model):
    updater = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    interview_status = models.ForeignKey(InterviewStatus, on_delete=models.SET_NULL, null=True)
    datetime_update_status = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.id,self.updater,self.interview_status.status_name)

class OrderItem(models.Model):
    candidate = models.ForeignKey(CandidateBasic, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    is_interviewed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True,blank=True)
    interview_status = models.ForeignKey(InterviewStatus, on_delete=models.SET_NULL, null=True, blank=True)
    interview_status_log = models.ManyToManyField(InterviewStatusLog, blank=True)

    def __str__(self):
        return '{0} - {1} - isO:{2} - isI:{3}'.format(self.candidate.id_number,self.owner,self.is_ordered,self.is_interviewed)

    def get_interview_log(self):
        return self.interview_status_log.all()


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)

#
# class Interview(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     order_id = models.CharField(max_length=120)
#     date_interview = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.order_id
    #
    # class Meta:
    #     ordering = ['-timestamp']
