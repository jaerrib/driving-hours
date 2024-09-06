from django.views.generic import DetailView

from .models import Drive, DrivingLog


class DrivingLogDetailView(DetailView):
    model = DrivingLog
    template_name = "driving_logs/driving_log.html"


class DriveDetailView(DetailView):
    model = Drive
    template_name = "driving_logs/drive_detail.html"
