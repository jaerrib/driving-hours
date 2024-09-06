from django.contrib import admin

from .models import Drive, DrivingLog


class DrivingLogAdmin(admin.ModelAdmin):
    list_display = ["id", "creator"]


class DriveAdmin(admin.ModelAdmin):
    list_display = ["id", "date", "driving_log"]


admin.site.register(Drive, DriveAdmin)
admin.site.register(DrivingLog, DrivingLogAdmin)
