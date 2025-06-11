from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from usuario.decorators import admin_required, entrenador_required, atleta_required
from .models import Gym, Entrenador
from .forms import GymForm, EntrenadorForm, UserForm, RedSocialForm
from .forms import RedSocialFormSet
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

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
    total_usuarios = User.objects.count()
    total_entrenadores= Entrenador.objects.count()
    total_gimnasios = Gym.objects.count()
    return render(request, 'administrador/inicio.html', {
        'total_usuarios': total_usuarios,
        'total_entrenadores': total_entrenadores,
        'total_gimnasios': total_gimnasios})
@admin_required
def administrador_entrenadores(request):
    entrenadores = Entrenador.objects.select_related('usuario', 'gym').prefetch_related('redes_sociales')
    return render(request, 'administrador/entrenadores.html', {'entrenadores': entrenadores,})
@admin_required
def crear_entrenador(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        entrenador_form = EntrenadorForm(request.POST, request.FILES)

        if user_form.is_valid() and entrenador_form.is_valid():
            # 1. Crear usuario
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # 2. Agregar al grupo 'entrenador'
            grupo = Group.objects.get(name='entrenador')
            user.groups.add(grupo)

            # 3. Crear entrenador
            entrenador = entrenador_form.save(commit=False)
            entrenador.usuario = user
            entrenador.save()

            # 4. Guardar redes sociales
            formset = RedSocialFormSet(request.POST, instance=entrenador)
            if formset.is_valid():
                formset.save()

            return redirect('usuario:administrador_entrenadores')
        else:
            formset = RedSocialFormSet(request.POST)

    else:
        user_form = UserForm()
        entrenador_form = EntrenadorForm()
        formset = RedSocialFormSet()

    return render(request, 'administrador/crear_entrenador.html', {
        'user_form': user_form,
        'entrenador_form': entrenador_form,
        'formset': formset
    })

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

def lista_entrenadores(request):
    query = request.GET.get("q", "")
    gym_id = request.GET.get("gym", "")
    page_number = request.GET.get("page", 1)

    entrenadores = Entrenador.objects.select_related('usuario', 'gym').prefetch_related('redes_sociales').all()

    if query:
        entrenadores = entrenadores.filter(
            Q(usuario__first_name__icontains=query) |
            Q(usuario__last_name__icontains=query) |
            Q(usuario__email__icontains=query) |
            Q(usuario__username__icontains=query)
        )

    if gym_id:
        entrenadores = entrenadores.filter(gym_id=gym_id)

    paginator = Paginator(entrenadores, 20)
    page_obj = paginator.get_page(page_number)

    context = {
        "entrenadores": page_obj,
        "gyms": Gym.objects.all(),
        "query": query,
        "selected_gym": gym_id
    }

    if request.htmx:
        return render(request, "administrador/partials/_tabla_entrenadores.html", context)
    return render(request, "administrador/entrenadores.html", context)

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


    