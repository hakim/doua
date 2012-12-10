# Create your views here.
from app.models import Drogs
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf  import csrf_exempt, csrf_protect
from django.http import HttpResponse


@csrf_exempt
def search_func(request):
    searched_name = request.POST['query']
    all = Drogs.objects.all()
    if searched_name in all:
        return HttpResponse("Drugs Exist")
    else
        return HttpResponse("Drug Doesn\'t exist ")
