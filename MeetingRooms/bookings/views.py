from django.shortcuts import render, redirect
from .models import Recetas, Saladas, Dulces
from .forms import RecetasForm, SaladasForm, DulcesForm
from django import forms


def index(request):
    recetas = Recetas.objects.all()
    saladas = Saladas.objects.all()
    dulces = Dulces.objects.all()
    return render(request, 'bookings/index.html', {'recetas': recetas, 'saladas': saladas, 'dulces': dulces})

def buscar(request):
    query = request.GET.get('query')
    if query:
        query_lower = query.lower()
        resultados_recetas = Recetas.objects.filter(nombre__icontains=query_lower)
        resultados_saladas = Saladas.objects.filter(nombre__icontains=query_lower)
        resultados_dulces = Dulces.objects.filter(nombre__icontains=query_lower)
    else:
        resultados_recetas = []
        resultados_saladas = []
        resultados_dulces = []

    context = {
        'query': query,
        'resultados_recetas': resultados_recetas,
        'resultados_saladas': resultados_saladas,
        'resultados_dulces': resultados_dulces,
    }
    return render(request, 'bookings/busqueda.html', context)


def crear_receta(request):
    if request.method == 'POST':
        form = RecetasForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('index')
    else:
        form = RecetasForm()
    return render(request, 'bookings/crear_receta.html', {'form': form})

def crear_receta_salada(request):
    if request.method == 'POST':
        form = SaladasForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('index')
    else:
        form = SaladasForm()
    return render(request, 'bookings/crear_receta_salada.html', {'form': form})

def crear_receta_dulce(request):
    if request.method == 'POST':
        form = DulcesForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = DulcesForm()
    return render(request, 'bookings/crear_receta_dulce.html', {'form': form})

class RecetasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecetasForm, self).__init__(*args, **kwargs)
        self.fields['categoria'] = forms.ChoiceField(label='Categoría', choices=self.get_categorias_choices())

    def get_categorias_choices(self):
     categorias = Recetas.objects.values_list('categoria', flat=True).distinct()
     return [(str(categoria), str(categoria).capitalize()) for categoria in categorias]


    nombre = forms.CharField(label='Nombre', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)

    class Meta:
        model = Recetas
        fields = ['nombre', 'descripcion', 'categoria']
