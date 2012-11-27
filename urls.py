from django.conf.urls.defaults import *
from django.contrib import admin
from doua import settings
from doua import views

admin.autodiscover()

urlpatterns = patterns('',
     ('^$', views.main),
     (r'^admin/', include(admin.site.urls)),
    # (r'^thoughts/', include('thoughts.urls')),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

)
