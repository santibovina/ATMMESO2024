# Generated by Django 5.0.1 on 2024-06-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0012_alter_detallegaveta_total_por_gaveta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operacion',
            name='total_por_gaveta',
        ),
        migrations.AlterField(
            model_name='detallegaveta',
            name='total_por_gaveta',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
