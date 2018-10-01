from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='filter'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', login, {'template_name' : 'login.html'}),
    # url(r'^submit_filter/$', views.submit_filter),

]
