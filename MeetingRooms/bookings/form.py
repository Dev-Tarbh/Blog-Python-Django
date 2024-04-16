from django import forms
from .models import Recetas, Saladas, Dulces

class RecetasForm(forms.ModelForm):
        model = Recetas
        fields = '__all__'

class SaladasForm(forms.ModelForm):
        model = Saladas
        fields = '__all__'

class DulcesForm(forms.ModelForm):
        model = Dulces
        fields = '__all__'
