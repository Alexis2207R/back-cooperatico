from django.db import models


class Serie(models.Model):
    nombre = models.CharField(max_length=4, verbose_name="Nombre")
    numero = models.IntegerField(verbose_name="Número (Referencial)")


class TipoComprobante(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    serie = models.ForeignKey(Serie, verbose_name="Serie", on_delete=models.CASCADE)


class TipoDocumento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=2, unique=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre", unique=True)

class Moneda(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    

class MotivoTraslado(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Motivo de Traslado")


class Departamento(models.Model):
    codigo = models.CharField(max_length=2, unique=True, verbose_name="Código")
    nombre = models.CharField(max_length=70, verbose_name="Nombre")


class Provincia(models.Model):
    codigo = models.CharField(max_length=4, verbose_name="Código", unique=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=50)


class Ubigeo(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=6)
    nombre = models.CharField(verbose_name="Ubigeo", max_length=50)
    provincia = models.ForeignKey(Provincia, verbose_name="Provincia", on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, verbose_name="Departamento", on_delete=models.CASCADE)