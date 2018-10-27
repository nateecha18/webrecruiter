from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from account.models import Profile
from jobapply.models import CandidateBasic

from candidate_cart.extras import generate_order_id
from candidate_cart.models import OrderItem, Order, Interview

import datetime

def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    print(request.user)
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    candidate = CandidateBasic.objects.filter(id_number=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if candidate in request.user.profile.candidate.all():
        messages.info(request, 'You already own this candidate')
        return redirect(reverse('filter'))
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(candidate=candidate)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()
    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('filter'))


@login_required()
def delete_from_cart(request, item_id):
    user_profile = get_object_or_404(Profile, user=request.user)
    user_order = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    item = OrderItem.objects.filter(candidate=item_id)
    print("Before delete : ",user_order[0].items.all())
    if item.exists():
        item_to_delete = item[0]
        user_order[0].items.remove(item_to_delete)
        print("Deleted! : ",user_order[0].items.all())
    return redirect(reverse('candidate_cart:order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    cart_amount = ''
    if existing_order!=0:
        cart_amount = existing_order.items.all().count()

    context = {
        'order': existing_order,
        'Cart_amount': cart_amount,
    }
    return render(request, 'order_summary.html', context)


@login_required()
def create_interview(request):
    existing_order = get_user_pending_order(request)
    cart_amount = ''
    if existing_order!=0:
        cart_amount = existing_order.items.all().count()
    if request.method == 'POST':
        date_interview = request.POST.get('date_interview')
        user_profile = get_object_or_404(Profile, user=request.user)
        user_order = Order.objects.get(owner=user_profile, is_ordered=False)
        print(user_order,type(user_order))
        existing_order = get_user_pending_order(request)
        if existing_order!=0:
            interview_detail = Interview.objects.create(profile=user_profile, order_id=existing_order, date_interview=date_interview)
            context = {
                'order': existing_order,
                'Cart_amount': cart_amount,
            }

            return render(request, 'create-interview.html', context)
            # return redirect(reverse('candidate_cart:update_records',
            #             kwargs={
            #                 'order_id': user_order
            #             })
            #         )

    context = {
        'order': existing_order,
        'Cart_amount': cart_amount,
    }

    return render(request, 'create-interview.html', context)


@login_required()
def process_payment(request, order_id):
    # process the payment
    return redirect(reverse('shopping_cart:update_records',
                    kwargs={
                        'order_id' : order_id,
                    })
            )


@login_required()
def update_interview_records(request, order_id):
    # get the order being processed
    order_to_purchase = Order.objects.filter(pk=order_id).first()

    # update the placed order
    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.datetime.now()
    order_to_purchase.save()

    # get all items in the order - generates a queryset
    order_items = order_to_purchase.items.all()

    # update order items
    order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())

    # Add products to user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # get the products from the items
    order_products = [item.product for item in order_items]
    user_profile.ebooks.add(*order_products)
    user_profile.save()


    # =========== create a transaction =========

    # send an email to the customer
    # look at tutorial on how to send emails with sendgrid
    messages.info(request, "Thank you! Your purchase was successful!")
    return redirect(reverse('accounts:my_profile'))

#
# def success(request, **kwargs):
#     # a view signifying the transcation was successful
#     return render(request, 'shopping_cart/purchase_success.html', {})
