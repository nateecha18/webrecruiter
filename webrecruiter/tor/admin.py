from django.contrib import admin
from tor.models import ProjectType,ProjectLevel,PositionProject,Tor,PositionField,Project,PositionAll

# Register your models here.
admin.site.register(Tor)
admin.site.register(ProjectType)
admin.site.register(ProjectLevel)
admin.site.register(PositionProject)
admin.site.register(PositionField)
admin.site.register(Project)
admin.site.register(PositionAll)
