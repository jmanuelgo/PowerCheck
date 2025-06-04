from django import forms
from .models import Gym, Entrenador

class GymForm(forms.ModelForm):
    class Meta:
        model = Gym
        fields = ['nombre', 'ubucacion', 'logo', 'celular']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ubucacion': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['nombre', 'apellido', 'gym', 'celular', 'email', 'usuario', 'foto', 'especialidad', 'experiencia', 'redes_sociales']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'experiencia': forms.Textarea(attrs={'class': 'form-control'}),
            'redes_sociales': forms.TextInput(attrs={'class': 'form-control'}),
        }