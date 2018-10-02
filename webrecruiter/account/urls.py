from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.login_view, name='account'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),

    # url(r'^submit_filter/$', views.submit_filter),

]
