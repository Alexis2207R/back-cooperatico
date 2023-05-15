from rest_framework import serializers
from envios.models import *


class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = '__all__'


class VehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = '__all__'


class TransportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportista
        fields = '__all__'


class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = '__all__'


class GuiaRemitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaRemitente
        fields = '__all__'


class DestinatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinatario
        fields = '__all__'


class GuiaTransportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaTransportista
        fields = '__all__'


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'