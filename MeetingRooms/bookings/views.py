
from django.shortcuts import render
from .models import Recetas, Saladas, Dulces

def index(request):
    recetas = Recetas.objects.all()
    saladas = Saladas.objects.all()
    dulces = Dulces.objects.all()
    return render(request, 'bookings/index.html', {'recetas': recetas, 'saladas': saladas, 'dulces': dulces})

def busqueda(request):
    query = request.GET.get('query')
    
    resultados_recetas = Recetas.objects.filter(nombre__icontains=query) if query else []
    resultados_saladas = Saladas.objects.filter(nombre__icontains=query) if query else []
    resultados_dulces = Dulces.objects.filter(nombre__icontains=query) if query else []
    
    context = {
        'query': query,
        'resultados_recetas': resultados_recetas,
        'resultados_saladas': resultados_saladas,
        'resultados_dulces': resultados_dulces,
    }
    
    return render(request, 'busqueda.html', context)