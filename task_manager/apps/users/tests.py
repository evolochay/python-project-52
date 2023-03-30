from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpass'
        )

    def test_create_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@test.com')
        self.assertTrue(self.user.check_password('testpass'))

    def test_update_user(self):
        self.user.email = 'newemail@test.com'
        self.user.save()
        self.assertEqual(self.user.email, 'newemail@test.com')

    def test_delete_user(self):
        self.user.delete()
        self.assertEqual(get_user_model().objects.count(), 0)
