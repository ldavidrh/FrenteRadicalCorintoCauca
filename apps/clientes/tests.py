from django.test import TestCase
from django.urls import reverse, resolve
from apps.clientes.views import registro_view, login_view, consultarClientes_view, perfil_view
import unittest
# Create your tests here.

class ClienteURLTestCase(unittest.TestCase):
        
    def test_registro_url_is_resolved(self):
        registro = reverse('clientes:registro')
        self.assertEqual(resolve(registro).func, registro_view)

    def test_login_url_is_resolved(self):
        login = reverse('clientes:login')
        self.assertEqual(resolve(login).func, login_view)
    
    def test_consultarClientes_url_is_resolved(self):
        consultar = reverse('clientes:consulta')
        self.assertEqual(resolve(consultar).func, consultarClientes_view)
        
    def test_logout_error_forzado(self):
        logout = reverse('clientes:logout')
        self.assertEqual(resolve(logout).func, perfil_view) 

