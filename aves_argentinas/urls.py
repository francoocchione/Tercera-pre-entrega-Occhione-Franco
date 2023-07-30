from django.contrib import admin
from django.urls import path
from aves_argentinas.views import (
    mostrar_aves, mostrar_fauna, mostrar_flora, crear_aves, crear_fauna, crear_flora, buscar_aves, buscar_fauna, buscar_flora, eliminar_aves, editar_aves, AvesDetailView, FaunaDetailView, FloraDetailView, eliminar_fauna, eliminar_flora, editar_fauna, editar_flora
)
urlpatterns = [
    path('aves/', mostrar_aves, name="lista_aves"),
    path('fauna/', mostrar_fauna, name="lista_fauna"),
    path('flora/', mostrar_flora, name="lista_flora"),
    path('publicar-ave/', crear_aves, name="crear_aves"),
    path('publicar-fauna/',crear_fauna, name="crear_fauna"),
    path('publicar-flora', crear_flora, name="crear_flora"),
    path('buscar-ave/', buscar_aves, name='buscar_aves'),
    path('buscar-fauna/', buscar_fauna, name = "buscar_fauna"),
    path('buscar-flora/', buscar_flora, name = "buscar_flora"),
    path('eliminar_aves/<int:id>/', eliminar_aves, name = "eliminar_aves"),
    path('eliminar_fauna/<int:id>/', eliminar_fauna, name = "eliminar_fauna"),
    path('eliminar_flora/<int:id>/', eliminar_flora, name = "eliminar_flora"),
    path('editar-aves/<int:id>/', editar_aves, name = "editar_aves"),
    path('editar-fauna/<int:id>/', editar_fauna, name = "editar_fauna"),
    path('editar-flora/<int:id>/', editar_flora, name = "editar_flora"),
    path('aves/<int:pk>/', AvesDetailView.as_view(), name="ver_ave"),
    path('fauna/<int:pk>/', FaunaDetailView.as_view(), name="ver_fauna"),
    path('flora/<int:pk>/', FloraDetailView.as_view(), name="ver_flora"),
]
