from django.db import models

# Create your models here.
class CandidateRank(models.Model):
    """docstring forCandidate_History_Education."""
    candidate = models.CharField(max_length=50, blank=True, null=True)
    count = models.CharField(max_length=50, blank=True, null=True)

    def __int__(self):
        return self.candidate
