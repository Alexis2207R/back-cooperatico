# Generated by Django 4.2.1 on 2023-05-13 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("clientes", "0001_initial"),
        ("inventario", "0001_initial"),
        ("catalogo_sunat", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Factura",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "igv",
                    models.IntegerField(
                        choices=[(18, "ESTANDAR"), (10, "LEY 31556"), (4, "IVAP")],
                        verbose_name="IGV",
                    ),
                ),
                (
                    "tipo_cambio",
                    models.CharField(max_length=200, verbose_name="Tipo de cambio"),
                ),
                (
                    "fecha_emision",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de emisión"
                    ),
                ),
                (
                    "fecha_vencimiento",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de Vencimiento"
                    ),
                ),
                ("estado_pago", models.BooleanField(verbose_name="¿Pagado?")),
                (
                    "clientes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clientes.cliente",
                        verbose_name="Cliente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TipoOperacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.CharField(max_length=6, verbose_name="Código")),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
            ],
        ),
        migrations.CreateModel(
            name="FacturaItems",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad_item", models.PositiveIntegerField(verbose_name="Cantidad")),
                (
                    "factura",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ventas.factura"
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.items",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="factura",
            name="items",
            field=models.ManyToManyField(
                through="ventas.FacturaItems",
                to="inventario.items",
                verbose_name="Items",
            ),
        ),
        migrations.AddField(
            model_name="factura",
            name="moneda",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="catalogo_sunat.moneda",
                verbose_name="Moneda",
            ),
        ),
        migrations.AddField(
            model_name="factura",
            name="tipo_documento",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="catalogo_sunat.tipocomprobante",
                verbose_name="Tipo de Comprobante",
            ),
        ),
        migrations.AddField(
            model_name="factura",
            name="tipo_operacion",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ventas.tipooperacion",
                verbose_name="Tipo Operación",
            ),
        ),
    ]