from django import forms
from .models import *

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    tipo = forms.CharField(required=True)



    

    


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'descripcion', 'precio', 'imagen']



        
class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'descripcion', 'precio', 'imagen']
