from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status

from .models import Task


class TaskListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.status = Status.objects.create(name="Test name")
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            status=self.status,
            author=self.user,
        )
        self.url = reverse("tasks_list")

    def test_list_view_with_login(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks_list.html")
        self.assertContains(response, self.task.name)

    def test_create_view_with_login(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "name": "Test Task",
            "description": "Test Description",
            "status": self.status,
            "executor": self.client,
        }
        response = self.client.post(self.url, data=data, follow=True)
        self.assertRedirects(response, self.url)
        task = Task.objects.get(name="Test Task")
        self.assertEqual(task.author, self.user)

    def test_create_view_with_invalid_data(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "name": "",
            "description": "",
            "status": "",
            "executor": "",
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create.html")

    def test_update_task(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("task_update", kwargs={"pk": self.status.pk}),
            {"name": "New Task Name"},
        )
        self.assertRedirects(response, reverse("tasks_list"))
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, "New Task Name")

    def test_delete_task(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("task_delete", kwargs={"pk": self.task.pk}))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
        self.assertRedirects(response, reverse("tasks_list"))
        self.assertEqual(response.status_code, 302)
