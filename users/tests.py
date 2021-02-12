from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")


class UsersSignUpTests(TestCase):
    

    email = "newuser@gmail.com"
    password = "newuserpassword"


    def test_sign_up_status_code(self):
        response = self.client.get("/users/signup/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name_sign_up_page(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.email, self.password)
        self.assertEqual(get_user_model().objects.all().count(), 1)

        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
 #       self.assertEqual(get_user_model().objects.all()[0].password, self.password)

    
    class UserManagersTests(TestCase):

        def test_create_user(self):
            User = get_user_model()
            user = User.objects.create_user(email='users_email@gmail.com', password='users_password')
            self.assertEqual(user.email, email='users_email@gmail.com')
            self.assertTrue(user.is_active)
            self.assertFalse(user.is_staff)
            self.assertFalse(user.is_superuser)
            try:
                self.assertIsNone(user.username)
            except AttribureError:
                path
            with self.assertRaises(TypeError):
                User.objects.create_user()
            with self.assertRaises(TypeError):
                User.objects.create_user(email='')
            with self.assertRaises(ValueError):
                Users.objects.create_user(email='', password="")

