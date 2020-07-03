from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, User
# Register your models here.


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ['name', 'location']


@admin.register(User)
class UserAdmin(OSMGeoAdmin):
    list_display = ['name', 'location']