from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="test@email.com",
            password="testpassword",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testsuser",
            email="tests@email.com",
            password="testpassword",
        )
        self.assertEqual(user.username, "testsuser")
        self.assertEqual(user.email, "tests@email.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    