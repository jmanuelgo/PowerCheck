from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from usuario.decorators import admin_required 


def signin(request):
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name='admin').exists():
            return redirect('admin:index')
        elif user.groups.filter(name='entrenador').exists():
            return redirect('entrenador:index')
        elif user.groups.filter(name='atleta').exists():
            return redirect('atleta:index')
        else:
            messages.error(request, "No perteneces a ningún grupo válido.")
            return redirect('singin.html')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.groups.filter(name='admin').exists():
                return redirect('admin:index')
            elif user.groups.filter(name='entrenador').exists():
                return redirect('entrenador:index')
            elif user.groups.filter(name='atleta').exists():
                return redirect('atleta:index')
            else:
                messages.error(request, "No perteneces a ningún grupo válido.")
                return redirect('singin.html')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'singin.html', {'form': form})


def signout(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('usuario:signin')


    