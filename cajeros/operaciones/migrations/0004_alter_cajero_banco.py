# Generated by Django 5.0.1 on 2024-06-04 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0003_banco_remove_cajero_entidad_cajero_ubicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajero',
            name='banco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operaciones.banco'),
        ),
    ]
