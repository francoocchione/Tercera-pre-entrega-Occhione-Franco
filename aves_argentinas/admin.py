from django.contrib import admin
from aves_argentinas.models import Aves, Fauna, Flora
# Register your models here.
admin.site.register(Aves)
admin.site.register(Fauna)
admin.site.register(Flora)