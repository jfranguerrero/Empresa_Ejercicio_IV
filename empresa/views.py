"""
.. module:: views
   :platform: Unix, Windows
   :synopsis: Modulo en el cual estan declaradas todas las funciones que permiten
   el funcionamiento del sistema web

.. moduleauthor:: Jose Francisco Guerrero <jfranguerrero@gmail.com>


"""

from django.shortcuts import render
from .models import empresa
from .forms import empresaForm
from django.shortcuts import redirect
from .forms import calificacionForm
from django import forms
from .forms import deleteForm

def empresa_list(request):
    """Esta funcion muestra las empresas con sus calificaciones ordenadas por la nota de cada empresa de forma descendente.

    :param request: peticion realizada
    :type request: request
    :returns:  render

    """
    empresas = empresa.objects.filter(calificacion__gte=0).order_by('-calificacion')
    return render(request, 'empresa/empresa_list.html', {'empresas': empresas})

def empresa_new(request):
    """Esta funcion muestra el formulario para la creacion de una nueva empresa y la crea en la base de datos
    :param request: peticion realizada
    :type request: request
    :returns:  redirecciona al index si fue todo correcto o carga de nuevo el formulario.
    """
    if request.method == "POST":
        form = empresaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = empresaForm()
        return render(request, 'empresa/empresa_edit.html', {'form': form})


def calificacion_assign(request):
    """Esta funcion asigna una nota a una de las empresas ya creadas. Para ello extrae de la base de datos las empresas y le asgina la calificacion a la seleccionada.
    :param request: peticion realizada
    :type request: request
    :returns:  redirecciona al index si fue todo correcto o carga de nuevo el formulario.
    """
    if request.method == "POST":
        calificacionForm.base_fields['nombre_empresa']=forms.ModelChoiceField(queryset=empresa.objects.filter(calificacion__isnull=True))
        form = calificacionForm(request.POST)
        if form.is_valid():
            emp= form.cleaned_data['nombre_empresa']
            cali=form.cleaned_data['calificacion']
            empresa.objects.filter(nombre_empresa=emp).update(calificacion=cali)
            return redirect('/')
    else:
        calificacionForm.base_fields['nombre_empresa']=forms.ModelChoiceField(queryset=empresa.objects.filter(calificacion__isnull=True))
        form = calificacionForm()
        return render(request, 'empresa/calificacion_edit.html', {'form': form})

def calificacion_delete(request):
    """Esta funcion elimina de la base de datos la calificacion de la empresa seleccionada.
    :param request: peticion realizada
    :type request: request
    :returns:  redirecciona al index si fue todo correcto o carga de nuevo el formulario.
    """
    if request.method == "POST":
        deleteForm.base_fields['nombre_empresa']=forms.ModelChoiceField(queryset=empresa.objects.filter(calificacion__isnull=False))
        form = deleteForm(request.POST)
        if form.is_valid():
            emp= form.cleaned_data['nombre_empresa']
            empresa.objects.filter(nombre_empresa=emp).update(calificacion=None)
            return redirect('/')
    else:
        deleteForm.base_fields['nombre_empresa']=forms.ModelChoiceField(queryset=empresa.objects.filter(calificacion__isnull=False))
        form = deleteForm()
        return render(request, 'empresa/calificacion_delete.html', {'form': form})
