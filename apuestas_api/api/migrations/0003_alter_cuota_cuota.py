# Generated by Django 4.1 on 2022-10-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_cuota_cuota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuota',
            name='cuota',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
