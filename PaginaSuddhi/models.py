from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email=models.EmailField(default=None, blank=True, null=True)

    def __str__(self):
        return self.nombre
    

   
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)




class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)







class ContactRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject



