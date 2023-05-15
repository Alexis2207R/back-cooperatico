from django.db import models
from catalogo_sunat.models import TipoDocumento


class Cliente(models.Model):
    tipo_documento_cliente = models.ForeignKey(TipoDocumento, verbose_name="Tipo de Documento", on_delete=models.CASCADE)
    numero_de_documento = models.CharField(max_length=15, verbose_name="Número de Documento")
    nombre = models.CharField(max_length=100, verbose_name="Titulo")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    email = models.EmailField(max_length=250, verbose_name="Email", blank=True)
    email_1 = models.EmailField(max_length=250, verbose_name="Email 2", blank=True)
    email_2 = models.EmailField(max_length=250, verbose_name="Email 3", blank=True)

    def __str__(self):
        return self.nombre