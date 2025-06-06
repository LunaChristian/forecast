from django.urls import path
from .views import dashboard, detalle_semana, historial, mostrar_ultima_semana, ver_semana_actual

app_name = 'pronosticos'

urlpatterns = [
    path('semana/', mostrar_ultima_semana, name='ultima_semana'),
    path('dashboard/', dashboard, name='dashboard'),
    path('semana-actual/', ver_semana_actual, name='ver_semana_actual'),
    path('semana/<int:semana_id>/', detalle_semana, name='detalle_semana'),
    path('historial/', historial, name='historial'),
]
