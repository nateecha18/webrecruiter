from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from addskill.models import Skill, Poll, Choice

# Register your models here.
admin.site.register(Skill)

admin.site.register(Poll, SimpleHistoryAdmin)
admin.site.register(Choice, SimpleHistoryAdmin)
