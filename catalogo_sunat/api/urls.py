from django.urls import include, path
from rest_framework import routers
from catalogo_sunat.api.viewsets import *

router_catalogo_sunat = routers.DefaultRouter()

router_catalogo_sunat.register(r'serie', SerieViewSet)
router_catalogo_sunat.register(r'tipo-comprobante', TipoComprobanteViewSet)
router_catalogo_sunat.register(r'tipo-documento', TipoDocumentoViewSet)
router_catalogo_sunat.register(r'moneda', MonedaViewSet)
router_catalogo_sunat.register(r'motivo-traslado', MotivoTrasladoViewSet)
router_catalogo_sunat.register(r'departamentos', DepartamentoViewSet)
router_catalogo_sunat.register(r'provincias', ProvinciaViewSet)
router_catalogo_sunat.register(r'ubigeo', UbigeoViewSet)

urlpatterns = router_catalogo_sunat.urls