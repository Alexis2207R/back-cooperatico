from rest_framework import serializers
from clientes.models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __str__(self):
        return self.nombre