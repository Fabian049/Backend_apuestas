# Generated by Django 4.1 on 2022-10-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuota',
            name='cuota',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
