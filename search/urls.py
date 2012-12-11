from django.conf.urls.defaults import *
#from search import views

urlpatterns = patterns('search.views',
    # search url
    url(r'^$', search_func, name='search'),
)
