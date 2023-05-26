# Generated by Django 4.2.1 on 2023-05-22 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("envios", "0002_guiaremitente_numero_alter_guia_tipo_comprobante"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="conductor",
            name="guia",
        ),
        migrations.AddField(
            model_name="conductor",
            name="guia_remitente",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="envios.guiaremitente",
                verbose_name="Guia de Remision",
            ),
        ),
    ]