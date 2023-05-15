from rest_framework import viewsets, permissions
from envios.models import *
from .serializers import *


class TipoVehiculoViewSet(viewsets.ModelViewSet):
    queryset = TipoVehiculo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoVehiculoSerializer


class VehiculosViewSet(viewsets.ModelViewSet):
    queryset = Vehiculos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VehiculosSerializer


class TransportistaViewSet(viewsets.ModelViewSet):
    queryset = Transportista.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransportistaSerializer


class GuiaViewSet(viewsets.ModelViewSet):
    queryset = Guia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GuiaSerializer


class GuiaRemitenteViewSet(viewsets.ModelViewSet):
    queryset = GuiaRemitente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GuiaRemitenteSerializer


class DestinatarioViewSet(viewsets.ModelViewSet):
    queryset = Destinatario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DestinatarioSerializer


class GuiaTransportistaViewSet(viewsets.ModelViewSet):
    queryset = GuiaTransportista.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GuiaTransportistaSerializer


class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConductorSerializer