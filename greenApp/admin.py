from django.contrib import admin
from .models import *

class DataAdmin(admin.ModelAdmin):
    date_hierarchy="datetime"
    list_display = ("id","datetime",)
    

# Register your models here.
admin.site.register(esp)
admin.site.register(data,DataAdmin)

