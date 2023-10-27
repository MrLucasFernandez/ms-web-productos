from django.urls import path
from . import views

urlpatterns = [
    #path('',views.inicio, name=''),
    path('',views.ListarProductos, name='productos'),
    ]