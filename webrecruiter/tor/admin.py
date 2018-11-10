from django.contrib import admin
from tor.models import ProjectType,ProjectLevel,PositionProject,Tor

# Register your models here.
admin.site.register(Tor)
admin.site.register(ProjectType)
admin.site.register(ProjectLevel)
admin.site.register(PositionProject)
