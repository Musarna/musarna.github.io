from django import forms
from pruebaApp.models import Juguete, Libro, Ropa

class JugueteForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Nombre'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Descripcion'}))
    precio = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Precio'}))
    codigoProducto = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Codigo Producto'}))

    def clean_precio(self):

        precio = self.cleaned_data["precio"]
        try:
            precio = int (precio)
        except ValueError:
            raise forms.ValidationError("El Precio debe de ser un numero entero")
        
        if precio < 0:
            raise forms.ValidationError("El Precio debe de ser un numero positivo")
        
        return precio

    class Meta:
        model = Juguete
        fields = '__all__'

class LibroForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Nombre'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Descripcion'}))
    precio = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Precio'}))
    codigoProducto = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Codigo Producto'}))

    class Meta:
        model = Libro
        fields = '__all__'

class RopaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Nombre'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Descripcion'}))
    precio = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Precio'}))
    codigoProducto = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Ingrese Codigo Producto'}))

    class Meta:
        model = Ropa
        fields = '__all__'


