from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from laboratorio.models import Laboratorio

class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.laboratorio = Laboratorio.objects.create(
            nombre = "Laboratorio1",
            ciudad = "Ciudad 1",
            pais = "Pais 1"
        )
    
    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, "Laboratorio1")
        self.assertEqual(self.laboratorio.ciudad, "Ciudad 1")
        self.assertEqual(self.laboratorio.pais, "Pais 1")

    def test_url_exists_at_correct_location(self):
        res = self.client.get("/informacion/")
        self.assertEqual(res.status_code, 200)
    
    def test_homepage(self):
        res = self.client.get(reverse("informacion"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "info.html")
        self.assertContains(res, "Información de Laboratorios")