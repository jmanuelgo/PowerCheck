# usuario/urls.py
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    # Dashboards
    path('administrador/dashboard/', views.administrador_dashboard, name='administrador_dashboard'),
    path('entrenador/dashboard/', views.entrenador_dashboard, name='entrenador_dashboard'),
    path('atleta/dashboard/', views.atleta_dashboard, name='atleta_dashboard'),
    # administrador
    path('administrador/entrenadores/', views.administrador_entrenadores, name='administrador_entrenadores'),
    path('administrador/gimnasios/', views.administrador_gimnasios, name='administrador_gimnasios'),
    path('administrador/gimnasios/crear/', views.crear_gym, name='crear_gym'),
    path('administrador/entrenadores/crear/', views.crear_entrenador, name='crear_entrenador'),
    path('entrenadores/', views.lista_entrenadores, name='entrenadores'),

]
