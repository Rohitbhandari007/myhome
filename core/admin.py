from django.contrib import admin
from .models import *
from django.contrib import admin


class RoomInline(admin.TabularInline):
    model = Room


class LightInline(admin.TabularInline):
    model = Light


class HomeAdmin(admin.ModelAdmin):
    inlines = [
        RoomInline,
    ]
    list_display = ["id", "name", "created"]


class RoomAdmin(admin.ModelAdmin):
    inlines = [
        LightInline,
    ]
    list_display = ["id", "name", "home", "created"]


admin.site.register(Home, HomeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(LightningConfigurations)
admin.site.register(LightningScenes)
