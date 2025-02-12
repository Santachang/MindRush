# MindRush/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración de Django
    path('api/', include('api.urls')),  # Incluye las URLs de la aplicación api
]