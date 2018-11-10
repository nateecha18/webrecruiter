from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='tor_management'),
    url(r'^update-project/(?P<project_id>[-\w]+)/$', views.update_project, name='update_project'),

]
