# Generated by Django 5.0.2 on 2024-04-22 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturas',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
