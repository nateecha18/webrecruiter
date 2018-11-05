from django.conf.urls import url
from . import views

# from .views import HomeView, ChartData

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^submit_skill/$', views.submit_skill),
    url(r'^skill/create/$', views.create_skill),
    url(r'^skill/show/$', views.show_skill,name="show_skill"),

    # url(r'^chart/$', HomeView.as_view(),name="home"),
    # url(r'^api/data/$', get_data,name="api-data"),
    # url(r'^api/chart/data/$', ChartData.as_view(),name="api-chart-data"),
    # url(r'^admin/$', admin.site.urls),

]
