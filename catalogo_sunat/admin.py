from django.contrib import admin
from .models import Serie, TipoComprobante, TipoDocumento, MotivoTraslado, Departamento, Provincia, Ubigeo


class SerieAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(Serie, SerieAdmin) 


class TipoComprobanteAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(TipoComprobante, TipoComprobanteAdmin) 


class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(TipoDocumento, TipoDocumentoAdmin)


class MotivoTrasladoAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(MotivoTraslado, MotivoTrasladoAdmin) 


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(Departamento, DepartamentoAdmin)


class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(Provincia, ProvinciaAdmin)


class UbigeoAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    search_fields = ('nombre',)

admin.site.register(Ubigeo, UbigeoAdmin)