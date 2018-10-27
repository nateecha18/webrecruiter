from django.contrib import admin
from candidate_cart.models import OrderItem, Order

admin.site.register(OrderItem)
admin.site.register(Order)
