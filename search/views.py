# Create your views here.
from new_drug.models import Drug
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf  import csrf_exempt, csrf_protect
from django.http import HttpResponse


@csrf_exempt


def search_func(request):
    searched_name = request.POST['query']
    all = Drug.objects.all()
    if Drug.objects.filter(business_name__iexact=searched_name) or Drug.objects.filter(chemical_name__iexact=searched_name):
        return HttpResponse("Drug Exist")
    else:
        return HttpResponse("Drug doesn\'t Exist")
