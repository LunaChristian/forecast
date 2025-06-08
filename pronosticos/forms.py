from django import forms
from .models import DayEntry, WeekPlanner

class DayEntryForm(forms.ModelForm):
    class Meta:
        model = DayEntry
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control text-center',
                'min': 0}),
        }

class WeekPlannerForm(forms.ModelForm):
    class Meta:
        model = WeekPlanner
        fields = ['start_day']  # solo permitimos definir la fecha de inicio

    def clean_start_day(self):
        start_day = self.cleaned_data['start_day']

        # Verificar que la fecha ingresada sea un lunes
        if start_day.weekday() != 0:
            raise forms.ValidationError("La semana debe comenzar un lunes.")

        # Verificar que no exista ya una semana con ese mismo inicio
        if WeekPlanner.objects.filter(start_day=start_day).exists():
            raise forms.ValidationError("Ya existe una semana que comienza ese día.")

        return start_day