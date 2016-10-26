"""
.. module:: apps
   :platform: Unix, Windows
   :synopsis: Modulo que define el nombre de nuestro objeto.

.. moduleauthor:: Jose Francisco Guerrero <jfranguerrero@gmail.com>


"""

from __future__ import unicode_literals

from django.apps import AppConfig


class EmpresaConfig(AppConfig):
    name = 'empresa'
