from django.contrib import admin
from .models import Conductor, Cliente, TipoVehiculo, Vehiculos, Transportista, Guia


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(Cliente, ClienteAdmin) 


class VehiculosAdmin(admin.ModelAdmin):
    list_display = ('placa',) 
    search_fields = ('placa',)

admin.site.register(Vehiculos, VehiculosAdmin) 


class TipoVehiculoAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(TipoVehiculo, TipoVehiculoAdmin)


class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(Conductor, ConductorAdmin)


class TransportistaAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(Transportista, TransportistaAdmin)


class GuiaAdmin(admin.ModelAdmin):
    list_display = ('tipo_comprobante',) 
    search_fields = ('fecha_emision', 'destinatario', 'placa',)

admin.site.register(Guia, GuiaAdmin)