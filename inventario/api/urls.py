from django.urls import include, path
from rest_framework import routers
from inventario.api.viewsets import *

router_inventario = routers.DefaultRouter()

router_inventario.register(r'items', ItemsViewSet)
router_inventario.register(r'categoria', CategoriaItemViewSet)
router_inventario.register(r'tipo', TipoItemViewSet)
router_inventario.register(r'tipo-afectacion', TipoAfectacionViewSet)
router_inventario.register(r'codigo-sunat', CodigoSunatViewSet)

urlpatterns = router_inventario.urls