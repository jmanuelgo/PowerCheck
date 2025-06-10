from django import forms
from .models import Gym, Entrenador,RedSocial
from django.contrib.auth.models import User

class GymForm(forms.ModelForm):
    class Meta:
        model = Gym
        fields = ['nombre', 'ubucacion', 'logo', 'celular']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ubucacion': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña temporal")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['gym', 'celular', 'foto', 'especialidad', 'experiencia']

class RedSocialForm(forms.ModelForm):
    class Meta:
        model = RedSocial
        fields = ['tipo', 'url']

RedSocialFormSet = forms.inlineformset_factory(
    Entrenador, RedSocial,
    form=RedSocialForm,
    extra=1,
    can_delete=True
)