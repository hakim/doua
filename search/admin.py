from django.contrib import admin
from new_drug.models import *

admin.site.unregister(Drug)
admin.site.register(Drug)

