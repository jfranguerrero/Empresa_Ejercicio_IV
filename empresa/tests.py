from django.test import TestCase
from empresa.forms import empresaForm
from empresa.forms import calificacionForm
from empresa.forms import deleteForm
from .models import empresa


class empresaTest(TestCase):

    def test_formularioCreacion(self):
        datos_formulario={'nombre_empresa': 'Empresa Prueba', 'cif': '12345A'}
        form= empresaForm(data=datos_formulario)
        self.assertTrue(form.is_valid())



    def test_asignarCalificacion(self):
        datos_f={'nombre_empresa': 'Empresa Prueba', 'calificacion': '6'}
        form1= calificacionForm(data=datos_f)
        self.assertTrue(form1.is_valid())

    def test_deleteCalificacion(self):
        datos_f={'nombre_empresa': 'Empresa Prueba'}
        form1= deleteForm(data=datos_f)
        self.assertTrue(form1.is_valid())


    def test_crea_empresa(self):
		empress = empresa(nombre_empresa='test_empresa',cif='12345A')
		empress.crear()
		self.assertEqual(empress.__str__(), 'test_empresa')
