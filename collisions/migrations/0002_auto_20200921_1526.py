# Generated by Django 2.2.16 on 2020-09-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collisions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtp',
            name='concentration_accidents',
            field=models.CharField(blank=True, max_length=10, verbose_name='Является местом концентрации ДТП'),
        ),
    ]
