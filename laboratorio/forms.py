

from django.forms import ModelForm, TextInput
from laboratorio.models import Laboratorio

class LaboratorioForm(ModelForm):

    class Meta:
        model = Laboratorio
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs = {
                    'type': 'text',
                    'placeholder': 'Ingrese el nombre del laboratorio'
                    }
            ),
            'ciudad': TextInput(
                attrs = {
                    'type': 'text',
                    'placeholder': 'Ingrese la ciudad del laboratorio'
                    }
            ),
            'pais': TextInput(
                attrs = {
                    'type': 'text',
                    'placeholder': 'Ingrese el pais del laboratorio'
                    }
            )
        }