# Generated by Django 3.1.5 on 2021-02-15 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('epicomm', '0005_auto_20210214_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CommandMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191, unique=True, verbose_name='commande')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='créée le ')),
                ('closed_at', models.DateField(verbose_name='fermée le ')),
                ('closed', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Commande globale',
                'verbose_name_plural': 'Commandes globales',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='avaible',
            field=models.BooleanField(default=True, verbose_name='disponible'),
        ),
        migrations.CreateModel(
            name='CommandUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='créée le ')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('paid', models.BooleanField()),
                ('collected', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Commande idividuelle',
                'verbose_name_plural': 'Commandes individuelles',
            },
        ),
    ]
