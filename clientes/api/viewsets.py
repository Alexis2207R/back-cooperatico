from rest_framework import viewsets, permissions
from clientes.models import *
from .serializers import *


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer