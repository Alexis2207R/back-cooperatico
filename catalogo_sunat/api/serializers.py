from rest_framework import serializers
from catalogo_sunat.models import *


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'
    
    def __str__(self):
        return self.nombre


class TipoComprobanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoComprobante
        fields = '__all__'
    
    def __str__(self):
        return self.nombre


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

    def __str__(self):
        return self.nombre


class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = '__all__'
    
    def __str__(self):
        return self.nombre


class MotivoTrasladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivoTraslado
        fields = '__all__'

    def __str__(self):
        return self.nombre


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

    def __str__(self):
        return self.nombre


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'
        
    def __str__(self):
        return self.nombre


class UbigeoSerializer(serializers.ModelSerializer):
    provincia_txt = serializers.CharField(source='provincia.nombre', read_only=True)
    class Meta:
        model = Ubigeo
        fields = '__all__'

    def __str__(self):
        return self.nombre