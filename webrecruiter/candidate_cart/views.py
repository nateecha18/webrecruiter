from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from account.models import Profile
from jobapply.models import CandidateBasic

from candidate_cart.extras import generate_order_id
from candidate_cart.models import OrderItem, Order, InterviewStatus,InterviewStatusLog
from request.models import Status,Comment,RequestType,RequestCandidate,RequestInterview,Request,Position
from request.generate_id import generate_request_id
# import datetime
# from datetime import datetime,date,time,timedelta, timezone
from datetime import datetime


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
    # Check Candidate is in Interview process
    try:
        order_item = OrderItem.objects.get(candidate=candidate,owner=user_profile,is_ordered=True,is_interviewed=False)
    except OrderItem.DoesNotExist:
        order_item = None
    if order_item:
        messages.info(request, 'This Candidate is in the Interview Process')
        return redirect(reverse('filter'))

    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(candidate=candidate,owner=user_profile,is_ordered=False,is_interviewed=False)
    # ถ้าสร้าง Order_item ขึ้นมาใหม่
    # if status:
    interview_status = InterviewStatus.objects.filter(status_name='IN REVIEW').first()
    print(interview_status)
    order_item.interview_status = interview_status
    interview_status_log = InterviewStatusLog(updater=user_profile,interview_status=interview_status)
    interview_status_log.save()
    order_item.interview_status_log.add(interview_status_log)
    order_item.save()
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
    item = OrderItem.objects.filter(candidate=item_id,owner=user_profile,is_ordered=False,is_interviewed=False)
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
    positions = Position.objects.all()
    existing_order = get_user_pending_order(request)
    cart_amount = ''
    if existing_order!=0:
        cart_amount = existing_order.items.all().count()
    else:
        return redirect(reverse('candidate_cart:order_summary'))
    if request.method == 'POST':
        request_id = generate_request_id()
        request_title = request.POST.get('request_title')

        date_interview = request.POST.get('date_interview')
        note_interview = request.POST.get('note_interview')

        request_position_id = request.POST.get('request_position')
        request_position_other = request.POST.get('request_position_other_name')
        print(request_position_id,"||||||||||",request_position_other)
        request_position = get_object_or_404(Position, position_id=request_position_id)

        user_profile = get_object_or_404(Profile, user=request.user)
        user_order = Order.objects.get(owner=user_profile, is_ordered=False)

        status = get_object_or_404(Status, status_id='1')
        request_type = get_object_or_404(RequestType, request_type_id='2')

        existing_order = get_user_pending_order(request)
        if existing_order!=0:
            request_interview = RequestInterview(order = user_order,date_interview = date_interview,note_interview =note_interview)
            request_interview.save()

            request_detail = Request(request_id=request_id,request_type=request_type,request_interview=request_interview,request_title=request_title,request_position=request_position,request_position_other=request_position_other,owner=user_profile,status=status)
            request_detail.save()

            # context = {
            #     'order': existing_order,
            #     'Cart_amount': cart_amount,
            # }
            #
            # return render(request, 'create-interview.html', context)
            return redirect(reverse('candidate_cart:update_interview',
                        kwargs={
                            'order_id': user_order.ref_code
                        })
                    )

    context = {
        'Positions' : positions,
        'order': existing_order,
        'Cart_amount': cart_amount,
    }

    return render(request, 'create-interview.html', context)


# @login_required()
# def process_payment(request, order_id):
#     # process the payment
#     return redirect(reverse('shopping_cart:update_records',
#                     kwargs={
#                         'order_id' : order_id,
#                     })
#             )


@login_required()
def update_interview_records(request, order_id):
    # get the order being processed
    user_profile = get_object_or_404(Profile, user=request.user)

    order_to_interview = Order.objects.filter(ref_code=order_id).first()

    # update the placed order
    order_to_interview.is_ordered=True
    order_to_interview.date_ordered=datetime.datetime.now()
    order_to_interview.save()

    # get all items in the order - generates a queryset
    order_items = order_to_interview.items.all()

    # update order items
    interview_status = InterviewStatus.objects.filter(status_name='IN REQUEST').first()
    print(interview_status)
    order_items.update(is_ordered=True, interview_status=interview_status, date_ordered=datetime.datetime.now())

    # อัพเดต In Request ทุกๆ OrderItem ใน Order นี้
    interview_status_log = InterviewStatusLog(updater=user_profile,interview_status=interview_status)
    interview_status_log.save()
    for order_item in order_items:
        order_item.interview_status_log.add(interview_status_log)
        order_item.save()

    # # Add products to user profile
    # user_profile = get_object_or_404(Profile, user=request.user)
    # # get the products from the items
    # order_products = [item.candidate for item in order_items]
    # user_profile.candidate.add(*order_products)
    # user_profile.save()


    # =========== create a transaction =========

    # send an email to the customer
    # look at tutorial on how to send emails with sendgrid
    messages.info(request, "Thank you! Your purchase was successful!")
    return redirect(reverse('filter'))

#
# def success(request, **kwargs):
#     # a view signifying the transcation was successful
#     return render(request, 'shopping_cart/purchase_success.html', {})
