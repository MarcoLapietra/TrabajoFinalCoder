from django.db import models

# Create your models here.

    




def directorio_imagen_producto(instance, filename):
    return f'Imagenes_Productos/{instance.titulo}/{filename}'

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to=directorio_imagen_producto)

    def __str__(self):
        return self.titulo