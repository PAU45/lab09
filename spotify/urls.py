from django.urls import path
from .views import (
    ArtistaListaVista,
    ArtistaDetalleVista,
    AlbumListaVista,
    AlbumDetalleVista,
    CancionListaVista,
    CancionDetalleVista,
    PlaylistListaVista,
    PlaylistDetalleVista
)

urlpatterns = [
    path('artistas/', ArtistaListaVista.as_view(), name='artista-lista-crear'),
    path('artistas/<int:artista_id>/', ArtistaDetalleVista.as_view(), name='artista-detalle'),
    path('albumes/', AlbumListaVista.as_view(), name='album-lista-crear'),
    path('albumes/<int:album_id>/', AlbumDetalleVista.as_view(), name='album-detalle'),
    path('canciones/', CancionListaVista.as_view(), name='cancion-lista-crear'),
    path('canciones/<int:cancion_id>/', CancionDetalleVista.as_view(), name='cancion-detalle'),
    path('playlists/', PlaylistListaVista.as_view(), name='playlist-lista-crear'),
    path('playlists/<int:playlist_id>/', PlaylistDetalleVista.as_view(), name='playlist-detalle'),
]