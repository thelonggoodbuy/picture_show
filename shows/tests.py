from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import Permission, User
from django.test.testcases import SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import tempfile
from io import BytesIO
import uuid
import os



from users.models import CustomUser
from .models import Cinema
from .views import CinemaCreateView
from django.conf import settings





class TestCinemaCreateView(TestCase):

    def test_anonymous_cannot_add_cinemas(self):
        response = self.client.get(reverse("cinema_create"))
        self.assertRedirects(response, "/users/login/?next=/shows/cinema/cinema_create/")

    def test_simple_user_can_add_of_cinemas(self):
        user = CustomUser.objects.create_user("simpletest@email.com", "secret", is_superuser=False)
        self.client.force_login(user=user)
        response = self.client.post('/shows/cinema/cinema_create/', {'name':'Kiev', 'description':'Unlocked in new life', 'address':'kiev', 'cover':'cover2.img'})
        self.assertEqual(response.status_code, 403)


class TestCinemaReadListView(TestCase):
    cover1 = tempfile.NamedTemporaryFile(suffix=".jpeg").name
    def setUp(self):
        
        self.cinema = Cinema.objects.create(
            name = 'Jovten',
            description = 'nice cinema!',
            address = 'kiev',
            cover = 'cover/cover1.jpg'
         )

    def test_anonymous_cannot_see_list_of_cinemas(self):
        response = self.client.get(reverse("cinema_list"))
        self.assertRedirects(response, "/users/login/?next=/shows/cinema/")

    def test_admin_user_can_see_list_of_cinemas(self):
        user = CustomUser.objects.create_user("admintest@email.com", "secret", is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.get(reverse("cinema_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jovten' and 'kiev' and 'nice cinema!' and 'cover')
        self.assertTemplateUsed(response, 'cinema_list.html')


    def test_simple_user_cannot_see_list_of_cinema(self):
        user = CustomUser.objects.create_user("simpletest@email.com", "secret", is_superuser=False)
        self.client.force_login(user=user)
        response = self.client.get(reverse("cinema_list"))
        self.assertEqual(response.status_code, 403)

class TestCinemaReadDetailView(TestCase):
    def setUp(self):

        self.cinema = Cinema.objects.create(
            name = 'Jovten',
            description = 'nice cinema!',
            address = 'kiev',
            cover = 'cover/cover1.jpg'
         )
    def test_anonymous_cannot_see_details_about_cinema(self):
        response = self.client.get("/shows/cinema/1/")
        self.assertRedirects(response, "/users/login/?next=/shows/cinema/1/")

    def test_admin_user_can_see_details_about_cinema(self):
        user = CustomUser.objects.create_user("admintest@email.com", "secret", is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.get("/shows/cinema/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jovten' and 'kiev' and 'nice cinema!' and 'cover/cover1.jpg')
        self.assertTemplateUsed(response, 'cinema_detail.html')

    def test_simple_user_cannot_see_details_about_cinema(self):
        user = CustomUser.objects.create_user("simpletest@email.com", "secret", is_superuser=False)
        self.client.force_login(user=user)
        response = self.client.get('/shows/cinema/1/')
        self.assertEqual(response.status_code, 403)


class TestCinemaUpdateView(TestCase):
    def setUp(self):

        self.cinema = Cinema.objects.create(
            name = 'Jovten',
            description = 'nice cinema!',
            address = 'kiev',
            cover = 'cover/cover1.jpg'
         )

    def test_anonimus_user_cant_update_data_about_cinema(self):
        response = self.client.get("/shows/1/cinema_edit/")
        self.assertRedirects(response, "/users/login/?next=/shows/1/cinema_edit/")

    def test_admin_user_can_update_data_about_cinema(self):
        user = CustomUser.objects.create_user("admintest@email.com", "secret", is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.post('/shows/1/cinema_edit/', {'name':'Kiiiv', 'description':'Unlocked in new life', 'address':'kiev', 'cover':'cover2.img'})
        self.assertEqual(response.status_code, 302)

    def test_simple_user_cant_update_data_about_cinema(self):
        user = CustomUser.objects.create_user("simpleuser@email.com", "secret", is_superuser=False)
        self.client.force_login(user=user)
        response = self.client.post('/shows/1/cinema_edit/', {'name':'Kiiiv', 'description':'Unlocked in new life', 'address':'kiev', 'cover':'cover2.img'})
        self.assertEqual(response.status_code, 403)


class TestCinemaUpdateView(TestCase):

    def setUp(self):
        self.cinema = Cinema.objects.create(
            name = 'Jovten',
            description = 'nice cinema!',
            address = 'kiev',
            cover = 'cover/cover1.jpg'
         )

    def test_anonimus_user_cant_delete_data_about_cinema(self):
        response = self.client.get("/shows/cinema/1/cinema_delete/")
        self.assertRedirects(response, "/users/login/?next=/shows/cinema/1/cinema_delete/")

    def test_admin_user_can_delete_data_about_cinema(self):
        user = CustomUser.objects.create_user("admintest@email.com", "secret", is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.post('/shows/cinema/1/cinema_delete/')
        self.assertEqual(response.status_code, 302)

    def test_simple_user_cant_delete_data_about_cinema(self):
        user = CustomUser.objects.create_user("simpleuser@email.com", "secret", is_superuser=False)
        self.client.force_login(user=user)
        response = self.client.post('/shows/cinema/1/cinema_delete/')
        self.assertEqual(response.status_code, 403)


class CinemaModelTest(TestCase):

    def setUp(self):
        self.cinema = Cinema.objects.create(
            name = 'Jovten',
            description = 'nice cinema!',
            address = 'kiev',
            cover = None
         )
  
    def test_if_photo_saved_in_model(self):
        with open(settings.BASE_DIR / 'tests/testfiles/cover_1.jpg', 'rb') as cinema_cover1_jpg:
            print('Before Test:')
            print(Cinema.objects.values())
            response = self.client.post("cinema/<int:pk>/cinema_edit/", {
                "name": 'Jovten',
                "description": 'nice cinema!',
                "address": 'kiev',
                "cover": cinema_cover1_jpg
                })
        
        self.assertEqual(Cinema.objects.last(), self.cinema)
        self.assertEqual(Cinema.objects.count(), 1)
        print('After Test:')
        print(Cinema.objects.values())

    def test_cinema_string_representation(self):
        cinema = Cinema(name = 'Jovten')
        self.assertEqual(str(cinema), cinema.name)

    def test_cinema_content(self):
        self.assertEqual(f'{self.cinema.name}', 'Jovten')
        self.assertEqual(f'{self.cinema.description}', 'nice cinema!')
        self.assertEqual(f'{self.cinema.address}', 'kiev')
