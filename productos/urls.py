from django.urls import path
from . import views

urlpatterns = [
    #path('',views.inicio, name=''),
    path('',views.ListarProductos, name='productos'),
    path('detalle/<str:pk>',views.FiltrarProducto, name='detalle'),
    path('crear', views.CrearProducto, name="crear"),
    path('actualizar/<str:pk>/', views.ActualizarProducto, name="actualizar"),
    path('eliminar/<str:pk>/', views.EliminarProducto, name="eliminar"),
    ]