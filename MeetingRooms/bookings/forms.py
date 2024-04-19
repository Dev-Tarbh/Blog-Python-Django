from django import forms
from .models import Recetas, Saladas, Dulces

class RecetasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecetasForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].choices = self.get_categorias_choices()

    def get_categorias_choices(self):
        categorias = Recetas.objects.values_list('categoria', flat=True).distinct()
        return [(categoria, categoria.capitalize()) for categoria in categorias]

    nombre = forms.CharField(label='Nombre', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)
    categoria = forms.CharField(label='Categoría', max_length=100)  

    class Meta:
        model = Recetas
        fields = ['nombre', 'descripcion', 'categoria']

class SaladasForm(forms.ModelForm):
    class Meta:
        model = Saladas
        fields = '__all__'

class DulcesForm(forms.ModelForm):
    class Meta:
        model = Dulces
        fields = '__all__'
