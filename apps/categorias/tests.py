from django.test import TestCase
from .models import Categoria

# Create your tests here.
class CategoriaTestCase(TestCase):
    def setUp(self):
        Categoria.objects.create(nombre='Pantalon')
        Categoria.objects.create(nombre='Zapatos')
        Categoria.objects.create(nombre='Accesorios')

    def test_categoria_get(self):
        pantalon = Categoria.objects.get(nombre='Pantalon')
        zapatos = Categoria.objects.get(nombre='Zapatos')
        accesorios = Categoria.objects.get(nombre='Accesorios')

        self.assertEqual(pantalon.nombre, "Pantalon")
        self.assertEqual(zapatos.nombre, "Zapatos")
        self.assertEqual(accesorios.nombre, "Accesorios")
