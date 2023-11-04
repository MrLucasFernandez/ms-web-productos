from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from rest_framework.utils import json
from .forms import ProductoForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.


def index(request):
    response = requests.get('http://127.0.0.1:8000/productos/').json()
    return render(request, 'web/index.html', {
        'response': response
    })


@csrf_protect
def post_producto(request):
    url = "http://127.0.0.1:8000/productos/crear"
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        categoria   = form.cleaned_data.get("categoria")
        nombre      = form.cleaned_data.get("nombre")
        descripcion = form.cleaned_data.get("descripcion")
        precio      = form.cleaned_data.get("precio")
        stock       = form.cleaned_data.get("stock")

        print(categoria)
        print(nombre)
        print(descripcion)
        print(precio)
        print(stock)
        data = {'id_categoria': categoria , 'nombre': nombre, 'descripcion': descripcion, 'stock': stock, 'precio': precio }
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return render(request, 'web/form.html', {
            'response': response
        })