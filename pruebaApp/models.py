from django.db import models
from django.utils import timezone
import os

# Create your models here.


class Juguete(models.Model):
    nombre = models.CharField(max_length=50,verbose_name="Nombre del Producto")
    descripcion = models.CharField(max_length=500,verbose_name="Descripcion del producto")
    precio = models.PositiveIntegerField(verbose_name="Precio")
    codigoProducto = models.CharField(max_length=20,verbose_name="Código del Producto")
    creado = models.DateTimeField(default=timezone.now,editable=False)

    def generar_nombre(instance,filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'juguetes'
        fecha = timezone.now().strftime('%d%m%Y_%H%M%S')
        nombre = f"{fecha}.{extension}"
        return os.path.join(ruta, nombre)
    
    foto = models.ImageField(upload_to=generar_nombre,null=True,blank=True,default='juguetes/juguete.png')

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "juguete"
        verbose_name = "Juguete"   
        verbose_name_plural = "Juguetes"
        ordering = ["nombre"]

class Libro(models.Model):
    nombre = models.CharField(max_length=50,verbose_name="Nombre del Producto")
    descripcion = models.CharField(max_length=500,verbose_name="Descripcion del producto")
    precio = models.PositiveIntegerField(verbose_name="Precio")
    codigoProducto = models.CharField(max_length=20,verbose_name="Código del Producto")
    creado = models.DateTimeField(default=timezone.now,editable=False,)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "libro"
        verbose_name = "Libro"   
        verbose_name_plural = "Libros"
        ordering = ["nombre"]

class Ropa(models.Model):
    nombre = models.CharField(max_length=50,verbose_name="Nombre del Producto")
    descripcion = models.CharField(max_length=500,verbose_name="Descripcion del producto")
    precio = models.PositiveIntegerField(verbose_name="Precio")
    codigoProducto = models.CharField(max_length=20,verbose_name="Código del Producto")
    creado = models.DateTimeField(default=timezone.now,editable=False,)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "ropa"
        verbose_name = "Ropa"   
        verbose_name_plural = "Ropas"
        ordering = ["nombre"]