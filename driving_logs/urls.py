from django.urls import path

from .views import (
    DrivingLogDetailView,
    DrivingLogCreateView,
    DrivingLogUpdateView,
    DrivingLogDeleteView,
    DrivingLogListView,
    DriveDetailView,
    DriveCreateView,
    DriveUpdateView,
    DriveDeleteView,
)

urlpatterns = [
    path("new/", DrivingLogCreateView.as_view(), name="driving_log_new"),
    path("<uuid:pk>/edit/", DrivingLogUpdateView.as_view(), name="driving_log_edit"),
    path(
        "<uuid:pk>/delete/", DrivingLogDeleteView.as_view(), name="driving_log_delete"
    ),
    path("<uuid:pk>/", DrivingLogDetailView.as_view(), name="driving_log_detail"),
    path("", DrivingLogListView.as_view(), name="driving_log_list"),
    path("drives/<uuid:pk>/", DriveDetailView.as_view(), name="drive_detail"),
    path("<uuid:pk>/drives/new/", DriveCreateView.as_view(), name="drive_new"),
    path("drives/<uuid:pk>/edit/", DriveUpdateView.as_view(), name="drive_edit"),
    path("drives/<uuid:pk>/delete/", DriveDeleteView.as_view(), name="drive_delete"),
]
