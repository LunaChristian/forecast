from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WeekPlanner
from .forms import DayEntryForm

@login_required
def home_redirect(request):
    # Redirige al nombre de vista configurado como inicio tras login
    return redirect('ultima_semana')


@login_required 
def mostrar_ultima_semana(request):
    semana = WeekPlanner.objects.order_by('-start_day').first()
    entradas = semana.entries.order_by('date') if semana else []

    if request.method == 'POST':
        for entrada in entradas:
            form = DayEntryForm(request.POST, instance=entrada, prefix=str(entrada.id))
            if form.is_valid():
                form.save()
        return redirect('ultima_semana')

    forms = [DayEntryForm(instance=entrada, prefix=str(entrada.id)) for entrada in entradas]

    context = {
        'semana': semana,
        'entradas': entradas,
        'forms': forms,
    }
    return render(request, 'pronosticos/week_detail.html', context)
