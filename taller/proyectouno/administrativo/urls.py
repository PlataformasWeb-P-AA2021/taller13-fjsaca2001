"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('ver/edificio/<int:id>', views.verEdificio, name='verEdificio'),
    path('crear/edificio', views.crearEdificio, name='crearEdificio'),
    path('editar/edificio/<int:id>', views.editarEdificio, name='editarEdificio'),
    path('eliminar/edificio/<int:id>', views.eliminarEdificio, name='eliminarEdificio'),
    path('crear/departamento', views.crearDepartamento, name='crearDepartamento'),
    path('editar/departamento/<int:id>', views.editarDepartamento, name='editarDepartamento'),
    path('crear/departamento/edificio/<int:id>', views.agregarDepartamentoEdificio, name='agregarDepartamentoEdificio'),
]
