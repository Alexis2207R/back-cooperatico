# Generated by Django 4.2.1 on 2023-05-13 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("catalogo_sunat", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoriaItem",
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
                    "codigo",
                    models.CharField(
                        default="0001", max_length=6, verbose_name="Código"
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        default="LINEA BLANCA",
                        max_length=100,
                        verbose_name="Categoria Item",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CodigoSunat",
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
                    "codigo",
                    models.CharField(max_length=50, unique=True, verbose_name="Código"),
                ),
                (
                    "nombre",
                    models.CharField(max_length=50, unique=True, verbose_name="Nombre"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TipoAfectacion",
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
                    "nombre",
                    models.CharField(max_length=50, verbose_name="Tipo de Afectacion"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TipoItem",
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
                ("nombre", models.CharField(max_length=100, verbose_name="Tipo Item")),
            ],
        ),
        migrations.CreateModel(
            name="Items",
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
                ("codigo", models.CharField(max_length=50)),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
                ("stock", models.PositiveIntegerField(default=0, verbose_name="Stock")),
                (
                    "peso",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Peso"
                    ),
                ),
                (
                    "valor_venta",
                    models.PositiveIntegerField(
                        verbose_name="Valor de Venta Unitario sin IGV (al que se vendera)"
                    ),
                ),
                (
                    "precio_venta",
                    models.PositiveIntegerField(
                        verbose_name="Precio de Venta Unitario con IGV (al que se vendera)"
                    ),
                ),
                (
                    "valor_compra",
                    models.PositiveIntegerField(
                        verbose_name="Valor de Compra Unitario con IGV (al que se compró)"
                    ),
                ),
                (
                    "precio_compra",
                    models.PositiveIntegerField(
                        verbose_name="Precio de Compra Unitario con IGV (al que se compró)"
                    ),
                ),
                ("destacado", models.BooleanField(verbose_name="Destacado")),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.categoriaitem",
                        verbose_name="Categoria",
                    ),
                ),
                (
                    "codigo_sunat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.codigosunat",
                        verbose_name="Código de la SUNAT",
                    ),
                ),
                (
                    "moneda",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogo_sunat.moneda",
                        verbose_name="Moneda",
                    ),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.tipoitem",
                        verbose_name="Tipo de Item",
                    ),
                ),
            ],
        ),
    ]
