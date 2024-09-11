from django.urls import path

from .views import (
    DrivingLogDetailView,
    DrivingLogCreateView,
    DrivingLogListView,
    DriveDetailView,
    DriveCreateView,
    DriveUpdateView,
    DriveDeleteView,
)

urlpatterns = [
    path("new/", DrivingLogCreateView.as_view(), name="driving_log_new"),
    path("<uuid:pk>/", DrivingLogDetailView.as_view(), name="driving_log_detail"),
    path("", DrivingLogListView.as_view(), name="driving_log_list"),
    path("drives/<uuid:pk>/", DriveDetailView.as_view(), name="drive_detail"),
    path("<uuid:pk>/drives/new/", DriveCreateView.as_view(), name="drive_new"),
    path("drives/<uuid:pk>/edit/", DriveUpdateView.as_view(), name="drive_edit"),
    path("drives/<uuid:pk>/edit/", DriveDeleteView.as_view(), name="drive_delete"),
]
