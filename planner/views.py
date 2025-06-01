from django.shortcuts import render
from .models import WeekPlanner

def mostrar_ultima_semana(request):
    semana = WeekPlanner.objects.order_by('-start_day').first()
    context = {
        'semana': semana,
        'entradas': semana.entries.order_by('date') if semana else []
    }
    return render(request, 'planner/week_detail.html', context)