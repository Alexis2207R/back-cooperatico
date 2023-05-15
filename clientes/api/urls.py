from django.urls import include, path
from rest_framework import routers
from clientes.api.viewsets import *

router_clientes = routers.DefaultRouter()

router_clientes.register(r'', ClienteViewSet)

urlpatterns = router_clientes.urls