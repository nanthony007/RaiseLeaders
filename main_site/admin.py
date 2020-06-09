from django.contrib import admin
from main_site.models import Event, Resource, AttendanceTracker


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'class_code', 'class_date', 'class_title')


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'difficulty', 'belt_level', 'curriculum')


class AttendanceTrackerAdmin(admin.ModelAdmin):
    list_display = ('event', 'attendee', 'is_attending')


admin.site.register(Event, EventAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(AttendanceTracker, AttendanceTrackerAdmin)
