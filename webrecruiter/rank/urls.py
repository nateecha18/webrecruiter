from django.conf.urls import url
from . import views
# from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='rank'),
    url(r'^(?P<ranks_day>[-\w]+)/$', views.rank_filter_day, name='rank_filter_day'),

]
