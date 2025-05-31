from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

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
    
    week = models.ForeignKey('WeekPlanner', on_delete=models.CASCADE, related_name='entries')
    day_name = models.CharField(max_length=10, choices=LISTA_DIAS, verbose_name='Dia')
    date = models.DateField(verbose_name='Fecha')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Cantidad')

class WeekPlanner(models.Model):
    start_day = models.DateField(unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.start_day.weekday() != 0:
            raise ValidationError("La fecha de inicio debe ser un lunes.")

        nuevo = self.pk is None  # Solo si es un objeto nuevo
        super().save(*args, **kwargs)

        if nuevo:
            dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
            for i in range(7):
                fecha = self.start_day + timedelta(days=i)
                DayEntry.objects.create(
                    week=self,
                    day_name=dias[i],
                    date=fecha,
                    quantity=0
                )
    
    def __str__(self):
        return f"La semana comienza el {self.start_day.strftime('%d/%m/%Y')}"

