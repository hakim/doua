# Create your views here.
from new_drug.models import Drug
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf  import csrf_exempt, csrf_protect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt


def search_func(request):
    searched_name = request.POST['query']
    all = Drug.objects.all()
    if Drug.objects.filter(business_name__iexact=searched_name) :
       d1 =  Drug.objects.get(business_name__iexact=searched_name)
    else:
       d1 = "Drug  doesn't exist."
    return render_to_response("result_search.html", {'Searched_drugs':d1},context_instance=RequestContext(request)  )
