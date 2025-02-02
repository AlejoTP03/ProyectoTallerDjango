# Generated by Django 5.1.4 on 2024-12-27 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('ci', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('matricula', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('ci_mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_app.mecanico')),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('ci', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('carros', models.ManyToManyField(related_name='carros', to='gestion_app.carro')),
            ],
        ),
    ]
