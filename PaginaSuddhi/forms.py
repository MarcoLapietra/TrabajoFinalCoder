from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions




class RegistroForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

 
 
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ()







class UserEditForm(UserChangeForm):
    

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)


    class Meta:
        model=User
        fields = ("email", "first_name", "last_name", "password1", "password2",)

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
        
    






class BusquedaProductoForm(forms.Form):
    consulta = forms.CharField(max_length=100, required=False, label='Buscar')





class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True, label='Nombre')
    correo = forms.EmailField(required=True, label='Correo Electrónico')
    telefono = forms.CharField(max_length=15, required=True, label='Número de Teléfono')
    subject = forms.CharField(max_length=100, required=True, label='Asunto')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Mensaje')


