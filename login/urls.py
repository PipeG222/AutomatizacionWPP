from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home , name="home"),
    path('products', views.products , name="products"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register_view, name="register"),
    
]