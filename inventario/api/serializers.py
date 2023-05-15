from rest_framework import serializers
from inventario.models import *


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
        # Campos que no quiero que aparescan
        # read_only_fields = ('nombre',)
    
    def __str__(self):
        return self.nombre

    
class CategoriaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaItem
        fields = '__all__'
    
    def __str__(self):
        return self.nombre

    
class TipoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoItem
        fields = '__all__'
    
    def __str__(self):
        return self.nombre

    
class TipoAfectacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAfectacion
        fields = '__all__'

    def __str__(self):
        return self.nombre

    
class CodigoSunatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoSunat
        fields = '__all__'

    def __str__(self):
        return self.nombre