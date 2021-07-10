from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Departamento, Edificio


class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre del Edificio'),
            'direccion': _('Ingrese la direccion'),
            'ciudad': _('Ingrese la ciudad'),
            'tipo': _('Ingrese el tipo'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']

        if valor[0] == "L":
            raise forms.ValidationError("La ciudad no puede iniciar con la L mayúscula")
        return valor


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombrePropietario', 'costoDepartamento', 'numeroCuartos', 'edificio']
        labels = {
            'nombrePropietario': _('Ingrese el nombre del propietario'),
            'costoDepartamento': _('Ingrese el costo del departamento'),
            'numeroCuartos': _('Ingrese el numero de cuartos'),
            'edificio': _('Ingrese el edificio'),
        }

    def clean_nombrePropietario(self):
        valor = self.cleaned_data['nombrePropietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese un nombre y dos apellidos")
        return valor

    def clean_costoDepartamento(self):
        valor = self.cleaned_data['costoDepartamento']

        if valor > 100000:
            raise forms.ValidationError("Ingrese un valor menor a 100 Mil.")
        return valor

    def clean_numeroCuartos(self):
        valor = self.cleaned_data['numeroCuartos']

        if valor == 0 or valor > 7:
            raise forms.ValidationError("Ingrese un valor mayor a cero o menor que 7.")
        return valor


class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombrePropietario', 'costoDepartamento', 'numeroCuartos', 'edificio']
        labels = {
            'nombrePropietario': _('Ingrese el nombre del propietario'),
            'costoDepartamento': _('Ingrese el costo del departamento'),
            'numeroCuartos': _('Ingrese el numero de cuartos'),
        }

    def clean_nombrePropietario(self):
        valor = self.cleaned_data['nombrePropietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese un nombre y dos apellidos")
        return valor

    def clean_costoDepartamento(self):
        valor = self.cleaned_data['costoDepartamento']

        if valor > 100000:
            raise forms.ValidationError("Ingrese un valor menor a 100 Mil.")
        return valor

    def clean_numeroCuartos(self):
        valor = self.cleaned_data['numeroCuartos']

        if valor == 0 or valor > 7:
            raise forms.ValidationError("Ingrese un valor mayor a cero o menor que 7.")
        return int(valor)
