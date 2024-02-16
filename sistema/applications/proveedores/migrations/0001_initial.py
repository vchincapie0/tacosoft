# Generated by Django 5.0.2 on 2024-02-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('prov_id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('nit', models.IntegerField(unique=True, verbose_name='NIT')),
                ('prov_nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('prov_telefono', models.CharField(max_length=10, verbose_name='Telefono')),
            ],
        ),
    ]
