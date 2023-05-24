from django.db import models


class Serie(models.Model):
    nombre = models.CharField(max_length=4, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.nombre


class TipoComprobante(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    serie = models.ForeignKey(Serie, verbose_name="Serie", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class TipoDocumento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=2, unique=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.nombre

class Moneda(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    
    def __str__(self):
        return self.nombre
    

class MotivoTraslado(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Motivo de Traslado")

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    codigo = models.CharField(max_length=2, unique=True, verbose_name="Código")
    nombre = models.CharField(max_length=70, verbose_name="Nombre")

    def __str__(self):
        return self.nombre
    


class Provincia(models.Model):
    codigo = models.CharField(max_length=4, verbose_name="Código", unique=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=50)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

    def __str__(self):
        return self.nombre
    

class Ubigeo(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=6)
    nombre = models.CharField(verbose_name="Ubigeo", max_length=150)
    provincia = models.ForeignKey(Provincia, verbose_name="Provincia", on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, verbose_name="Departamento", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class TipoOperacion(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código")
    nombre = models.CharField(verbose_name="Nombre", max_length=100)