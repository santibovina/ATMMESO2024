# Generated by Django 5.0.1 on 2024-06-04 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cajero',
            old_name='descripcion',
            new_name='entidad',
        ),
    ]
