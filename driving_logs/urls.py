from django.urls import path

from .views import DrivingLogDetailView, DriveDetailView

urlpatterns = [
    path(
        "<uuid:pk>",
        DrivingLogDetailView.as_view(),
        name="driving_log_detail",
    ),
    path("drives/<uuid:pk>", DriveDetailView.as_view(), name="drive_detail"),
]
