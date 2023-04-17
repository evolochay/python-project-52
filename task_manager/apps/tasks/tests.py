from django.test import TestCase, Client
from django.urls import reverse
from model_bakery import baker
from django.contrib.messages import get_messages
from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status
from task_manager.apps.tasks.models import Task
from task_manager.apps.labels.models import Label


class TaskListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpass")
        self.status = Status.objects.create(name="Test name")
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            status=self.status,
            author=self.user,
        )
        self.url = reverse("tasks_list")
        self.create_task_url = reverse("task_create")
        self.form_data = {'name': 'one more task',
                          'status': 1,
                          'description': '111',
                          'executor': 2,
                          'label': [1, 2, 3]}

    def test_list_view_with_login(self):
        self.client.force_login(self.user)
        # self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks_list.html")
        self.assertContains(response, self.task.name)

class TaskCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass"
        )
        self.url = reverse("task_create")
        self.client.login(username="testuser", password="testpass")

    def test_create_task(self):
        response = self.client.post(
            self.url,
            {
                "name": "Test Task",
                "description": "This is a test task.",
                "status": "new",
                "executor": "",
                "labels": "",
            },
        )
        self.assertRedirects(response, reverse("tasks_list"))
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.author, self.user)
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.description, "This is a test task.")
        self.assertEqual(task.status, "new")
        self.assertEqual(task.executor, None)
        self.assertEqual(task.labels, "")
   
