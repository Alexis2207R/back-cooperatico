# Generated by Django 4.2.1 on 2023-05-21 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("catalogo_sunat", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                    "numero_de_documento",
                    models.CharField(max_length=15, verbose_name="Número de Documento"),
                ),
                ("nombre", models.CharField(max_length=100, verbose_name="Titulo")),
                (
                    "direccion",
                    models.CharField(max_length=100, verbose_name="Dirección"),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=250, verbose_name="Email"),
                ),
                (
                    "email_1",
                    models.EmailField(
                        blank=True, max_length=250, verbose_name="Email 2"
                    ),
                ),
                (
                    "email_2",
                    models.EmailField(
                        blank=True, max_length=250, verbose_name="Email 3"
                    ),
                ),
                (
                    "tipo_documento_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogo_sunat.tipodocumento",
                        verbose_name="Tipo de Documento",
                    ),
                ),
            ],
        ),
    ]
