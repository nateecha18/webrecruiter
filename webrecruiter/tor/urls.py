from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='tor_management'),
    url(r'^update-project/(?P<project_id>[-\w]+)/$', views.update_project, name='update_project'),
    url(r'^create-project/(?P<position_id>[-\w]+)/$', views.create_project, name='create_project'),
    url(r'^delete-project/(?P<position_id>[-\w]+)/(?P<project_id>[-\w]+)/$', views.delete_project, name='delete_project'),

]
