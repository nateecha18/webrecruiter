from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit_applyjob/$', views.submit_applyjob),
]
