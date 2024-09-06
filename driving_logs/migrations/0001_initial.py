# Generated by Django 4.2.16 on 2024-09-06 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DrivingLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_hours_needed', models.IntegerField(default=0)),
                ('night_hours_needed', models.IntegerField(default=0)),
                ('inclement_weather_hours_needed', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('hours', models.IntegerField(blank=True, default=0, null=True)),
                ('minutes', models.IntegerField(blank=True, default=0, null=True)),
                ('night', models.BooleanField(default=False)),
                ('inclement_weather', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('driving_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driving_logs.drivinglog')),
            ],
        ),
    ]
