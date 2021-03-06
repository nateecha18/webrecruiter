from django.db import models
from jobapply.models import CandidateBasic
from account.models import Profile
from candidate_cart.models import OrderItem,Order
from tor.models import ProjectType,ProjectLevel,PositionField,Project,PositionAll

# Create your models here.
class Status(models.Model):
    status_id = models.CharField(max_length=15)
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name

class Comment(models.Model):
    comment_id = models.CharField(max_length=40)
    comment_title = models.CharField(max_length=100, null=True, blank=True)
    comment_detail = models.CharField(max_length=250)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True) # hr ที่สร้าง comment
    datetime_comment = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.comment_id

class RequestType(models.Model):
    request_type_id = models.CharField(max_length=5)
    request_type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.request_type_id

class UpdateAmountLog(models.Model):
    added_amount = models.IntegerField(blank=True, null=True)
    datetime_add_amount = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return 'เพิ่ม - {0}คน'.format(self.added_amount)

class RequestCandidate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(PositionField, on_delete=models.SET_NULL, null=True)
    tor_employee_amount = models.IntegerField(blank=True, null=True)
    now_employee_amount = models.IntegerField(blank=True, null=True)
    empty_employee_amount = models.IntegerField(blank=True, null=True)
    requirement = models.CharField(max_length=250, blank=True, null=True)
    certification = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=250, blank=True, null=True)
    update_amount_log = models.ManyToManyField(UpdateAmountLog,blank=True)
    is_full = models.BooleanField(default=False)

    def __int__(self):
        return self.id
    def diff_empty_amount(self):
        return self.tor_employee_amount - self.now_employee_amount
    def diff_empty_amount_now(self):
        update_amount_log_all = self.update_amount_log.all()
        empty_amount_now = self.empty_employee_amount
        for log in update_amount_log_all:
            empty_amount_now -= log.added_amount
        print("empty_amount_now!!!",empty_amount_now)
        return empty_amount_now

class RequestInterview(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    date_interview = models.CharField(max_length=100)
    note_interview = models.CharField(max_length=100)

    def __str__(self):
        return '{0} - {1}'.format(self.order.owner, self.order.ref_code)

class Request(models.Model):
    request_id = models.CharField(max_length=15)
    request_type = models.ForeignKey(RequestType, on_delete=models.SET_NULL, null=True)
    request_interview = models.OneToOneField(RequestInterview, on_delete=models.SET_NULL, null=True,blank=True)
    request_candidate = models.OneToOneField(RequestCandidate, on_delete=models.SET_NULL, null=True,blank=True)
    request_title = models.CharField(max_length=200, blank=True, null=True)
    request_position = models.ForeignKey(PositionAll, on_delete=models.SET_NULL, null=True, blank=True)
    request_position_other = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='creator') # คน Request
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    datetime_add_request = models.DateTimeField(auto_now_add=True)
    datetime_update_request = models.DateTimeField(auto_now=True)
    comment = models.ManyToManyField(Comment,blank=True) # Comment
    last_comment_owner = models.ForeignKey(Profile, on_delete=models.SET_NULL,blank=True, null=True, related_name='last_updater') # เจ้าของ comment ล่าสุด

    class Meta:
        ordering = ['datetime_add_request']

    def __str__(self):
        return self.request_id
