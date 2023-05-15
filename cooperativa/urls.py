from django.contrib import admin
from django.urls import path, include

from inventario.api.urls import router_inventario
from envios.api.urls import router_envios

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/inventario/', include('inventario.api.urls')),
    path('api/envios/', include('envios.api.urls')),
    path('api/clientes/', include('clientes.api.urls')),
    path('api/catalogo_sunat/', include('catalogo_sunat.api.urls')),
]
