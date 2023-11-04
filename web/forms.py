from django import forms

class ProductoForm(forms.Form):
    categoria   = forms.IntegerField()
    nombre      = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=200)
    precio      = forms.IntegerField()
    stock       = forms.IntegerField()