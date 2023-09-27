from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono= models.IntegerField()
    direccion=models.TextField()
    email=models.EmailField(default=None)

    def __str__(self):
        return self.nombre
    

class Productos(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField
    foto=models.ImageField
    



class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)



