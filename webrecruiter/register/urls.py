from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.UserFormView.as_view(), name='register'),
    # url(r'^submit_filter/$', views.submit_filter),

]
