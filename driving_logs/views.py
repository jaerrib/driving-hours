from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import (
    DriveCreateForm,
    DriveUpdateForm,
    DrivingLogCreateForm,
    DrivingLogUpdateForm,
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


class DrivingLogCreateView(LoginRequiredMixin, CreateView):
    model = DrivingLog
    form_class = DrivingLogCreateForm
    template_name = "driving_logs/driving_log_new.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DrivingLogUpdateView(LoginRequiredMixin, UpdateView):
    model = DrivingLog
    form_class = DrivingLogUpdateForm
    template_name = "driving_logs/driving_log_edit.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DriveCreateView(LoginRequiredMixin, CreateView):
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
        return DrivingLog.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = DriveCreateForm()
        context["driving_log"] = DrivingLog.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.driving_log = DrivingLog.objects.filter(pk=self.kwargs["pk"])
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DriveUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Drive
    form_class = DriveUpdateForm
    template_name = "driving_logs/drive_edit.html"

    def get_success_url(self):
        driving_log_pk = self.object.driving_log_id
        return reverse("driving_log_detail", kwargs={"pk": driving_log_pk})

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class DriveDeleteView(DeleteView):
    model = Drive
    template_name = "driving_logs/drive_delete.html"
    success_url = reverse_lazy("driving_log_list")
