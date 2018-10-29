from django.conf.urls import url
from . import views
# from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='wishlist'),
    url(r'^add-to-wishlist/(?P<item_id>[-\w]+)/$', views.add_to_wishlist, name="add_to_wishlist"),
    url(r'^delete-from-wishlist/(?P<item_id>[-\w]+)/$', views.delete_from_wishlist, name='delete_from_wishlist'),

]
