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
from rolepermissions.decorators import has_role_decorator


@has_role_decorator('hr')
def index(request):
    CandidateRank.objects.all().delete()
    orders = Order.objects.all()
    for order in orders:
        items = order.items.all()
        owner = order.owner
        print(owner)
        for item in items:
            print(item)
            candidate = CandidateBasic.objects.filter(id_number=item).first()
            candidate_rank = CandidateRank.objects.get_or_create(candidate = candidate)[0]
            count = candidate_rank.count + 1
            candidate_rank.owner.add(owner)
            print(owner,item,"=","Counted",count)
            CandidateRank.objects.filter(candidate=candidate).update(count=count)
            print("ALL OWNER",candidate_rank.owner.all())
    ranks = CandidateRank.objects.all().order_by('-count')
    context = {
        'ranks' : ranks,
    }
    template = loader.get_template("rank.html")
    return HttpResponse(template.render(context, request))
    # return render('index.html', context_instance=RequestContext(request))
