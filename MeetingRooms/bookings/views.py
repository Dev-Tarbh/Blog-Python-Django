from django.shortcuts import render, redirect, get_object_or_404
from .models import Personajes, Avatar
from .forms import PersonajesForm, UserEditForm, AvatarCreateForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

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

def crear_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("Usuario creado:", user.username)
            login(request, user)
            return redirect("index")
 
    return render(request, "bookings/crear_usuario.html", {"form": form})



def ver_descripcion(request, personaje_id):
    personaje = Personajes.objects.get(id=personaje_id)
    return render(request, 'bookings/descripcion.html', {'personaje': personaje})

class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'bookings/editar_usuario.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
    

def avatar_view(request):
        if request.method == "GET":
            contexto = {"form": AvatarCreateForm()}
        else:
           form = AvatarCreateForm(request.POST, request.FILES)
           if form.is_valid():
               image = form.cleaned_data["image"]
               nuevo_avatar = Avatar(image=image, user=request.user)
               nuevo_avatar.save()
               return redirect('index')
           else:
               contexto = {"form": form}

        return render(request, "bookings/avatar_create.html", context=contexto)