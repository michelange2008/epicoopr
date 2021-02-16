# Generated by Django 3.1.5 on 2021-02-16 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('epicomm', '0013_auto_20210216_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commandline',
            name='commandUser',
        ),
        migrations.RemoveField(
            model_name='commanduser',
            name='products',
        ),
        migrations.AddField(
            model_name='commandline',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commanduser',
            name='commandLine',
            field=models.ManyToManyField(to='epicomm.CommandLine'),
        ),
    ]
