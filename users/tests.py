from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse
from django.utils.translation import ugettext_lazy


from .models import CustomUser


class HomePageTest(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        response = self.client.get(reverse ('home'))
        self.assertTemplateUsed(response, 'home.html')


class SignUpPageTest(TestCase):
    
    email = 'newuser@gmail.com'
    password = 'newuserpassword'


    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_creating_user_in_database(self):
        new_user = get_user_model().objects.create_user(self.email, self.password)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        self.assertEqual(get_user_model().objects.all()[0].password, self.password)

class CustomUserManager(BaseUserManager):

    def test_create_user(self, email, password, **extra_fields):
        print(start_users_creating)
        if not email:
            raise ValueError(ugettext('The email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        print(finish_users_creating)
        return user
