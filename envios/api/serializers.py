from rest_framework import serializers
from envios.models import *


class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = '__all__'
    
    def __str__(self):
        return self.nombre


class VehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = '__all__'

    def __str__(self):
        return self.placa


class TransportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportista
        fields = '__all__'
    
    def __str__(self):
        return self.nombre


class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = '__all__'

    def __str__(self):
        return self.id


class GuiaRemitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaRemitente
        fields = '__all__'
    
    def __str__(self):
        return self.numero


class DestinatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinatario
        fields = '__all__'
    
    def __str__(self):
        return self.nombre


class GuiaTransportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaTransportista
        fields = '__all__'
    
    def __str__(self):
        return self.numero


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'
    
    def __str__(self):
        return self.denominacion