from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Album(models.Model):
    POP = 'pop'
    ROCK = 'rock'
    JAZZ = 'jazz'
    HIP_HOP = 'hip_hop'
    ELECTRONICO = 'electronico'
    CLASICA = 'clasica'

    OPCIONES_GENERO = (
        (POP, 'Pop'),
        (ROCK, 'Rock'),
        (JAZZ, 'Jazz'),
        (HIP_HOP, 'Hip Hop'),
        (ELECTRONICO, 'Electrónico'),
        (CLASICA, 'Clásica'),
    )

    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='albumes')
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=15, choices=OPCIONES_GENERO)

    def __str__(self):
        return f"{self.titulo} de {self.artista.nombre}"


class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')
    duracion = models.DurationField()  # Duración de la canción
    numero_pista = models.PositiveIntegerField()
    calificacion = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.titulo} de {self.album.titulo}"


class Playlist(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)  # Este podría ser un ForeignKey a un modelo de usuario
    canciones = models.ManyToManyField(Cancion, related_name='playlists')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre