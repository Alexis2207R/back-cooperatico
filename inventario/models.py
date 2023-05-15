from django.db import models
from catalogo_sunat.models import Moneda


class CategoriaItem(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=6, default="0001")
    nombre = models.CharField(verbose_name="Categoria Item", max_length=100, default="LINEA BLANCA")


class TipoItem(models.Model):
    nombre = models.CharField(verbose_name="Tipo Item", max_length=100)


class TipoAfectacion(models.Model):
    nombre = models.CharField(verbose_name="Tipo de Afectacion", max_length=50)


class CodigoSunat(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=50, unique=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=50, unique=True)


class Items(models.Model):
    codigo = models.CharField(max_length=50) # Queda pendiente
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    tipo = models.ForeignKey(TipoItem, verbose_name="Tipo de Item", on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaItem, verbose_name="Categoria", on_delete=models.CASCADE)
    codigo_sunat = models.ForeignKey(CodigoSunat, verbose_name="Código de la SUNAT", on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, verbose_name="Moneda", on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(verbose_name="Stock", default=0)
    peso = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso")
    valor_venta = models.PositiveIntegerField(verbose_name="Valor de Venta Unitario sin IGV (al que se vendera)")
    precio_venta = models.PositiveIntegerField(verbose_name="Precio de Venta Unitario con IGV (al que se vendera)")
    valor_compra = models.PositiveIntegerField(verbose_name="Valor de Compra Unitario con IGV (al que se compró)")
    precio_compra = models.PositiveIntegerField(verbose_name="Precio de Compra Unitario con IGV (al que se compró)")
    destacado = models.BooleanField(verbose_name="Destacado")