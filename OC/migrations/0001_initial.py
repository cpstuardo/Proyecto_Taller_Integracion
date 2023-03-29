# Generated by Django 3.2.4 on 2021-06-19 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('cliente', models.CharField(max_length=10)),
                ('proveedor', models.CharField(max_length=10)),
                ('_id', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('sku', models.IntegerField()),
                ('fechaEntrega', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('cantidadDespachada', models.IntegerField()),
                ('precioUnitario', models.IntegerField()),
                ('canal', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=10)),
                ('notas', models.CharField(max_length=10)),
                ('rechazo', models.CharField(max_length=10)),
                ('anulacion', models.CharField(max_length=10)),
                ('urlNotificacion', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
