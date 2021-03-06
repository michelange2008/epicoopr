# Generated by Django 3.1.5 on 2021-02-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epicomm', '0004_auto_20210214_1809'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'produit', 'verbose_name_plural': 'produits alimentaires'},
        ),
        migrations.AlterField(
            model_name='categorie',
            name='icon',
            field=models.ImageField(upload_to='epicomm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='packing',
            field=models.PositiveIntegerField(verbose_name='conditionnement'),
        ),
    ]
