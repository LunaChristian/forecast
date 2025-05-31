from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WeekPlanner(models.Model):
    start_day = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"La semana comienza el {self.start_day}"

class DayEntry(models.Model):
    
    LISTA_DIAS = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miercoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sabado'),
        ('domingo', 'Domingo'),
    ]
    
    week = models.ForeignKey(WeekPlanner, on_delete=models.CASCADE, related_name='entries')
    day_name = models.CharField(max_length=10, choices=LISTA_DIAS)
    date = models.DateField()
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')