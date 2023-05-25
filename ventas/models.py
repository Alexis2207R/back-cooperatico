# from django.db import models
# from clientes.models import Cliente
# from inventario.models import Items
# from catalogo_sunat.models import TipoComprobante, Moneda


# ############### FACTURAS ###########

# class TipoOperacion(models.Model):
#     codigo = models.CharField(max_length=6, verbose_name="Código")
#     nombre = models.CharField(verbose_name="Nombre", max_length=100)


# class TipoPercepcion(models.Model):
#     nombre = models.CharField(max_length=50, verbose_name="Tipo de percepcion")
#     tasa = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Tipo de Documento")


# class Factura(models.Model):
#     IGV = (
#         (18, "ESTANDAR"),
#         (10, "LEY 31556"),
#         (4, "IVAP"),
#     )
#     TIPO_RETENCION = (
#         (1, "Tasa 3%"),
#         (2, "Tasa 6%"),
#     )
#     operacion = models.CharField(max_length=50, verbose_name="Operación", default="generar_comprobante")
#     cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
#     tipo_comprobante = models.ForeignKey(TipoComprobante, verbose_name="Tipo de Comprobante", on_delete=models.CASCADE)
#     igv = models.DecimalField(choices=IGV, verbose_name="IGV", max_digits=4, decimal_places=2)
#     sunat_transaction = models.ForeignKey(TipoOperacion, verbose_name="Tipo Operación", on_delete=models.CASCADE)
#     moneda = models.ForeignKey(Moneda, verbose_name="Moneda", on_delete=models.CASCADE)
#     tipo_cambio = models.CharField(verbose_name="Tipo de cambio", max_length=200, blank=True)
#     fecha_emision = models.DateField(auto_now_add=True, verbose_name="Fecha de emisión")
#     fecha_vencimiento = models.DateField(auto_now_add=True, verbose_name="Fecha de Vencimiento", blank=True)
#     porcentaje_descuento = models.DecimalField(verbose_name="Porcentaje de descuento", max_digits=4, decimal_places=2, blank=True)
#     total_descuento = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Descuento Total (-)", blank=True) 
#     total_anticipo = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Anticipo (-)", blank=True)
#     total_inafecta = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Inafecta", blank=True)
#     total_gravado = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Gravada")
#     total_exonerada = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Exonerada")
#     total_igv = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="IGV")
#     total_gratuita = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Gratuita")
#     total_otros_cargos = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Otros Cargos")
#     total_isc = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="ICBPERS")
#     total = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Total")
#     estado_pago = models.BooleanField(verbose_name="¿Pagado?")
#     tipo_percepcion = models.ForeignKey(TipoPercepcion, verbose_name="", on_delete=models.CASCADE)
#     percepcion_base_imponible = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Percepción Base Imponible")
#     total_percepcion = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Total Percepcion")
#     total_incluido_percepcion = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Total Percepción Incluido")
#     tipo_retencion = models.IntegerField(verbose_name="Tipo Retención", choices=TIPO_RETENCION)
#     retencion_base_imponible = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Percepción Base Imponible")
#     total_retencion = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Total Retención")
#     total_impuestos_bolsas = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Total Impuestos Bolsas")
#     # observaciones = 
#     # documento = 
#     items = models.ManyToManyField(Items, verbose_name="Items", through="FacturaItems")

#     def __str__(self):
#         return str(self.fecha_emision.strftime("%d-%m-%Y"))


# class FacturaItems(models.Model):
#     factura = models.ForeignKey(Factura, on_delete=models.CASCADE) 
#     item = models.ForeignKey(Items, on_delete=models.CASCADE) # borrar el null
#     cantidad_item = models.PositiveIntegerField(verbose_name="Cantidad")
    
#     def __unicode__(self):
#         return self.factura