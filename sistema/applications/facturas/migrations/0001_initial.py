# Generated by Django 5.0.2 on 2024-05-06 22:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('num_factura', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Numero Factura')),
                ('fac_fechaLlegada', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Llegada')),
                ('fac_numeroUnidades', models.PositiveIntegerField(verbose_name='Numero de Unidades')),
                ('fac_subtotal', models.FloatField(verbose_name='Subtotal')),
                ('fac_total', models.FloatField(default=0.0, verbose_name='Total')),
                ('img_factura', models.ImageField(blank=True, null=True, upload_to='facturas')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FacturasAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('C', 'Creado'), ('U', 'Actualizado'), ('D', 'Borrado')], max_length=1)),
                ('details', models.TextField(blank=True, null=True)),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IVA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(default=0, verbose_name='IVA')),
            ],
        ),
    ]
