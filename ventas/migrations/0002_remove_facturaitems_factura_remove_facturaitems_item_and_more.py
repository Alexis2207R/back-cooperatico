# Generated by Django 4.2.1 on 2023-05-25 22:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ventas", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="facturaitems",
            name="factura",
        ),
        migrations.RemoveField(
            model_name="facturaitems",
            name="item",
        ),
        migrations.DeleteModel(
            name="Factura",
        ),
        migrations.DeleteModel(
            name="FacturaItems",
        ),
        migrations.DeleteModel(
            name="TipoOperacion",
        ),
        migrations.DeleteModel(
            name="TipoPercepcion",
        ),
    ]
