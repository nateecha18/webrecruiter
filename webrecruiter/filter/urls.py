from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

# from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='filter'),
    url(r'^testajax/$', views.test_ajax,name="test_ajax"),
    url(r'^(?P<candidate_id>[-\w]+)/$', views.candidate_detail, name="candidate_detail"),
    url(r'^download_resume/(?P<selected_candidate>[-\w]+)/$', views.download_resume, name="download_resume"),
    url(r'^download_transcript/(?P<selected_candidate>[-\w]+)/$', views.download_transcript, name="download_transcript"),


]
