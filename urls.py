from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from django.contrib import admin
from doua import settings
from doua import views
from search.views import search_func

admin.autodiscover()
urlpatterns = patterns('',
     ('^$', views.main),
     (r'^admin/', include(admin.site.urls)),
   #  (r'^search/', include('search.urls')),
     url(r'^search/', search_func, name='search'),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

)
