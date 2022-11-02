# Generated by Django 4.1 on 2022-11-02 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_cuota_cuota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partido', models.CharField(max_length=100)),
                ('pronostico', models.CharField(max_length=100)),
                ('cuota', models.DecimalField(decimal_places=2, max_digits=3)),
                ('resultado', models.BooleanField()),
            ],
        ),
    ]
