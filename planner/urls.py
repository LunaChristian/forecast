from django.urls import path
from .views import mostrar_ultima_semana

urlpatterns = [
    path('semana/', mostrar_ultima_semana, name='ultima_semana'),
]