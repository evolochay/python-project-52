from django.test import TestCase, LiveServerTestCase, Client
from django.urls import reverse
from model_bakery import baker
from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status
from task_manager.apps.tasks.models import Task


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
        self.form_data = {
            "name": "one more task",
            "status": self.status,
            "description": "111",
        }

    def test_list_view_with_login(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks_list.html")
        self.assertContains(response, self.task.name)


class TaskCUDTest(TestCase, LiveServerTestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.status = baker.make("statuses.Status", name="new")
        self.url = reverse("task_create")
        self.label = baker.make("labels.Label", name="taskkkkkkkk")
        self.client.login(username="testuser", password="testpass")
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            status=self.status,
            author=self.user,
        )

        self.task_data = {
            "name": "Test Task 2",
            "status": 1,
            "description": "Test Description 2",
            "label": [1, 2, 3],
        }

    def test_create_task(self):
        response = self.client.post(self.url, self.task_data)
        self.assertEqual(Task.objects.count(), 2)
        self.assertRedirects(response, reverse("tasks_list"))
        task = Task.objects.get(pk=2)
        self.assertEqual(task.author, self.user)
        self.assertEqual(task.name, "Test Task 2")
        self.assertEqual(task.description, "Test Description 2")
        self.assertEqual(task.executor, None)

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
        self.assertTemplateUsed(response, "crud/create&update.html")

    def test_update_task(self):
        self.client.login(username="testuser", password="testpass")
        print(f"{self.task.pk} TASK ID")
        response = self.client.post(
            reverse("task_update", kwargs={"pk": self.task.pk}), self.task_data
        )
        self.assertRedirects(response, reverse("tasks_list"))
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, "Test Task 2")

    def test_delete_task(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("task_delete", kwargs={"pk": self.task.pk}))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
        self.assertRedirects(response, reverse("tasks_list"))
        self.assertEqual(response.status_code, 302)
