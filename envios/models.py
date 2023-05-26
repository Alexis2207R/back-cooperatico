from django.db import models
from clientes.models import Cliente
from inventario.models import Items
from catalogo_sunat.models import Ubigeo, MotivoTraslado, TipoComprobante, TipoDocumento
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinValueValidator


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
    numero_documento = models.CharField(max_length=11, verbose_name="Numero del Documento", unique=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")

    def create_conductor(request):
    # Lógica para crear el conductor y validar el campo numero_documento
        try:
            # Tu lógica de validación aquí
            
            # Si el campo numero_documento ya está registrado
            return JsonResponse({'error': 'El número de documento ya está registrado'}, status=400)
            
            # Si no hay errores de validación
            return JsonResponse({'success': 'El conductor se registró correctamente'})
    
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def __str__(self):
        return self.nombre


class Yaer(models.Model):
    year = models.PositiveIntegerField(validators=[MaxLengthValidator(2030), MinValueValidator(2000)],verbose_name="Año",unique=True,)


class Mes(models.Model):
    mes = models.PositiveIntegerField(verbose_name="Año", unique=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre", unique=True)


class Dia(models.Model):
    dia = models.PositiveIntegerField(verbose_name="Año", unique=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre", unique=True)


class Destinatario(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, verbose_name="Tipo de Documento", on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=15, verbose_name="Número Documento")
    nombre = models.CharField(verbose_name="Nombre Completo", max_length=100)

    def create_conductor(request):
    # Lógica para crear el conductor y validar el campo numero_documento
        try:
            # Tu lógica de validación aquí
            
            # Si el campo numero_documento ya está registrado
            return JsonResponse({'error': 'El número de documento ya está registrado'}, status=400)
            
            # Si no hay errores de validación
            return JsonResponse({'success': 'El conductor se registró correctamente'})
    
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

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
    tipo_comprobante = models.ForeignKey(TipoComprobante, verbose_name="Tipo de Comprobante", on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Destinatario, verbose_name="Destinatario / Cliente", on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE, null=True) # Borrar el null
    fecha_emision = models.DateField(auto_now_add=True, verbose_name="Fecha de emisión")
    # Se puede llamar a la fecha de la siguiente la manera:
    # <p>Fecha: #{{ mi_modelo.get_fecha_formateada }}</p>
    peso_bruto_total = models.DecimalField(max_digits=22, decimal_places=10, verbose_name="Peso Bruto Total")
    peso_bruto_unidad_medida = models.CharField(max_length=3, verbose_name="Unidad de medida", choices=UNIDAD_MEDIDA)
    fecha_inicio_traslado = models.DateField(auto_now_add=True, verbose_name="Fecha de emisión")
    placa = models.ForeignKey(Vehiculos, verbose_name="Placa del vehiculo del transportista", on_delete=models.CASCADE)
    punto_partida = models.ForeignKey(Ubigeo, verbose_name="Punto de Partida (Ubigeo)", on_delete=models.CASCADE, related_name='partida_remitente')
    punto_partida_direccion = models.CharField(verbose_name="Punto de Partida (Dirección)", max_length=150)
    codigo_partida_establecimiento_sunat = models.CharField(verbose_name="Establecimiento Sunat", max_length=4)
    punto_llegada = models.ForeignKey(Ubigeo, verbose_name="Punto de Llegada (Ubigeo)", on_delete=models.CASCADE, related_name='llegada_remitente')
    punto_llegada_direccion = models.CharField(verbose_name="Punto de Llegada (Dirección)", max_length=150)
    codigo_llegada_establecimiento_sunat = models.CharField(verbose_name="Establecimiento Sunat", max_length=4)
    observaciones = models.TextField(verbose_name="Observaciones", blank=True)
    enviar_cliente = models.BooleanField(verbose_name="Enviar automaticamente al cliente", max_length=5)
    formato_pdf = models.CharField(verbose_name="Formato", max_length=5, )

    items = models.ManyToManyField(Items, through="GuiaItems")

    def validar_peso_bruto_total(self):
        if self.peso_bruto_total <= 0:
            raise ValidationError("El peso bruto total debe ser mayor que cero.")

    def fecha_emision(self):
        return str(self.fecha_emision.strftime("%d-%m-%Y"))

    def fecha_inicio_traslado(self):
        return self.fecha_inicio_traslado.strftime("%d-%m-%Y")

    def __unicode__(self):
        return self.tipo_comprobante


class GuiaItems(models.Model):
    guia = models.ForeignKey(Guia, on_delete=models.CASCADE) 
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    cantidad_item = models.PositiveIntegerField(verbose_name="Cantidad")
    
    def __unicode__(self):
        return self.guia

    # Usar los signals para disminuir un un almacen y aumentar en otro


class Conductor(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, verbose_name="Tipo de Documento", on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=15, verbose_name="Numero del Documento", unique=True)
    denominacion = models.CharField(verbose_name="Razon o Nombre Completo (Conductor)", max_length=100)
    nombre = models.CharField(max_length=250, verbose_name="Nombre")
    apellidos = models.CharField(max_length=250, verbose_name="Apellidos")
    licencia = models.CharField(max_length=10, verbose_name="Licencia")

    def create_conductor(request):
    # Lógica para crear el conductor y validar el campo numero_documento
        try:
            # Tu lógica de validación aquí
            
            # Si el campo numero_documento ya está registrado
            return JsonResponse({'error': 'El número de documento ya está registrado'}, status=400)
            
            # Si no hay errores de validación
            return JsonResponse({'success': 'El conductor se registró correctamente'})
    
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def __str__(self):
        return self.nombre


class GuiaRemitente(models.Model):
    TIPO_TRANSPORTE = (
        ("01", "TRANSPORTE PÚBLICO"),
        ("02", "TRANSPORTE PRIVADO"),
    )
    numero = models.CharField(max_length=10, verbose_name="N°", null=True) # Quitar null
    guia = models.ForeignKey(Guia, verbose_name="Datos Generales de la Guia", on_delete=models.CASCADE)
    tipo_de_transporte = models.CharField(max_length=2, choices=TIPO_TRANSPORTE)
    motivo_traslado = models.ForeignKey(MotivoTraslado, on_delete=models.CASCADE, verbose_name="Motivo de Traslado")
    motivo_traslado_otro = models.CharField(max_length=70, verbose_name="Otro Motivo de Traslado", blank=True)
    numero_de_bultos = models.PositiveIntegerField(validators=[MaxLengthValidator(999999), MinValueValidator(0)], verbose_name="Número de bultos",)
    transportista = models.ForeignKey(Transportista, verbose_name="Tansportista", on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, verbose_name="Conductor", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.numero


class GuiaTransportista(models.Model):
    numero = models.CharField(max_length=10, verbose_name="N°", null=True) # Quitar null
    vehiculo_principal = models.CharField(max_length=15, verbose_name="TUC Vehículo principal", null=True, blank=True)
    conductor = models.ForeignKey(Conductor, verbose_name="Conductor", on_delete=models.CASCADE, null=True) # Borrar el null

    def __str__(self):
        return self.vehiculo_principal