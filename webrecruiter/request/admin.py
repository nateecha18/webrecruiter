from django.contrib import admin
from request.models import Status,ProjectType,LevelRequest,Comment,RequestCandidate

admin.site.register(Status)
admin.site.register(Comment)
admin.site.register(RequestCandidate)
admin.site.register(ProjectType)
admin.site.register(LevelRequest)
