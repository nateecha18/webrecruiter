from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='filter'),
    url(r'^add_to_cart/$', views.add_to_cart),
    # url(r'^submit_filter/$', views.submit_filter),

]
