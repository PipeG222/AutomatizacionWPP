from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda , name="homeAgenda"),
    path('products/', views.products , name="products"),
    
]