from django import forms
from .models import DayEntry

class DayEntryForm(forms.ModelForm):
    class Meta:
        model = DayEntry
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control text-center',
                'min': 0}),
        }