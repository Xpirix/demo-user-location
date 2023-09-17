from django.test import TestCase, Client
from appUsers.models import CustomUser
from django.urls import reverse
from django.contrib.gis.geos import Point
import json
from appUsers.forms import SignUpForm

class LoginTestCase(TestCase):
    """
    Test the login feature
    """
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_valid_login(self):
        response = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(response)

    def test_invalid_login(self):
        response = self.client.login(username='testuser', password='wrongpassword')
        self.assertFalse(response)


class ProfileViewTestCase(TestCase):
    """
    Test the Profile page feature
    """
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_authenticated_user_access_profile(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Access the profile view
        response = self.client.get(reverse('profile'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'dashboard/profile.html')

        # Check if the 'user' context variable contains the logged-in user
        self.assertEqual(response.context['user'], self.user)

    def test_unauthenticated_user_redirect_to_login(self):
        # Access the profile view without logging in
        response = self.client.get(reverse('profile'))

        # Check if the response status code is 302 (Redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the user is redirected to the login page
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('profile'))


class EditProfileViewTestCase(TestCase):
    """
    Test the Profile page feature
    """
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_authenticated_user_access_edit_profile_form(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Access the edit_profile view with a GET request
        response = self.client.get(reverse('edit_profile'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'dashboard/edit_profile.html')

        # Check if 'form' context variable is present
        self.assertTrue('form' in response.context)

    def test_authenticated_user_submit_valid_edit_profile_form(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Prepare POST data for a valid form submission
        self.location = Point(12.345, 67.890)
        post_data = {
            'username':'customuser',
            'first_name':'John',
            'last_name':'Doe',
            'email':'john@example.com',
            'phone':'123-456-7890',
            'address':'123 Main St',
            'location':self.location
        }

        # Access the edit_profile view with a POST request
        response = self.client.post(reverse('edit_profile'), data=post_data)
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_submit_invalid_edit_profile_form(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Prepare POST data for an invalid form submission
        self.location = "POINT INVALID"
        post_data = {
            'username':'customuser',
            'first_name':'John',
            'last_name':'Doe',
            'email':'john@example.com',
            'phone':'123-456-7890',
            'address':'123 Main St',
            'location':self.location
        }

        # Access the edit_profile view with a POST request
        response = self.client.post(reverse('edit_profile'), data=post_data)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'dashboard/edit_profile.html')

        # Check if 'msg' context variable is not None (indicating a form error)
        self.assertIsNotNone(response.context['msg'])

        # Check if 'success' context variable is False
        self.assertFalse(response.context['success'])

    def test_unauthenticated_user_redirect_to_login(self):
        # Access the edit_profile view without logging in
        response = self.client.get(reverse('edit_profile'))

        # Check if the response status code is 302 (Redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the user is redirected to the login page
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('edit_profile'))

class UsersMapViewTestCase(TestCase):
    """
    Test the user map view feature
    """
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

        # Create a test CustomUser with location data
        self.location = Point(12.345, 67.890)
        self.custom_user = CustomUser.objects.create(
            username='customuser',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            phone='123-456-7890',
            address='123 Main St',
            location=self.location,
        )

    def test_authenticated_user_access_users_map(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Access the users_map view
        response = self.client.get('')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'dashboard/users_map.html')

        # Check if 'users' context variable is present
        self.assertTrue('users' in response.context)

        # Check if 'users' context variable is a valid JSON object
        try:
            users_geojson = response.context['users']
            self.assertTrue(isinstance(users_geojson, dict))
        except json.JSONDecodeError:
            self.fail('users_geojson is not a valid JSON object')

        # Check if the geojson is valid
        self.assertTrue('type' in users_geojson)
        self.assertTrue('features' in users_geojson)

    def test_unauthenticated_user_redirect_to_login(self):
        # Access the users_map view without logging in
        response = self.client.get('')

        # Check if the response status code is 302 (Redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the user is redirected to the login page
        self.assertRedirects(response, reverse('login') + '?next=/')

class SignupViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('register')

    def test_signup_view_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertIsInstance(response.context['form'], SignUpForm)

    def test_signup_view_post_valid_data(self):
        self.location = Point(12.345, 67.890)
        data = {
            'username': 'testuser',
            'first_name':'John',
            'last_name':'Doe',
            'password1': 'testpassword123',
            'password2': 'testpassword123',  # This will make the form invalid
            'email': 'john@example.com',
            'phone': '123-456-7890',
            'address': '123 Main St',
            'location': self.location.wkt,
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())

    def test_signup_view_post_invalid_data(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'mismatchedpassword',  # This will make the form invalid
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)  # Form submission should stay on the same page
        self.assertFormError(response, 'form', 'password2', ['The two password fields didn’t match.', 'Password and confirm password do not match'])

    def test_signup_view_post_form_not_valid(self):
        data = {}  # Submit empty data to make the form invalid
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)  # Form submission should stay on the same page
        self.assertContains(response, 'Form is not valid', status_code=200)