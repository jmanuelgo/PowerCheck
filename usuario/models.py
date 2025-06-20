from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gym(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False,unique=True)
    ubucacion = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='gym_logos/', blank=True, null=True,default='gym_logos/default_logo.png')
    celular = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.nombre
    
class Entrenador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='entrenador')
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    celular = models.CharField(max_length=15, blank=False, null=False)
    foto = models.ImageField(upload_to='entrenadores_fotos/', blank=True, null=True, default='entrenadores_fotos/default_photo.png')
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    experiencia= models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"
    
class RedSocial(models.Model):
    REDES = [
        ('IG', 'Instagram'),
        ('FB', 'Facebook'),
        ('X', 'X / Twitter'),
        ('YT', 'YouTube'),
        ('TT', 'TikTok'),
        ('OTRO', 'Otro'),
    ]

    entrenador = models.ForeignKey('Entrenador', on_delete=models.CASCADE, related_name='redes_sociales')
    tipo = models.CharField(max_length=10, choices=REDES)
    url = models.URLField()

    def __str__(self):
        return f"{self.get_tipo_display()}: {self.url}"
class Atleta(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='atleta')
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    celular = models.CharField(max_length=15, blank=False, null=False)
    foto = models.ImageField(upload_to='atletas_fotos/', blank=True, null=True, default='atletas_fotos/default_photo.png')
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')], blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    entrenador= models.ForeignKey('Entrenador', on_delete=models.SET_NULL, null=True, blank=True, related_name='atletas')
    disciplina = models.CharField(max_length=100, blank=True, null=True)
    estilo_vida = models.TextField(blank=True, null=True)
    lesiones_previas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"