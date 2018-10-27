from django.conf.urls import url
from . import views


from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    create_interview,
    update_interview_records,
    # success
)

app_name = 'candidate_cart'

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    # url(r'^success/$', success, name='purchase_success'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^create-interview/$', create_interview, name='create_interview'),
    # url(r'^payment/(?P<order_id>[-\w]+)/$', process_payment, name='process_payment'),
    url(r'^update-interview/(?P<order_id>[-\w]+)/$', update_interview_records,
        name='update_interview')
]
