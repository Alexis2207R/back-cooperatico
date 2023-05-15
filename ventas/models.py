from django.db import models
from clientes.models import Cliente
from inventario.models import Items
from catalogo_sunat.models import TipoComprobante, Moneda


############### FACTURAS ###########

class TipoOperacion(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código")
    nombre = models.CharField(verbose_name="Nombre", max_length=100)

class Factura(models.Model):
    IGV = (
        (18, "ESTANDAR"),
        (10, "LEY 31556"),
        (4, "IVAP"),
    )
    clientes = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
    tipo_documento = models.ForeignKey(TipoComprobante, verbose_name="Tipo de Comprobante", on_delete=models.CASCADE)
    igv = models.IntegerField(choices=IGV, verbose_name="IGV")
    tipo_operacion = models.ForeignKey(TipoOperacion, verbose_name="Tipo Operación", on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, verbose_name="Moneda", on_delete=models.CASCADE)
    tipo_cambio = models.CharField(verbose_name="Tipo de cambio", max_length=200)
    fecha_emision = models.DateField(auto_now_add=True, verbose_name="Fecha de emisión")
    fecha_vencimiento = models.DateField(auto_now_add=True, verbose_name="Fecha de Vencimiento")
    estado_pago = models.BooleanField(verbose_name="¿Pagado?")
    items = models.ManyToManyField(Items, verbose_name="Items", through="FacturaItems")


class FacturaItems(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE) 
    item = models.ForeignKey(Items, on_delete=models.CASCADE) # borrar el null
    cantidad_item = models.PositiveIntegerField(verbose_name="Cantidad")
    
    def __unicode__(self):
        return self.factura