from __future__ import unicode_literals

from django.db import models

from account.models import Profile
from jobapply.models import CandidateBasic

class OrderItem(models.Model):
    candidate = models.OneToOneField(CandidateBasic, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.candidate.id_number


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


class Interview(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120)
    date_interview = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id
    #
    # class Meta:
    #     ordering = ['-timestamp']
