from rest_framework import viewsets, permissions
from inventario.models import *
from .serializers import *


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemsSerializer


class CategoriaItemViewSet(viewsets.ModelViewSet):
    queryset = CategoriaItem.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaItemSerializer


class TipoItemViewSet(viewsets.ModelViewSet):
    queryset = TipoItem.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoItemSerializer


class TipoAfectacionViewSet(viewsets.ModelViewSet):
    queryset = TipoAfectacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoAfectacionSerializer


class CodigoSunatViewSet(viewsets.ModelViewSet):
    queryset = CodigoSunat.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CodigoSunatSerializer
