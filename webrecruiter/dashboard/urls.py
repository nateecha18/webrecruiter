from django.conf.urls import url
from . import views


from .views import HomeView, ChartData

urlpatterns = [
    url(r'^$', HomeView.as_view(),name="home"),
    url(r'^api/chart/data/$', ChartData.as_view(),name="api-chart-data"),
]
