from django.contrib import admin
from request.models import Status,ProjectType,LevelRequest,Comment,RequestType,RequestCandidate,RequestInterview,Request

admin.site.register(Status)
admin.site.register(Comment)
admin.site.register(ProjectType)
admin.site.register(LevelRequest)
admin.site.register(RequestType)
admin.site.register(RequestCandidate)
admin.site.register(RequestInterview)
admin.site.register(Request)