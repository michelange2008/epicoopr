# Generated by Django 3.1.5 on 2021-02-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epicomm', '0022_auto_20210219_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='name',
            field=models.CharField(max_length=191, unique_for_date='created_at', verbose_name='nom de la commande'),
        ),
    ]
