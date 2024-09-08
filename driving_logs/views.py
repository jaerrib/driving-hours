from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import (
    DriveCreateForm,
)
from .models import Drive, DrivingLog


class DrivingLogListView(LoginRequiredMixin, ListView):
    model = DrivingLog
    template_name = "driving_logs/driving_log_list.html"

    def get_queryset(self):
        return DrivingLog.objects.filter(creator=self.request.user.pk)


class DriveDetailView(DetailView):
    model = Drive
    template_name = "driving_logs/drive_detail.html"


class DrivingLogDetailView(LoginRequiredMixin, DetailView):
    model = DrivingLog
    template_name = "driving_logs/driving_log_detail.html"
    context_object_name = "drive_list"
    pk_url_kwarg = "pk"

    def test_func(self):
        driving_log = self.get_object()
        return driving_log.creator == self.request.user

    def get_queryset(self):
        return DrivingLog.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        driving_log = self.get_object()
        context["drive_list"] = Drive.objects.filter(driving_log=driving_log)
        context["driving_log_pk"] = driving_log.pk
        return context


class DriveCreateView(CreateView):
    model = Drive
    form_class = DriveCreateForm
    template_name = "driving_logs/drive_new.html"
    context_object_name = "driving_log"
    pk_url_kwarg = "driving_log_pk"

    def get_success_url(self):
        driving_log_pk = self.object.driving_log_id
        return reverse("driving_log_detail", kwargs={"pk": driving_log_pk})

    def get_redirect_url(self, param):
        return reverse_lazy("driving_log_detail", kwargs={"param": param})

    def get_queryset(self):
        return DrivingLog.objects.filter(pk=self.kwargs["driving_log_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = DriveCreateForm()
        context["driving_log"] = DrivingLog.objects.get(
            pk=self.kwargs["driving_log_pk"]
        )
        return context

    def form_valid(self, form):
        form.instance.todo_list = DrivingLog.objects.get(
            pk=self.kwargs["driving_log_pk"]
        )
        form.instance.creator = self.request.user
        return super().form_valid(form)
