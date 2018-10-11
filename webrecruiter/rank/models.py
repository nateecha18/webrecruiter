from django.db import models
from jobapply.models import CandidateBasic
from account.models import Profile

# Create your models here.
class CandidateRank(models.Model):
    """docstring forCandidate_History_Education."""
    candidate = models.OneToOneField(CandidateBasic, on_delete=models.SET_NULL, null=True)
    # candidate = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True,default=0)
    owner = models.ManyToManyField(Profile)


    def __str__(self):
        return self.candidate.id_number

    def get_candidate_owner(self):
        print("_____________________",self.owner.all())
        return self.owner.all()
