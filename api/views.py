# api/views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

# Vista para registrar nuevos usuarios
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

# Vista para obtener el token de acceso y actualización
class CustomTokenObtainPairView(TokenObtainPairView):
    # Puedes personalizar la vista si es necesario
    pass

# Vista protegida que requiere autenticación
class SomeProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Ya funciona tu mierda"})