from rest_framework import viewsets, permissions
from rest_framework.response import Response
from catalogo_sunat.models import *
from .serializers import *


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SerieSerializer


class TipoComprobanteViewSet(viewsets.ModelViewSet):
    queryset = TipoComprobante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoComprobanteSerializer


class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoDocumentoSerializer


class MonedaViewSet(viewsets.ModelViewSet):
    queryset = Moneda.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MonedaSerializer


class MotivoTrasladoViewSet(viewsets.ModelViewSet):
    queryset = MotivoTraslado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MotivoTrasladoSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartamentoSerializer


class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProvinciaSerializer


class UbigeoViewSet(viewsets.ModelViewSet):
    queryset = Ubigeo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UbigeoSerializer
    
    # def list(self, request):
    #     return Response(self.serializer_class(self.queryset, write_only=False).data)