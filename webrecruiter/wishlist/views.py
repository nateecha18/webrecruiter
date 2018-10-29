from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from account.models import Profile
from jobapply.models import CandidateBasic

from candidate_cart.extras import generate_order_id
from candidate_cart.models import OrderItem, Order
from request.models import Status,ProjectType,LevelRequest,Comment,RequestType,RequestCandidate,RequestInterview,Request
from request.generate_id import generate_request_id
from rolepermissions.decorators import has_role_decorator

from wishlist.models import WishlistItem,Wishlist
from wishlist.extras import generate_wishlist_item_id



@login_required()
def index(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    wishlist = Wishlist.objects.filter(owner=user_profile).first()

    context = {
        'WishlistDetail' : wishlist,
    }
    template = loader.get_template("wishlist.html")
    return HttpResponse(template.render(context, request))
    # return render('index.html', context_instance=RequestContext(request))

@login_required()
def add_to_wishlist(request, **kwargs):
    # get the user profile
    print(request.user)
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    candidate = CandidateBasic.objects.filter(id_number=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    print("Check1",request.user.profile.candidate.all())
    # Check if in ORDER
    # if candidate in request.user.profile.candidate.all():
    #     messages.info(request, 'You already own this candidate')
    #     return redirect(reverse('filter'))

    # create orderItem of the selected product
    wishlist_item = WishlistItem.objects.create(candidate=candidate,owner=user_profile)
    # create order associated with the user
    wishlist, status = Wishlist.objects.get_or_create(owner=user_profile)
    print("!!!",wishlist,status)
    print("Check2",wishlist.wishlist_items.filter(candidate=candidate))
    if wishlist.wishlist_items.filter(candidate=candidate):
        # Candidate in WishlistItem already
        messages.info(request, 'You already add this candidate to wishlist')
        return redirect(reverse('filter'))

    wishlist.wishlist_items.add(wishlist_item)
    if status:
        # generate a reference code
        wishlist.ref_code = generate_wishlist_item_id()
        wishlist.save()
    # show confirmation message and redirect back to the same page
    messages.info(request, "Candidate added to Wishlist")
    return redirect(reverse('filter'))

@login_required()
def delete_from_wishlist(request, item_id):
    user_profile = get_object_or_404(Profile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(owner=user_profile)
    selected_candidate = CandidateBasic.objects.filter(id_number=item_id).first()
    print(selected_candidate)
    selected_item = WishlistItem.objects.filter(candidate=selected_candidate,owner=user_profile)
    print(selected_item)
    print("Before delete : ",wishlist[0].wishlist_items.all())
    if selected_item.exists():
        item_to_delete = selected_item.last()
        wishlist[0].wishlist_items.remove(item_to_delete)
        print("Deleted! : ",wishlist[0].wishlist_items.all())
    return redirect(reverse('wishlist'))
