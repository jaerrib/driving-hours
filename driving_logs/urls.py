from django.urls import path

from .views import (
    DrivingLogDetailView,
    DrivingLogListView,
    DriveDetailView,
    DriveCreateView,
)

urlpatterns = [
    path(
        "<uuid:pk>",
        DrivingLogDetailView.as_view(),
        name="driving_log_detail",
    ),
    path(
        "",
        DrivingLogListView.as_view(),
        name="driving_log_list",
    ),
    path("drives/<uuid:pk>", DriveDetailView.as_view(), name="drive_detail"),
    path(
        "<uuid:pk>/drives/new/",
        DriveCreateView.as_view(),
        name="drive_new",
    ),
]
