from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^submit_skill/$', views.submit_skill),
    url(r'^skill/create/$', views.create_skill),
    url(r'^skill/show/$', views.show_skill,name="show_skill"),


]
