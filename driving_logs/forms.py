from django import forms
from django.forms import ModelForm

from .models import Drive, DrivingLog


class DateInput(forms.DateInput):
    input_type = "date"


class CheckBoxInput(forms.CheckboxInput):
    input_type = "checkbox"


class DriveCreateForm(ModelForm):
    class Meta:
        model = Drive
        fields = [
            "date",
            "hours",
            "minutes",
            "night",
            "inclement_weather",
            "driving_log",
        ]
        widgets = {
            "date": DateInput(),
            "night": CheckBoxInput(),
            "inclement_weather": CheckBoxInput(),
        }


class DriveUpdateForm(ModelForm):
    class Meta:
        model = Drive
        fields = [
            "date",
            "hours",
            "minutes",
            "night",
            "inclement_weather",
        ]
        widgets = {
            "date": DateInput(),
            "night": CheckBoxInput(),
            "inclement_weather": CheckBoxInput(),
        }


class DrivingLogCreateForm(ModelForm):
    class Meta:
        model = DrivingLog
        fields = [
            "name",
            "total_hours_needed",
            "night_hours_needed",
            "inclement_weather_hours_needed",
        ]


class DrivingLogUpdateForm(ModelForm):
    class Meta:
        model = DrivingLog
        fields = [
            "name",
            "total_hours_needed",
            "night_hours_needed",
            "inclement_weather_hours_needed",
        ]
