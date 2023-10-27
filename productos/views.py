from django.shortcuts import render
from .models import Producto
from .serializers import ProductosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#def inicio(request):
#    context={}
#    return render(request, 'productos/index.html',context)

@api_view(["GET"])
def ListarProductos(request):
    productos = Producto.objects.all()
    serializer = ProductosSerializer(productos, many=True)
    return Response(serializer.data)