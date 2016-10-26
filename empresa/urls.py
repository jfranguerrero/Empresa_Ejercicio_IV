from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.empresa_list),
    url(r'^empresa/new/$', views.empresa_new, name='empresa_new'),
    url(r'^empresa/calificacion/$', views.calificacion_assign, name='calificacion_assign'),
    url(r'^empresa/delete/$', views.calificacion_delete, name='calificacion_delete'),

]
