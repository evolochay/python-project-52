from django.test import TestCase, Client
from django.urls import reverse

# from django.contrib.auth.models import User
from task_manager.apps.users.models import User
from .models import Status


class StatuseListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.status = Status.objects.create(name="Test name")
        self.form_data = {"name": "new status"}
        self.client = Client()

    def test_statuses_list_view_with_login(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("statuses_list"))
        self.assertTemplateUsed(response, "statuses_list.html")
        self.assertQuerysetEqual(response.context["statuses"], [self.status])
        self.assertEqual(response.status_code, 200)

    def test_statuses_list_view_without_login(self):
        response = self.client.get(reverse("statuses_list"))
        self.assertRedirects(
            response, "/login/", status_code=302, target_status_code=200
        )
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You need to be authorized")
