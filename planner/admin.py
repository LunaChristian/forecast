from django.contrib import admin
from .models import WeekPlanner, DayEntry

# Inline: permite cargar DayEntry desde la vista de WeekPlanner
class DayEntryInline(admin.TabularInline):  # o admin.TabularInline para estilo vertical
    model = DayEntry
    extra = 0
    readonly_fields = ('day_name', 'date')  # 👈 Opcional: evita que se modifiquen
    can_delete = False                     # 👈 Opcional: evita que se borren desde el admin
    fields = ('day_name', 'date', 'quantity')
    
# Admin de WeekPlanner con los días embebidos
@admin.register(WeekPlanner)
class WeekPlannerAdmin(admin.ModelAdmin):
    inlines = [DayEntryInline]
    list_display = ('start_day', 'created_by')
    list_filter = ('created_by',)
    ordering = ('-start_day',)

# Admin separado (opcional) para ver los DayEntry por separado
""" @admin.register(DayEntry)
class DayEntryAdmin(admin.ModelAdmin):
    list_display = ('week', 'day_name', 'date', 'quantity')
    list_filter = ('day_name', 'week')
    ordering = ('week', 'date')
 """