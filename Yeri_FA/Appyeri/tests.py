from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from Appyeri.models import Profesor


class EliminarProfesorTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='98765')
        self.client = Client()
        self.client.login(username='testuser', password='98765')
        self.profesor = Profesor.objects.create(
            nombre="Pepe",
            apellido="Lopez",
            email ="p@l.com"
            )
        self.url= reverse('eliminar_profesor', args=[self.profesor.id])

    def test_eliminar_profesor(self):
        response = self.client.post(self.url)
        print(response.content)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('ListarProfesores')) 
        self.client.post(self.url)
        self.assertQuerysetEqual(Profesor.objects.all(), [])