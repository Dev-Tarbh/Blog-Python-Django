from django.shortcuts import render, redirect
from .models import Recetas, Saladas, Dulces
from .forms import RecetasForm, SaladasForm, DulcesForm
from django import forms
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




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
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            categoria_id = form.cleaned_data['categoria']
            if categoria_id == '0':
               
                pass
            elif categoria_id == '1':
               
                pass
            elif categoria_id == '2':
            
                pass

            messages.success(request, '¡La receta se ha guardado correctamente!')
            return redirect('index')
        else:
            messages.error(request, '¡Por favor corrija los errores del formulario!')
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
    return render(request, 'bookings/crear_receta.html', {'form': form})

def crear_receta_dulce(request):
    if request.method == 'POST':
        form = DulcesForm(request.POST)
        if form.is_valid():
            form.save()
            print("La receta se guardó correctamente.")
            return redirect('index')
        else:
            print("El formulario no es válido. Errores:", form.errors)

    else:
        form = DulcesForm()
    return render(request, 'bookings/crear_receta.html', {'form': form})

class RecetasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecetasForm, self).__init__(*args, **kwargs)
        self.fields['categoria'] = forms.ChoiceField(label='Categoría', choices=self.get_categorias_choices())

    def get_categorias_choices(self):
        return Recetas.CATEGORIAS

    nombre = forms.CharField(label='Nombre', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)

    class Meta:
        model = Recetas
        fields = ['nombre', 'descripcion', 'categoria']


def index(request):
    recetas = Recetas.objects.all()
    saladas = Saladas.objects.all()
    dulces = Dulces.objects.all()
    return render(request, 'bookings/index.html', {'recetas': recetas, 'saladas': saladas, 'dulces': dulces})

def editar_receta(request, receta_id):
    receta = get_object_or_404(Recetas, pk=receta_id)
    if request.method == 'POST':
        form = RecetasForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecetasForm(instance=receta)
    return render(request, 'bookings/editar_receta.html', {'form': form, 'receta': receta})

def borrar_receta(request, borrar_id):
    receta = get_object_or_404(Recetas, pk=borrar_id)
    if request.method == 'POST':
        receta.delete()
        return redirect('index')
    return render(request, 'bookings/confirmar_borrar_receta.html', {'receta': receta})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            messages.error(request, 'Por favor, inténtalo de nuevo.')
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')