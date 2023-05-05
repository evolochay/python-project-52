from django.test import TestCase, Client
from django.urls import reverse_lazy, reverse
from task_manager.apps.users.models import User
from .models import Label


class LabelListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="12345"
        )
        self.label = Label.objects.create(name="Test Label")
        self.url = reverse_lazy("labels_list")
        self.del_url = reverse_lazy(
            "label_delete", kwargs={"pk": self.label.pk}
        )
        self.client = Client()

    def test_list_labels(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "labels_list.html")
        self.assertContains(response, "Test Label")


    def test_create_label(self):
        self.client.login(username="testuser", password="12345")
        form_data = {
            "name": "New Test Label",
        }
        response = self.client.post(reverse("label_create"), form_data)
        self.assertEqual(Label.objects.count(), 2)
        self.assertRedirects(response, reverse("labels_list"))

    def test_update_status(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            reverse("label_update", kwargs={"pk": self.label.pk}),
            {"name": "Super New Label Name"},
        )
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, "Super New Label Name")

    def test_delete_label(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.post(self.del_url)
        self.assertRedirects(response, self.url)
