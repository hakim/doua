# Create your views here.
from new_drug.models import Drug
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf  import csrf_exempt, csrf_protect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


@csrf_exempt
def search(request):
    drugs = []
    if 'query' in request.GET:
        query = request.GET['query']
        if query != '':
           all_drugs = Drug.objects.all()
           for string in query.split():
               drugs = all_drugs.filter(Q(chemical_name__icontains = string)
                                        | Q(business_name__icontains = string)
                                        | Q(description__icontains = string))
    context = {
        'drugs' : drugs,
        'request' : request,
        }   
    return render_to_response(
        "search/results.html", 
        context,
        context_instance=RequestContext(request)
    )
