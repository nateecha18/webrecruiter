from django.db import models

# Create your models here.
class FilterPosition(models.Model):
    """docstring forCandidate_History_Education."""
    checkbox_position = models.CharField(max_length=50, blank=True, null=True)
    operator_position = models.CharField(max_length=250, blank=True, null=True)
    filter_position = models.CharField(max_length=250, blank=True, null=True)

    def __int__(self):
        return self.id
