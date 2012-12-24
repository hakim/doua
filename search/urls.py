from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'results$', 'search.views.search', name='search_drug'),
)
