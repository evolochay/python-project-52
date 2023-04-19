from django.test import TestCase, LiveServerTestCase, Client
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
                          'status': self.status,
                          'description': '111',
                          }

    def test_list_view_with_login(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks_list.html")
        self.assertContains(response, self.task.name)

class TaskCreateViewTest(TestCase, LiveServerTestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass"
        )
        self.status = baker.make("statuses.Status", name="new")
        self.url = reverse("task_create")
        self.label = baker.make("labels.Label", name="taskkkkkkkk")
        self.client.login(username="testuser", password="testpass")
  
        self.task_data = {'name': 'Test Task 2',
                          'status': 1,
                          'description': 'Test Description 2',
                          'label': [1, 2, 3]}

    def test_create_task(self):
        response = self.client.post(self.url, self.task_data)
        # content = response.content.decode('utf-8')
        # print(content)
        self.assertEqual(Task.objects.count(), 1)
        self.assertRedirects(response, reverse("tasks_list"))
        task = Task.objects.first()
        self.assertEqual(task.author, self.user)
        self.assertEqual(task.name, "Test Task 2")
        self.assertEqual(task.description, "Test Description 2")
        self.assertEqual(task.executor, None)   
