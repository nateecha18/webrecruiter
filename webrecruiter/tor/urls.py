from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='tor_management'),
    url(r'^update-tor/(?P<tor_id>[-\w]+)/$', views.update_tor, name='update_tor'),

]
