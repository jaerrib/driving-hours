import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class DrivingLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_hours_needed = models.IntegerField(default=0)
    night_hours_needed = models.IntegerField(default=0)
    inclement_weather_hours_needed = models.IntegerField(default=0)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("driving_log_detail", args=[str(self.id)])


class Drive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now=False, auto_now_add=True)
    hours = models.IntegerField(default=0, blank=True, null=True)
    minutes = models.IntegerField(default=0, blank=True, null=True)
    night = models.BooleanField(default=False)
    inclement_weather = models.BooleanField(default=False)
    driving_log = models.ForeignKey(DrivingLog, on_delete=models.CASCADE)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("drive_detail", args=[str(self.id)])
