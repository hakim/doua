# Create your views here.
from app.models import Drogs
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf  import csrf_exempt, csrf_protect
from django.http import HttpResponse


@csrf_exempt
def add(request):
    r_name = request.POST['drog_name']
    c_name = request.POST['drog_chemical']
    drog_instance = Drogs()
    drog_instance.Drog_Chemical = c_name
    drog_instance.Drog_Name = r_name
    drog_instance.save()
    all = Drogs.objects.all()
    return render_to_response("index.html",{'list_drogs':all},
    )