# Generated by Django 5.0.2 on 2024-04-22 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materiaprima', '0001_initial'),
        ('procesamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoTerminado',
            fields=[
                ('pt_lote', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('pt_cantidad', models.IntegerField(default=100)),
                ('pt_fechapreparacion', models.DateField(verbose_name='Fecha Preparacion')),
                ('pt_fechavencimiento', models.DateField(verbose_name='Fecha Vencimiento')),
                ('idCoccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procesamiento.coccion')),
                ('idPicado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procesamiento.picado')),
            ],
        ),
        migrations.CreateModel(
            name='ExistenciaPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exisPT_CantidadIngresada', models.IntegerField(verbose_name='Cantidad Ingresada')),
                ('exisPT_CantidadEgresada', models.IntegerField(verbose_name='Cantidad Egresada')),
                ('pt_lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productoterminado.productoterminado')),
            ],
        ),
        migrations.CreateModel(
            name='EmpaqueProductoTerminado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_pesoKg', models.FloatField(verbose_name='Peso Empaque')),
                ('emp_cantidadBolsas', models.IntegerField(verbose_name='Cantidad Bolsas')),
                ('pt_lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productoterminado.productoterminado')),
            ],
        ),
        migrations.CreateModel(
            name='CaracteristicasOrganolepticasPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.CharField(max_length=50, verbose_name='Observaciones')),
                ('olor', models.BooleanField(default=False, verbose_name='Olor')),
                ('sabor', models.BooleanField(default=False, verbose_name='Sabor')),
                ('textura', models.BooleanField(default=False, verbose_name='Textura')),
                ('color', models.BooleanField(default=False, verbose_name='Color')),
                ('estado', models.CharField(choices=[('0', 'Aprobado'), ('1', 'No Aprobado')], max_length=1, verbose_name='Estado')),
                ('pt_lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productoterminado.productoterminado')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoTerminadoGenerico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_nombre', models.CharField(max_length=50, verbose_name='Nombre Producto Terminado')),
                ('materiaPrimaUsada', models.ManyToManyField(to='materiaprima.materiaprimagenerica')),
            ],
        ),
        migrations.AddField(
            model_name='productoterminado',
            name='pt_nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productoterminado.productoterminadogenerico'),
        ),
        migrations.CreateModel(
            name='Vacio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_bolsas_rechazadas', models.IntegerField(verbose_name='Cantidad Bolsas Rechazadas')),
                ('cantidad_bolsas_liberadas', models.IntegerField(verbose_name='Cantidad Bolsas Liberadas')),
                ('pt_lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productoterminado.productoterminado')),
            ],
        ),
    ]
