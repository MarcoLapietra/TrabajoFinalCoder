from django import forms


class ProductoFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    tipo = forms.CharField(required=True)



    