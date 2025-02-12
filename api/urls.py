# api/urls.py

from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, SomeProtectedView  # Asegúrate de importar tu vista protegida

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('protected/', SomeProtectedView.as_view(), name='protected'),  # Asegúrate de tener un endpoint protegido
]