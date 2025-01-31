# Generated by Django 5.1.2 on 2024-10-15 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('biografia', models.TextField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_lanzamiento', models.DateField()),
                ('genero', models.CharField(choices=[('pop', 'Pop'), ('rock', 'Rock'), ('jazz', 'Jazz'), ('hip_hop', 'Hip Hop'), ('electronico', 'Electrónico'), ('clasica', 'Clásica')], max_length=15)),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albumes', to='spotify.artista')),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('duracion', models.DurationField()),
                ('numero_pista', models.PositiveIntegerField()),
                ('calificacion', models.IntegerField(default=0)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='canciones', to='spotify.album')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('canciones', models.ManyToManyField(related_name='playlists', to='spotify.cancion')),
            ],
        ),
    ]
