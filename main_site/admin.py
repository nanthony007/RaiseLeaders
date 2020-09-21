from django.contrib import admin
from main_site.models import Event, Resource, NinjaItem


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ("class_id", "class_title", "class_date", "class_code")


class ResourceAdmin(admin.ModelAdmin):
    list_display = ("category", "title", "difficulty", "belt_level", "curriculum")


class NinjaItemAdmin(admin.ModelAdmin):
    list_display = ("text", "date", "media")


admin.site.register(Event, EventAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(NinjaItem, NinjaItemAdmin)
