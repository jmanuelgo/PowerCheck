# Generated by Django 4.2.21 on 2025-06-10 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atleta',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='atleta',
            name='email',
        ),
        migrations.RemoveField(
            model_name='atleta',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='entrenador',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='entrenador',
            name='email',
        ),
        migrations.RemoveField(
            model_name='entrenador',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='entrenador',
            name='redes_sociales',
        ),
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('IG', 'Instagram'), ('FB', 'Facebook'), ('X', 'X / Twitter'), ('YT', 'YouTube'), ('TT', 'TikTok'), ('OTRO', 'Otro')], max_length=10)),
                ('url', models.URLField()),
                ('entrenador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redes_sociales', to='usuario.entrenador')),
            ],
        ),
    ]
