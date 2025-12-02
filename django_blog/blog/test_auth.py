from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def test_register_login_logout_flow(self):
        register_url = reverse('register')
        login_url = reverse('login')
        profile_url = reverse('profile')
        logout_url = reverse('logout')

        # register
        response = self.client.post(register_url, {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123',
        })
        self.assertEqual(response.status_code, 302)  # redirected after register

        # user exists
        user = User.objects.filter(username='testuser').first()
        self.assertIsNotNone(user)

        # logged in after register: profile accessible
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, 200)

        # logout
        response = self.client.get(logout_url)
        self.assertIn(response.status_code, (302, 200))

        # login
        response = self.client.post(login_url, {
            'username': 'testuser',
            'password': 'ComplexPass123',
        })
        self.assertIn(response.status_code, (302, 200))
