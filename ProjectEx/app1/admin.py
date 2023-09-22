from django.contrib import admin

# Register your models here.

from .models import Userinfo 

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ['name','email','address']
    
