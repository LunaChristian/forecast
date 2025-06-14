# Generated by Django 5.2.1 on 2025-06-02 10:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.DateField(unique=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DayEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('domingo', 'Domingo')], max_length=10, verbose_name='Dia')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Cantidad')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='pronosticos.weekplanner')),
            ],
        ),
    ]
