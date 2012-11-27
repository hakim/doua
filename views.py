from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required


@csrf_exempt
def main(request):
   return render_to_response ( 
        'index.html',
        {
         'is_authenticated' : request.user.is_authenticated(),
        },
        context_instance = RequestContext(request)
        )

