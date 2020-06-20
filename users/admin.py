from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_user_name', 'get_attendance', 'get_user_email', 'belt', 'joined')


    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_user_name.short_description = 'User Full Name'
    get_user_name.admin_order_field = '-user__first_name'


    def get_user_email(self, obj):
        return f"{obj.user.email}"
    get_user_email.short_description = 'User Email'
    get_user_email.admin_order_field = '-user__email'

    def get_attendance(self, obj):
        return obj.user.attending.count()
    get_attendance.short_description = 'User Attendance Count'
    get_attendance.admin_order_field = '-user__attending'

admin.site.register(Profile, ProfileAdmin)
