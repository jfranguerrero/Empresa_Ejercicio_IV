
"""
.. module:: models
   :platform: Unix, Windows
   :synopsis: Modulo donde se definen los modelos a usar en el sistema

.. moduleauthor:: Jose Francisco Guerrero <jfranguerrero@gmail.com>


"""
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class empresa(models.Model):
    """
    clase que declara los objetos necesarios para identificar una empresa

    :ivar nombre_empresa: nombre de la empresa
    :ivar cif: identificador de la empresa
    :ivar calificacion: nota de la empresa

    """
    nombre_empresa = models.CharField(max_length=200)
    cif = models.CharField(max_length=20)
    calificacion = models.IntegerField(blank=True, null=True)


    def crear(self):
        self.save()

    def __str__(self):
        return self.nombre_empresa

    def _cif(self):
        return self.cif
