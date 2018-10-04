from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='filter'),
    url(r'^(?P<candidate_id>[-\w]+)/$', views.candidate_detail, name="candidate_detail"),

]
