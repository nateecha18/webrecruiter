from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='request'),
    url(r'^new_request_candidate/$', views.new_request_candidate, name='new_request_candidate'),
    url(r'^request_detail/(?P<request_id>[-\w]+)/$', views.request_detail, name='request_detail'),
    url(r'^show_close_request/$', views.show_close_request, name='show_close_request'),
    url(r'^show_open_request/$', views.show_open_request, name='show_open_request'),
    url(r'^interview/$', views.request_interview, name='request_interview'),
    url(r'^show_close_request_interview/$', views.show_close_request_interview, name='show_close_request_interview'),
    url(r'^show_open_request_interview/$', views.show_open_request_interview, name='show_open_request_interview'),
    url(r'^candidate/$', views.request_candidate, name='request_candidate'),
    url(r'^show_close_request_candidate/$', views.show_close_request_candidate, name='show_close_request_candidate'),
    url(r'^show_open_request_candidate/$', views.show_open_request_candidate, name='show_open_request_candidate'),
    url(r'^get_position/(?P<project_id>[-\w]+)/$', views.get_position, name='get_position'),
    url(r'^get_position_detail/(?P<position_id>[-\w]+)/$', views.get_position_detail, name='get_position_detail'),




]
