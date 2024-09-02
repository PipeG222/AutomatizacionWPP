from django.urls import path
from . import views

urlpatterns = [
    path('', views.superadmin , name="superadmin"), 
    path('empresas_superadmin/', views.empresas_superadmin , name="empresas_superadmin"),
    path('negocios_superadmin/', views.negocios_superadmin , name="negocios_superadmin"),
    path('servicios_superadmin/', views.servicios_superadmin , name="servicios_superadmin"),
    path('usuarios_superadmin/', views.usuarios_superadmin , name="usuarios_superadmin"),
    path('clientes_superadmin/', views.clientes_superadmin , name="clientes_superadmin"),
    path('citas_superadmin/', views.citas_superadmin , name="citas_superadmin"),
    path('notificaciones_superadmin/', views.notificaciones_superadmin , name="notificaciones_superadmin"),
]