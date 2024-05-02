from django.shortcuts import render, redirect, get_object_or_404
from .models import Personajes, Fecha
from .forms import PersonajesForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



def index(request):
    personaje = Personajes.objects.all()
    return render(request, 'bookings/index.html', {'personajes': personaje})


@login_required
def crear_personaje(request):
    if request.method == 'POST':
        form = PersonajesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')   
    else:
        form = PersonajesForm()
    
    return render(request, 'bookings/crear_personaje.html', {'form': form})

@login_required
def editar_personaje(request, personaje_id):
    personaje = get_object_or_404(Personajes, pk=personaje_id)
    if request.method == 'POST':
        form = PersonajesForm(request.POST, instance=personaje)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = PersonajesForm(instance=personaje)
    return render(request, 'bookings/editar_personaje.html', {'form': form, 'personaje': personaje})

@login_required
def borrar_personaje(request, personaje_id):
    personaje = get_object_or_404(Personajes, pk=personaje_id)

    if request.method == 'POST':
        personaje.delete()
        return redirect('index')  
    return render(request, 'bookings/index.html', {'personaje': personaje})


def buscar(request):
    query = request.GET.get('query')
    if query:
        query_lower = query.lower()
        resultados_personajes = Personajes.objects.filter(nombre__icontains=query_lower)
    else:
     resultados_personajes = []

    context = {
        'query': query,
        'resultados_personajes': resultados_personajes,
    }
    return render(request, 'bookings/busqueda.html', context)

def custom_login(request):
    if request.method == 'GET':
       form = AuthenticationForm()
    elif request.method == 'POST':
     form = AuthenticationForm(request, data=request.POST)

     if form.is_valid():
         user = form.user_cache
         if user is not None:
             login(request, user)
             return redirect('index')

    return render(request, 'bookings/login.html', {'form': form})



def custom_logout(request):
    logout(request)
    return redirect('login')