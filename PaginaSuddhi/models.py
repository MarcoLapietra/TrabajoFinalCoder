from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono= models.IntegerField()
    direccion=models.TextField()

    def __str__(self):
        return self.nombre
    

class Productos(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField
    foto=models.ImageField
    



