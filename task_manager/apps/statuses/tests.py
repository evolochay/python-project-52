from django.test import TestCase, Client
from django.urls import reverse
from model_bakery import baker
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


class StatusUpdateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.status = Status.objects.create(name='Old Status Name')

    def test_update_status(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('status_update', kwargs={'pk': self.status.pk}),
            {'name': 'New Status Name'}
        )
        self.assertEqual(response.status_code, 302)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'New Status Name')



class StatusDeleteViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.status = baker.make(Status, name="Test Status")
        self.url = reverse("status_delete", kwargs={"pk": self.status.pk})

    def test_view_requires_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_user_can_delete_status(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("statuses_list"))
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())

    def test_user_cannot_delete_protected_status(self):
        self.client.login(username="testuser", password="testpass")
        # task = baker.make("tasks.Task", status=self.status)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("statuses_list"))
