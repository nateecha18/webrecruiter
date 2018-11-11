from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Skill(models.Model):
    """docstring forCandidate_History_Education."""
    skill_name = models.CharField(max_length=50, blank=True, null=True)
    skill_type = models.CharField(max_length=50, blank=True, null=True)

    def __int__(self):
        return self.id

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    history = HistoricalRecords()
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.SET_NULL,null=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    history = HistoricalRecords()
