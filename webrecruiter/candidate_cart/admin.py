from django.contrib import admin
from candidate_cart.models import OrderItem, Order, InterviewStatus,InterviewStatusLog

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(InterviewStatus)
admin.site.register(InterviewStatusLog)
