# Generated by Django 3.2.4 on 2021-06-19 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendecompra',
            name='cliente',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ordendecompra',
            name='proveedor',
            field=models.CharField(max_length=30),
        ),
    ]
