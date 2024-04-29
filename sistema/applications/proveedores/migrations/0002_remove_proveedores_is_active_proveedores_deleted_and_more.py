# Generated by Django 5.0.2 on 2024-04-29 23:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedores',
            name='is_active',
        ),
        migrations.AddField(
            model_name='proveedores',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ProveedoresAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('C', 'Creado'), ('U', 'Actualizado'), ('D', 'Borrado')], max_length=1)),
                ('details', models.TextField(blank=True, null=True)),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('proveedor', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='audit_logs', to='proveedores.proveedores')),
            ],
        ),
    ]
