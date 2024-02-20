# Generated by Django 5.0.2 on 2024-02-20 19:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insumos', '0001_initial'),
        ('materiaprima', '0001_initial'),
        ('proveedores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('ref_pedido', models.IntegerField(unique=True, verbose_name='Referencia')),
                ('pedi_fecha', models.DateField(verbose_name='fecha')),
                ('pedi_estado', models.CharField(choices=[('0', 'Completo'), ('1', 'Incompleto'), ('2', 'Rechazado')], max_length=1, verbose_name='estado')),
                ('pedi_comprobatePago', models.CharField(max_length=45, verbose_name='Comprobante Pago')),
                ('pedi_insumos', models.ManyToManyField(to='insumos.implementostrabajo')),
                ('pedi_materiaprima', models.ManyToManyField(to='materiaprima.materiaprima')),
                ('pedi_proveedor', models.ManyToManyField(to='proveedores.proveedores')),
                ('pedi_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
