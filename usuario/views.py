from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from usuario.decorators import admin_required, entrenador_required, atleta_required
from .models import Gym
from .forms import GymForm

def inicio(request):
    return render(request,'inicio.html')

def signin(request):
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name='administrador').exists():
            return redirect('usuario:administrador_dashboard')
        elif user.groups.filter(name='entrenador').exists():
            return redirect('entrenador_dashboard')
        elif user.groups.filter(name='atleta').exists():
            return redirect('atleta_dashboard')
        else:
            messages.error(request, "No perteneces a ningún grupo válido.")
            return redirect('signin.html')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.groups.filter(name='administrador').exists():
                return redirect('usuario:administrador_dashboard')
            elif user.groups.filter(name='entrenador').exists():
                return redirect('usuario:entrenador_dashboard')
            elif user.groups.filter(name='atleta').exists():
                return redirect('atleta_dashboard')
            else:
                messages.error(request, "No perteneces a ningún grupo válido.")
                return redirect('signin.html')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})

#funciones del administrador
@admin_required
def administrador_dashboard(request):
    return render(request, 'administrador/inicio.html')
@admin_required
def administrador_entrenadores(request):
    return render(request, 'administrador/entrenadores.html')
@admin_required
def administrador_gimnasios(request):
    Gyms = Gym.objects.all()
    return render(request, 'administrador/gym.html', {'gyms': Gyms})

@admin_required
def crear_gym(request):
    if request.method == 'POST':
        form = GymForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Gimnasio creado exitosamente.")
            return redirect('usuario:administrador_gimnasios')
    else:
        form = GymForm()
    
    return render(request, 'administrador/crear_gym.html', {'form': form})

#funciones del entrenador
@entrenador_required
def entrenador_dashboard(request):
    return render(request, 'entrenador/dashboard.html')

#funciones del atleta
@atleta_required
def atleta_dashboard(request):
    return redirect(request, 'atleta/dashboard.html')
def signout(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('usuario:signin')


    