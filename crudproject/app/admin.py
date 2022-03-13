from django.contrib import admin
# Register your models here.
from .models import userpost

class Userdata(admin.ModelAdmin):
    list_display=[ 'name','id','mobile',"date_created"]
admin.site.register(userpost,Userdata)

