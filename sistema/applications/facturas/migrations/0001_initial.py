<<<<<<< HEAD
# Generated by Django 5.0.2 on 2024-04-22 21:00
=======
# Generated by Django 5.0.2 on 2024-04-24 20:49
>>>>>>> 243e933845d4838b38c6f00a8dcbae588ca398d4

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pedidos', '0001_initial'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IVA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(default=0, verbose_name='IVA')),
            ],
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('num_factura', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Numero Factura')),
                ('fac_fechaLlegada', models.DateField(verbose_name='Fecha Llegada')),
                ('fac_numeroUnidades', models.PositiveIntegerField(verbose_name='Numero de Unidades')),
                ('fac_subtotal', models.FloatField(verbose_name='Subtotal')),
                ('fac_total', models.FloatField(default=0.0, verbose_name='Total')),
                ('img_factura', models.ImageField(blank=True, null=True, upload_to='facturas')),
                ('fac_numeroPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedidos')),
                ('fac_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedores')),
                ('fac_iva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.iva')),
            ],
        ),
    ]
