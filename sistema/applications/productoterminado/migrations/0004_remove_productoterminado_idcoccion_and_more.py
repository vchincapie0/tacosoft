# Generated by Django 5.0.2 on 2024-05-23 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productoterminado', '0003_rename_productoterminado_productoterminadoaudit_productoterminado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoterminado',
            name='idCoccion',
        ),
        migrations.RemoveField(
            model_name='productoterminado',
            name='idPicado',
        ),
    ]
