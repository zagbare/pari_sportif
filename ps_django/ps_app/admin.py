from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name' ,'lastname','email','contacts','password','status','register_date')
    list_filter = ("register_date","status",)
    search_fields = ('name' ,'lastname',)
    list_per_page = 50

@admin.register(Paries)
class PariesAdmin(admin.ModelAdmin):
    list_display = ('equipeA' ,'score','scoreB','equipeB','montant_parié','date_match','date_parie',)
    list_filter = ("date_parie",)
    search_fields = ('score',)
    list_per_page = 50
