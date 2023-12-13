from django.shortcuts import render
from .models import Producto, Categoria
from .serializers import ProductosSerializer, CategoriasSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#def inicio(request):
#    context={}
#    return render(request, 'productos/index.html',context)
@api_view(["GET"])
def ListarCategorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriasSerializer(categorias, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def ListarProductos(request):
    productos = Producto.objects.all()
    serializer = ProductosSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def FiltrarProducto(request, pk):
    productos = Producto.objects.get(id_producto=pk)
    serializer = ProductosSerializer(productos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CrearProducto(request):
    serializer = ProductosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
def ActualizarProducto(request, pk):
    productos = Producto.objects.get(id_producto=pk)
    serializer = ProductosSerializer(instance=productos, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def EliminarProducto(request, pk):
    productos = Producto.objects.get(id_producto=pk)
    productos.delete()

    return Response('Producto eliminado')
