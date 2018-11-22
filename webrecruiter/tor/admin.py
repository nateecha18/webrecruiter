from django.contrib import admin
from tor.models import ProjectType,ProjectLevel,PositionField,Project,PositionAll

# Register your models here.
admin.site.register(ProjectType)
admin.site.register(ProjectLevel)
admin.site.register(PositionField)
admin.site.register(Project)
admin.site.register(PositionAll)
