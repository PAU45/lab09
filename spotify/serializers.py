from rest_framework import serializers
from .models import Artista, Album, Cancion, Playlist

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['id', 'nombre', 'biografia', 'fecha_nacimiento']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'titulo', 'artista', 'fecha_lanzamiento', 'genero']


class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = ['id', 'titulo', 'album', 'duracion', 'numero_pista', 'calificacion']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'nombre', 'usuario', 'canciones', 'fecha_creacion', 'descripcion']