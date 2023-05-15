from rest_framework import serializers
from catalogo_sunat.models import *


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'


class TipoComprobanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoComprobante
        fields = '__all__'


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'


class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = '__all__'


class MotivoTrasladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivoTraslado
        fields = '__all__'


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'


class UbigeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubigeo
        fields = '__all__'