from django.urls import path
from . import views

urlpatterns = [
    path('', views.superadmin , name="superadmin"),
]