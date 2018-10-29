from __future__ import unicode_literals

from django.db import models

from account.models import Profile
from jobapply.models import CandidateBasic

class WishlistItem(models.Model):
    candidate = models.ForeignKey(CandidateBasic, on_delete=models.SET_NULL, null=True)
    date_wishlist_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.candidate.id_number)


class Wishlist(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)
    wishlist_items = models.ManyToManyField(WishlistItem, blank=True)

    def get_wishlist_items(self):
        return self.wishlist_items.all()

    def get_wishlist_candidate_skill(self,candidate_id):
        return self.wishlist_items.candidate.filter(id_number=candidate_id).first().candidate_computer_skill.tags.all()

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)
