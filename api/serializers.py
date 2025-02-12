from rest_framework import serializers
from .models import Categoria, Pregunta, Respuesta

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ['id', 'texto', 'es_correcta']

class PreguntaSerializer(serializers.ModelSerializer):
    respuestas = RespuestaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pregunta
        fields = ['id', 'texto', 'dificultad', 'puntos', 'respuestas']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']