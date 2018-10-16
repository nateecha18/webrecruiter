from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^pdf/$', views.GeneratePdf.as_view()),
    url(r'^show/$', views.show_list),

]
