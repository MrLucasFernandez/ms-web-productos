from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria    = models.BigAutoField(db_column='idCategoria', primary_key=True)
    descripcion     = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.descripcion)

class Producto(models.Model):
    id_producto     = models.AutoField(primary_key=True)
    id_categoria    = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria')
    nombre          = models.CharField(max_length=30)
    descripcion     = models.CharField(max_length=200)
    stock           = models.IntegerField()
    precio          = models.IntegerField()
    
    def __str__(self):
        return "ID: "+str(self.id_producto)+" "+str(self.nombre)+" /"+str(self.id_categoria)