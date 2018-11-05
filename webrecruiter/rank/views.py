from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import View
from rank.models import CandidateRank
from jobapply.models import CandidateBasic
from candidate_cart.models import OrderItem,Order
from wishlist.models import WishlistItem,Wishlist
from rolepermissions.decorators import has_role_decorator
import datetime
from datetime import datetime,date,time,timedelta, timezone
import pytz
import math

@has_role_decorator('hr')
def get_rank(request):
    # get order for the correct user
    wishlists = Wishlist.objects.all()
    print(wishlists)
    for wishlist in wishlists:
        wishlist_items = wishlist.wishlist_items.all()
        owner = wishlist.owner
        print(owner)
        for wishlist_item in wishlist_items:
            print(wishlist_item)
            candidate = CandidateBasic.objects.filter(id_number=wishlist_item.candidate.id_number).first()
            if candidate:
                candidate_rank = CandidateRank.objects.get_or_create(candidate = candidate)[0]
                # candidate_rank.owner.clear()
                candidate_rank.owner.add(owner)
                count = candidate_rank.owner.count()
                candidate_rank.count = count
                candidate_rank.save()
                print("ALL OWNER",candidate_rank.owner.all())
    ranks = CandidateRank.objects.all().order_by('-count')
    return ranks

@has_role_decorator('hr')
def get_rank_filter(request,day):
    # get order for the correct user
    date_from = datetime.now() - timedelta(days=day)
    wishlists = Wishlist.objects.all()
    print(wishlists)
    for wishlist in wishlists:
        wishlist_items = wishlist.wishlist_items.all()
        owner = wishlist.owner
        print(owner)
        for wishlist_item in wishlist_items:
            print(wishlist_item)
            candidate = CandidateBasic.objects.filter(id_number=wishlist_item.candidate.id_number,date_apply__gte=date_from).first()
            if candidate:
                candidate_rank = CandidateRank.objects.get_or_create(candidate = candidate)[0]
                # candidate_rank.owner.clear()
                candidate_rank.owner.add(owner)
                count = candidate_rank.owner.count()
                candidate_rank.count = count
                candidate_rank.save()
                print("ALL OWNER",candidate_rank.owner.all())
    ranks = CandidateRank.objects.all().order_by('-count')
    return ranks

@has_role_decorator('hr')
def index(request):
    CandidateRank.objects.all().delete()
    ranks = get_rank(request)

    print(ranks,"Rank")
    topthree = ranks[:3]
    context = {
        'ranks' : ranks,
        'topthree' : topthree,
    }
    template = loader.get_template("rank.html")
    return HttpResponse(template.render(context, request))

@has_role_decorator('hr')
def rank_filter_day(request, ranks_day):
    CandidateRank.objects.all().delete()
    day = int(ranks_day)
    ranks = get_rank_filter(request,day)

    print(ranks,"Rank")
    topthree = ranks[:3]
    context = {
        'ranks' : ranks,
        'topthree' : topthree,
    }
    template = loader.get_template("rank.html")
    return HttpResponse(template.render(context, request))
