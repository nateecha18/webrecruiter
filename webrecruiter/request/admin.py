from django.contrib import admin
from request.models import Status,Comment,RequestType,RequestCandidate,RequestInterview,Request,Position

admin.site.register(Status)
admin.site.register(Comment)
admin.site.register(RequestType)
admin.site.register(RequestCandidate)
admin.site.register(RequestInterview)
admin.site.register(Request)
admin.site.register(Position)
