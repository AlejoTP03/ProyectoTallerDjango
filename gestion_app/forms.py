from django import forms
from .models import Mecanico,Carro,Propietario

class Mecanico_form(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = ['ci','nombre','apellido','telefono','direccion']
        
class Carro_form(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['matricula','marca','modelo','ci_mecanico']
        
class Propietario_form(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['ci','nombre','apellido','telefono','direccion','carros']