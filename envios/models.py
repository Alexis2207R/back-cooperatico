from django.db import models
from clientes.models import Cliente
from inventario.models import Items
from catalogo_sunat.models import Ubigeo, MotivoTraslado, TipoComprobante, TipoDocumento
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Tipo de Vehiculo")

    def __str__(self):
        return self.nombre


######### Los vehiculos son de los transportistas #########
class Vehiculos(models.Model):
    # Para mostrar el error al intentar registrar una placa existente se usa:
    # try:
    #     vehiculo = Vehiculo.objects.create(placa='ABC123')
    # except IntegrityError:
    #     print("Ya existe un vehículo con la placa ABC123")
    placa = models.CharField(max_length=6, unique=True, verbose_name="Placa")
    tipo = models.ForeignKey(TipoVehiculo, verbose_name="Tipo de Vehiculo", on_delete=models.CASCADE)
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    year = models.CharField(max_length=4, verbose_name="Año")
    color = models.CharField(max_length=100, verbose_name="Color")

    def __str__(self):
        return self.placa


class Transportista(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, verbose_name="Tipo de Documento", on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=11, verbose_name="Numero del Documento")
    nombre = models.CharField(max_length=200, verbose_name="Nombre")

    def __str__(self):
        return self.nombre


class Yaer(models.Model):
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2030), MinValueValidator(2000)],verbose_name="Año",unique=True,)


class Mes(models.Model):
    mes = models.PositiveIntegerField(verbose_name="Año", unique=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre", unique=True)


class Dia(models.Model):
    dia = models.PositiveIntegerField(verbose_name="Año", unique=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre", unique=True)


class Destinatario(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, verbose_name="Tipo de Documento", on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=50, verbose_name="Número Documento")
    nombre = models.CharField(verbose_name="Nombre Completo", max_length=100)

    def __str__(self):
        return self.nombre


class Guia(models.Model):
    FORMATO = (
        ("A4", "Hoja A4"),
        ("TICKET", "TICKET"),
    )
    UNIDAD_MEDIDA = (
        ("KGM", "Kilogramos"),
        ("TNE", "Toneladas"),
    )
    
    operacion = models.CharField(default="generar_guia", verbose_name="Operación", max_length=12)
    tipo_comprobante = models.ForeignKey(TipoComprobante,on_delete=models.CASCADE,verbose_name="Tipo de Comprobante")
    destinatario = models.ForeignKey(Destinatario, verbose_name="Destinatario / Cliente", on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True, verbose_name="Fecha de emisión")
    # Se puede llamar a la fecha de la siguiente la manera:
    # <p>Fecha: #{{ mi_modelo.get_fecha_formateada }}</p>
    items = models.ManyToManyField(Items, through="GuiaItems")
    peso_bruto_total = models.DecimalField(max_digits=22, decimal_places=10, verbose_name="Peso Bruto Total")
    peso_bruto_unidad_medida = models.CharField(max_length=3, verbose_name="Unidad de medida", choices=UNIDAD_MEDIDA)
    fecha_inicio_traslado = models.DateField(auto_now_add=True, verbose_name="Fecha de emisión")
    placa = models.ForeignKey(Vehiculos, verbose_name="Placa del vehiculo del transportista", on_delete=models.CASCADE)
    punto_partida = models.ForeignKey(Ubigeo, verbose_name="Punto de Partida (Ubigeo)", on_delete=models.CASCADE, max_length=6, related_name='partida_remitente')
    punto_partida_direccion = models.CharField(verbose_name="Punto de Partida (Dirección)", max_length=150)
    codigo_partida_establecimiento_sunat = models.CharField(verbose_name="Establecimiento Sunat", max_length=4)
    punto_llegada = models.ForeignKey(Ubigeo, verbose_name="Punto de Llegada (Ubigeo)", on_delete=models.CASCADE, max_length=6, related_name='llegada_remitente')
    punto_llegada_direccion = models.CharField(verbose_name="Punto de Llegada (Dirección)", max_length=150)
    codigo_llegada_establecimiento_sunat = models.CharField(verbose_name="Establecimiento Sunat", max_length=4)
    observaciones = models.TextField(verbose_name="Observaciones", blank=True)
    enviar_cliente = models.BooleanField(verbose_name="Enviar automaticamente al cliente", max_length=5)
    formato_pdf = models.CharField(verbose_name="Formato", max_length=5, )

    def validar_peso_bruto_total(self):
        if self.peso_bruto_total <= 0:
            raise ValidationError("El peso bruto total debe ser mayor que cero.")

    def __str__(self):
        return str(self.fecha_emision.strftime("%d-%m-%Y"))

    def fecha_inicio_traslado(self):
        return self.fecha_inicio_traslado.strftime("%d-%m-%Y")

    def __str__(self):
        return self.tipo_comprobante


class GuiaItems(models.Model):
    guia = models.ForeignKey(Guia, on_delete=models.CASCADE) 
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    cantidad_item = models.PositiveIntegerField(verbose_name="Cantidad")
    
    def __unicode__(self):
        return self.guia

    # Usar los signals para disminuir un un almacen y aumentar en otro


class GuiaRemitente(models.Model):
    TIPO_TRANSPORTE = (
        ("01", "TRANSPORTE PÚBLICO"),
        ("02", "TRANSPORTE PRIVADO"),
    )
    guia = models.ForeignKey(Guia, verbose_name="Datos Generales de la Guia", on_delete=models.CASCADE)
    tipo_de_transporte = models.CharField(max_length=2, choices=TIPO_TRANSPORTE)
    motivo_traslado = models.ForeignKey(MotivoTraslado, on_delete=models.CASCADE, verbose_name="Motivo de Traslado")
    motivo_traslado_otro = models.CharField(max_length=70, verbose_name="Otro Motivo de Traslado", blank=True)
    numero_de_bultos = models.PositiveIntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)], verbose_name="Número de bultos",)
    transportista = models.ForeignKey(Transportista, verbose_name="Tansportista", on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_de_transporte


class GuiaTransportista(models.Model):
    vehiculo_principal = models.CharField(max_length=50, verbose_name="TUC Vehículo principal", blank=True)

    def __str__(self):
        return self.vehiculo_principal


class Conductor(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, verbose_name="Tipo de Documento", on_delete=models.CASCADE)
    guia = models.ForeignKey(Guia, on_delete=models.CASCADE, verbose_name="Guia")
    numero_documento = models.CharField(max_length=20, verbose_name="Numero del Documento")
    denominacion = models.CharField(verbose_name="Razon o Nombre Completo (Conductor)", max_length=250)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    licencia = models.CharField(max_length=200, verbose_name="Licencia")

    def __str__(self):
        return self.denominacion