from django.db import models

# Create your models here.
class Skill(models.Model):
    """docstring forCandidate_History_Education."""
    skill_name = models.CharField(max_length=50, blank=True, null=True)
    skill_type = models.CharField(max_length=50, blank=True, null=True)

    def __int__(self):
        return self.id
