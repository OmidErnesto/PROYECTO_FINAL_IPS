from django.urls import path
from AppTurismo.views import (
    CrearZonaTuristica,
    BorrarZonaTuristica,
    ZonaTuristicaDetailsView,
    ZonaTuristicaEdit,
    ZonaTuristicaListView,
    ZonaTuristicaRegistro,
    
)

app_name = 'AppTurismo'
urlpatterns = [
    path('agregar/',ZonaTuristicaRegistro.as_view(), name='Crear-ZonaTuristica'),
    #path('',ListarPelicula, name='Listar Pelicula'),
    #path('<str:myTitle>/', DescripcionPelicula, name='Ver Descripcion'),
    path('<str:myTitle>/borrar/', BorrarZonaTuristica, name='Borrar ZonaTuristica'),
    path('',ZonaTuristicaListView.as_view(), name='zonaturismo-list'),
    path('<str:pk>/', ZonaTuristicaDetailsView.as_view(), name='zona-detail'),
    path('<str:myTitle>/update/', ZonaTuristicaEdit, name='Editar ZonaTuristica'),
    
]
