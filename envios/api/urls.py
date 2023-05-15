from django.urls import include, path
from rest_framework import routers
from envios.api.viewsets import *

router_envios = routers.DefaultRouter()

router_envios.register(r'tipo-vehiculo', TipoVehiculoViewSet)
router_envios.register(r'vehiculo', VehiculosViewSet)
router_envios.register(r'transportista', TransportistaViewSet)
router_envios.register(r'guia', GuiaViewSet)
router_envios.register(r'guia-remitente', GuiaRemitenteViewSet)
router_envios.register(r'destinatario', DestinatarioViewSet)
router_envios.register(r'guia-transportista', GuiaTransportistaViewSet)
router_envios.register(r'conductor', ConductorViewSet)

urlpatterns = router_envios.urls