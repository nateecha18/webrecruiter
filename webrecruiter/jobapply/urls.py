from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^pdf/$', views.GeneratePdf.as_view()),
    url(r'^show/$', views.show_list),
    url(r'^api/get_institute/', views.get_institute, name='get_institute'),
    url(r'^check_idnumber/', views.check_idnumber, name='check_idnumber'),


]
