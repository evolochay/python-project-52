from django.test import TestCase, Client
from django.urls import reverse_lazy
from task_manager.apps.users.models import User
from .models import Label
from .views import LabelListView


class LabelListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.label = Label.objects.create(name='Test Label')
        self.url = reverse_lazy('labels_list')
        self.del_url = reverse_lazy('label_delete', kwargs={'pk': self.label.pk})
        self.client = Client()
    
    def test_list_labels(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels_list.html')
        self.assertContains(response, 'Test Label')
    
    def test_delete_label(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.del_url)
        self.assertRedirects(response, self.url)
        self.assertContains(response, "Label was successfully deleted")

