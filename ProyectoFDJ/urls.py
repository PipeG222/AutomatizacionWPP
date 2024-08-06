from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('login.urls')),
    path('barberia/', include('agenda.urls')),
    path('admin/', admin.site.urls),
]
