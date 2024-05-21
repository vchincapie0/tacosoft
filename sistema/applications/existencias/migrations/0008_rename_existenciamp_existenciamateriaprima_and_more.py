# Generated by Django 5.0.2 on 2024-05-21 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('existencias', '0007_alter_existenciamp_codigo'),
        ('insumos', '0003_insumosgenerico_cantidad_total'),
        ('materiaprima', '0003_materiaprimaaudit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExistenciaMp',
            new_name='ExistenciaMateriaPrima',
        ),
        migrations.CreateModel(
            name='ExistenciasImplementosTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaingreso', models.DateTimeField(auto_now_add=True)),
                ('implemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.insumosgenerico')),
            ],
        ),
    ]