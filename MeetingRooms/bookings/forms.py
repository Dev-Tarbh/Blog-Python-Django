from django import forms
from .models import Personajes

class PersonajesForm(forms.ModelForm):
    class Meta:
        model = Personajes
        fields = ['nombre', 'serie', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'serie': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }



    