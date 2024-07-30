# Generated by Django 5.0.7 on 2024-07-30 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=11)),
                ('fechaNacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('celular', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Deportista',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Personas.persona')),
                ('golesAnotados', models.IntegerField()),
                ('categoria', models.CharField(max_length=50)),
            ],
            bases=('Personas.persona',),
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Personas.persona')),
                ('preparacion', models.CharField(max_length=50)),
            ],
            bases=('Personas.persona',),
        ),
        migrations.CreateModel(
            name='Juez',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='Personas.persona')),
                ('idJuez', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            bases=('Personas.persona',),
        ),
    ]