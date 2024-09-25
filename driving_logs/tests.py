from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from driving_logs.models import DrivingLog, Drive


class DrivingLogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123",
        )

        cls.driving_log = DrivingLog.objects.create(
            name="Test Log",
            total_hours_needed=65,
            night_hours_needed=10,
            inclement_weather_hours_needed=5,
            creator=cls.user,
        )

        cls.drive = Drive.objects.create(
            name="Test Drive",
            date="2024-09-23",
            hours=1,
            minutes=10,
            night=True,
            inclement_weather=False,
            driving_log=cls.driving_log,
            creator=cls.user,
        )

    def test_driving_log_list_for_logged_in_user(self):
        self.client.login(email="testuser@email.com", password="testpass123")
        response = self.client.get(reverse("driving_log_list"))
        self.assertTemplateUsed(response, "driving_logs/driving_log_list.html")
        self.assertContains(response, "Test Log")

    def test_driving_log_list_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("driving_log_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "%s?next=/driving_logs/" % (reverse("account_login"))
        )
        response = self.client.get(
            "%s?next=/driving_logs/" % (reverse("account_login"))
        )
        self.assertContains(response, "Log In")

    def test_driving_log_detail_for_logged_in_user(self):
        self.client.login(email="testuser@email.com", password="testpass123")
        response = self.client.get(self.driving_log.get_absolute_url())
        no_response = self.client.get("/driving_logs/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test Drive")
        self.assertTemplateUsed(response, "driving_logs/driving_log_detail.html")

    def test_driving_log_detail_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(self.driving_log.get_absolute_url())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"%s?next=/driving_logs/{self.driving_log.pk}/"
            % (reverse("account_login")),
        )
        response = self.client.get(
            f"%s?next=/driving_logs/{self.driving_log.pk}/"
            % (reverse("account_login")),
        )
        self.assertContains(response, "Log In")

    def test_driving_log_data(self):
        self.assertEqual(self.driving_log.name, "Test Log")
        self.assertEqual(self.driving_log.total_hours_needed, 65)
        self.assertEqual(self.driving_log.night_hours_needed, 10)
        self.assertEqual(self.driving_log.inclement_weather_hours_needed, 5)

    def test_drive_data(self):
        self.assertEqual(self.drive.name, "Test Drive")
        self.assertEqual(self.drive.date, "2024-09-23")
        self.assertEqual(self.drive.hours, 1)
        self.assertEqual(self.drive.minutes, 10)
        self.assertEqual(self.drive.night, True)
        self.assertEqual(self.drive.inclement_weather, False)
