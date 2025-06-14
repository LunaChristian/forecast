from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect
from datetime import date, timedelta
from .models import WeekPlanner
from .forms import DayEntryForm, WeekPlannerForm

@login_required
@permission_required('pronosticos.change_dayentry', raise_exception=True)
def dashboard(request):
    hoy = date.today()
    lunes_actual = hoy - timedelta(days=hoy.weekday())
    semanas = WeekPlanner.objects.filter(start_day__gte=lunes_actual).order_by('start_day')
    return render(request, 'pronosticos/dashboard.html', {'semanas': semanas})

@login_required
def home_redirect(request):
    if request.user.has_perm('pronosticos.change_dayentry'):
        return redirect('pronosticos:dashboard')
    else:
        return redirect('pronosticos:ver_semana_actual')

@login_required 
def mostrar_ultima_semana(request):
    semana = WeekPlanner.objects.order_by('-start_day').first()
    entradas = semana.entries.order_by('date') if semana else []
    
    if request.method == 'POST':
        if not request.user.has_perm('pronosticos.change_dayentry'):
            return redirect('pronosticos:ultima_semana')  # evitar edición no autorizada
        
        for entrada in entradas:
            form = DayEntryForm(request.POST, instance=entrada, prefix=str(entrada.id))
            if form.is_valid():
                form.save()
        return redirect('pronosticos:ultima_semana')

    forms = []
    if request.user.has_perm('pronosticos.change_dayentry'):
        forms = [DayEntryForm(instance=entrada, prefix=str(entrada.id)) for entrada in entradas]

    context = {
        'semana': semana,
        'entradas': entradas,
        'forms': forms,
    }
    return render(request, 'pronosticos/week_detail.html', context)

@login_required
def ver_semana_actual(request):
    hoy = date.today()
    inicio = hoy - timedelta(days=hoy.weekday())
    
    try:
        semana = WeekPlanner.objects.get(start_day=inicio)
    except WeekPlanner.DoesNotExist:
        return render(request, 'pronosticos/sin_semana.html')
    
    entradas = semana.entries.order_by('date')
    
    context = {
        'semana': semana,
        'entradas': entradas,
        'forms': [],  # ← vacío: no hay edición
    }
    return render(request, 'pronosticos/week_detail.html', context)

@login_required
def detalle_semana(request, semana_id):
    semana = get_object_or_404(WeekPlanner, id=semana_id)
    entradas = semana.entries.order_by('date')
    forms = []

    if request.user.has_perm('pronosticos.change_dayentry'):
        forms = [DayEntryForm(instance=entrada, prefix=str(entrada.id)) for entrada in entradas]

    context = {
        'semana': semana,
        'entradas': entradas,
        'forms': forms,
    }
    return render(request, 'pronosticos/week_detail.html', context)

@login_required
@permission_required('pronosticos.change_dayentry', raise_exception=True)
def historial(request):
    #hoy = date.today()
    #lunes_actual = hoy - timedelta(days=hoy.weekday())
    semanas = WeekPlanner.objects.order_by('start_day')
    
    context = {
        'semanas': semanas
    }
    return render(request, 'pronosticos/historial.html', context)

@login_required
@permission_required('pronosticos.change_dayentry', raise_exception=True)
def crear_semana(request):
    if request.method == 'POST':
        form = WeekPlannerForm(request.POST)
        if form.is_valid():
            semana = form.save(commit=False)
            semana.created_by = request.user
            semana.save()
            return redirect('pronosticos:dashboard')
    else:
        form = WeekPlannerForm()
    return render(request, 'pronosticos/crear_semana.html', {'form':form})