from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import Permission, User
from django.test.testcases import SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


from users.models import CustomUser
from .models import Cinema

 
class TestCRUDCinemas(TestCase):
    def setUp(self):

        self.cinema = Cinema.objects.create(
            name = 'Jovten',
            description = 'nice cinema!',
            address = 'kiev',
            cover = 'cover/cover1.jpg'
         )

        #creating

    def test_anonymous_cannot_add_cinemas(self):
        response = self.client.get(reverse("cinema_create"))
        self.assertRedirects(response, "/users/login/?next=/shows/cinema_create/")

    def test_admin_user_can_add_of_cinemas(self):
        user = CustomUser.objects.create_user("admintest@email.com", "secret", is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.post('/shows/cinema_create/', {'name':'Kiev', 'description':'Unlocked in new life', 'address':'kiev', 'cover':'cover2.img'})
        self.assertEqual(response.status_code, 302)

    def test_simple_user_can_add_of_cinemas(self):
        user = CustomUser.objects.create_user("simpletest@email.com", "secret", is_superuser=False)
        self.client.force_login(user=user)
        response = self.client.post('/shows/cinema_create/', {'name':'Kiev', 'description':'Unlocked in new life', 'address':'kiev', 'cover':'cover2.img'})
        self.assertEqual(response.status_code, 403)    

        #reading

    def test_anonymous_cannot_see_list_of_cinemas(self):
        response = self.client.get(reverse("cinema_list"))
        self.assertRedirects(response, "/users/login/?next=/shows/")

    def test_admin_user_can_see_list_of_cinemas(self):
        user = CustomUser.objects.create_user("admintest@email.com", "secret", is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.get(reverse("cinema_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jovten' and 'kiev' and 'nice cinema!' and 'cover/cover1.jpg')
        self.assertTemplateUsed(response, 'cinema_list.html')


    def test_simple_user_cannot_see_list_of_cinema(self):
        user = CustomUser.objects.create_user("simpletest@email.com", "secret", is_superuser=False)
        self.client.force_login(user=user)
        response = self.client.get(reverse("cinema_list"))
        self.assertEqual(response.status_code, 403)

    def test_anonymous_cannot_see_details_about_cinema(self):
        response = self.client.get("/shows/1/")
        self.assertRedirects(response, "/users/login/?next=/shows/1/")

    def test_admin_user_can_see_details_about_cinema(self):
        user = CustomUser.objects.create_user("admintest@email.com", "secret", is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.get("/shows/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jovten' and 'kiev' and 'nice cinema!' and 'cover/cover1.jpg')
        self.assertTemplateUsed(response, 'cinema_detail.html')

    def test_simple_user_cannot_see_details_about_cinema(self):
        user = CustomUser.objects.create_user("simpletest@email.com", "secret", is_superuser=False)
        self.client.force_login(user=user)
        response = self.client.get('/shows/1/')
        self.assertEqual(response.status_code, 403)


    #updating

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

    #delete

    def test_anonimus_user_cant_delete_data_about_cinema(self):
        response = self.client.get("/shows/1/cinema_delete/")
        self.assertRedirects(response, "/users/login/?next=/shows/1/cinema_delete/")

    def test_admin_user_can_delete_data_about_cinema(self):
        user = CustomUser.objects.create_user("admintest@email.com", "secret", is_superuser=True)
        self.client.force_login(user=user)
        response = self.client.post('/shows/1/cinema_delete/')
        self.assertEqual(response.status_code, 302)

    def test_simple_user_cant_delete_data_about_cinema(self):
        user = CustomUser.objects.create_user("simpleuser@email.com", "secret", is_superuser=False)
        self.client.force_login(user=user)
        response = self.client.post('/shows/1/cinema_delete/')
        self.assertEqual(response.status_code, 403)


class CinemaModelTest(TestCase):
    def setUp(self):
        self.cinema = Cinema.objects.create(
            name = 'Jovten',
            description = 'nice cinema!',
            address = 'kiev'
         )

    def test_upload_cover(self):
        cover = SimpleUploadedFile("cover1.jpg", b"file_content", content_type="image/img")
        response = self.client.post("/shows/", {'covers':cover})
        self.assertEqual(response.status_code, 302)

    def test_cinema_string_representation(self):
        cinema = Cinema(name = 'Jovten')
        self.assertEqual(str(cinema), cinema.name)

    def test_cinema_get_absoute_url(self):
        self.assertEqual(self.cinema.get_absolute_url(), '/shows/')

    def test_cinema_content(self):
        self.assertEqual(f'{self.cinema.name}', 'Jovten')
        self.assertEqual(f'{self.cinema.description}', 'nice cinema!')
        self.assertEqual(f'{self.cinema.address}', 'kiev')
