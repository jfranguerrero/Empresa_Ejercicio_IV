"""
.. module:: forms
   :platform: Unix, Windows
   :synopsis: Modulo donde se definen los formularios del sistema

.. moduleauthor:: Jose Francisco Guerrero <jfranguerrero@gmail.com>


"""

from django import forms
from .models import empresa




class empresaForm(forms.ModelForm):
    """Formulario para la creacion de una empresa

    :param forms.ModelForm: objeto formulario
    :type forms.ModelForm: forms.ModelForm

    """
    class Meta:
        model = empresa
        fields = ('nombre_empresa', 'cif',)


class calificacionForm(forms.ModelForm):
    """Formulario para asignar una calificacion

    :param forms.ModelForm: objeto formulario
    :type forms.ModelForm: forms.ModelForm

    """
    class Meta:
        model = empresa
        fields = ('nombre_empresa', 'calificacion',)

class deleteForm(forms.ModelForm):
    """Formulario para eliminar una calificacion

    :param forms.ModelForm: objeto formulario
    :type forms.ModelForm: forms.ModelForm

    """
    class Meta:
        model=empresa
        fields = ('nombre_empresa',)
