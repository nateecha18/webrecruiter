from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='request_candidate'),
    url(r'^new_request/$', views.new_request, name='new_request_candidate'),
    url(r'^request_detail/(?P<request_id>[-\w]+)/$', views.request_detail, name='request_detail'),

]
