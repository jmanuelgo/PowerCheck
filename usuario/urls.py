# usuario/urls.py
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('singin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
]
