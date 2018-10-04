from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from account.models import Profile
from jobapply.models import CandidateBasic

from candidate_cart.extras import generate_order_id
from candidate_cart.models import OrderItem, Order

import datetime

# def get_user_pending_order(request):
#     # get order for the correct user
#     user_profile = get_object_or_404(Profile, user=request.user)
#     order = Order.objects.filter(owner=user_profile, is_ordered=False)
#     if order.exists():
#         # get the only order in the list of filtered orders
#         return order[0]
#     return 0


@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    print("Entry1")
    print("Entry2")
    print(request.user)
    user_profile = get_object_or_404(Profile, user=request.user)
    print("Entry2")
    # filter products by id
    candidate = CandidateBasic.objects.filter(id_number=kwargs.get('item_id', "")).first()
    print("Entry3")
    print("candidate:",candidate,"All :", request.user.profile.candidate.all())
    # check if the user already owns this product
    if candidate in request.user.profile.candidate.all():
        print("Entry4")
        messages.info(request, 'You already own this candidate')
        return redirect(reverse('filter'))
    print("Entry5")
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(candidate=candidate)
    print("Entry6")
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    print("Entry7")
    user_order.items.add(order_item)
    print("Entry8")
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()
        print("Entry9")
    print("Entry10")

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    print("Entry11")
    return redirect(reverse('filter'))

#
# @login_required()
# def delete_from_cart(request, item_id):
#     item_to_delete = OrderItem.objects.filter(pk=item_id)
#     if item_to_delete.exists():
#         item_to_delete[0].delete()
#         messages.info(request, "Item has been deleted")
#     return redirect(reverse('shopping_cart:order_summary'))
#
#
# @login_required()
# def order_details(request, **kwargs):
#     existing_order = get_user_pending_order(request)
#     context = {
#         'order': existing_order
#     }
#     return render(request, 'shopping_cart/order_summary.html', context)
#
#
# @login_required()
# def checkout(request):
#     existing_order = get_user_pending_order(request)
#     context = {
#         'order': existing_order,
#     }
#
#     return render(request, 'shopping_cart/checkout.html', context)
#
# @login_required()
# def process_payment(request, order_id):
#     # process the payment
#     return redirect(reverse('shopping_cart:update_records',
#                     kwargs={
#                         'order_id' : order_id,
#                     })
#             )
#
#
# @login_required()
# def update_transaction_records(request, order_id):
#     # get the order being processed
#     order_to_purchase = Order.objects.filter(pk=order_id).first()
#
#     # update the placed order
#     order_to_purchase.is_ordered=True
#     order_to_purchase.date_ordered=datetime.datetime.now()
#     order_to_purchase.save()
#
#     # get all items in the order - generates a queryset
#     order_items = order_to_purchase.items.all()
#
#     # update order items
#     order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())
#
#     # Add products to user profile
#     user_profile = get_object_or_404(Profile, user=request.user)
#     # get the products from the items
#     order_products = [item.product for item in order_items]
#     user_profile.ebooks.add(*order_products)
#     user_profile.save()
#
#
#     # =========== create a transaction =========
#
#     # send an email to the customer
#     # look at tutorial on how to send emails with sendgrid
#     messages.info(request, "Thank you! Your purchase was successful!")
#     return redirect(reverse('accounts:my_profile'))
#
#
# def success(request, **kwargs):
#     # a view signifying the transcation was successful
#     return render(request, 'shopping_cart/purchase_success.html', {})
