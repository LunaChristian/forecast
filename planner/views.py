from django.shortcuts import render, redirect
from .models import WeekPlanner
from .forms import DayEntryForm

def mostrar_ultima_semana(request):
    semana = WeekPlanner.objects.order_by('-start_day').first()
    entradas = semana.entries.order_by('date') if semana else []

    if request.method == 'POST':
        for entrada in entradas:
            form = DayEntryForm(request.POST, instance=entrada, prefix=str(entrada.id))
            if form.is_valid():
                form.save()
        return redirect('ultima_semana')  # redirige tras guardar

    # Si es GET, generamos los formularios para mostrar
    forms = [DayEntryForm(instance=entrada, prefix=str(entrada.id)) for entrada in entradas]

    context = {
        'semana': semana,
        'entradas': entradas,
        'forms': forms,
    }
    return render(request, 'planner/week_detail.html', context)

