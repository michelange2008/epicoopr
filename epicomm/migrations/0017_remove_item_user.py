# Generated by Django 3.1.5 on 2021-02-18 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epicomm', '0016_auto_20210216_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]
