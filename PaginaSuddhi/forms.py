from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm





class RegistroForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

 
 
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',)
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ()






class UserEditForm(UserChangeForm):
    avatar = forms.ImageField(required=False)

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)


    class Meta:
        model=User
        fields = ("email", "first_name", "last_name", "avatar", "password1", "password2",)

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    


# class AvatarFormulario(forms.ModelForm):

#     class Meta:
#         model = Avatar
#         fields = ("imagen",)




class BusquedaProductoForm(forms.Form):
    consulta = forms.CharField(max_length=100, required=False, label='Buscar')





class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)





