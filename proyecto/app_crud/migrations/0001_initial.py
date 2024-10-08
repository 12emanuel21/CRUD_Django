# Generated by Django 5.1 on 2024-08-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=150)),
                ('Apellido', models.CharField(max_length=150)),
                ('Email', models.EmailField(max_length=150)),
                ('Edad', models.IntegerField()),
                ('Generos', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=100)),
                ('Salario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Fecha_inicial', models.DateTimeField(auto_now_add=True, null=True)),
                ('Fecha_actualizada', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'empleados',
                'ordering': ['-Fecha_inicial'],
            },
        ),
    ]
