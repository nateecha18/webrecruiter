from django.contrib import admin
from candidate_cart.models import OrderItem, Order, Interview

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Interview)
