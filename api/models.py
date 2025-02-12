from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    texto = models.TextField()
    dificultad = models.IntegerField(choices=[(1, 'Fácil'), (2, 'Medio'), (3, 'Difícil')])
    puntos = models.IntegerField()
    
    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas', on_delete=models.CASCADE)
    texto = models.TextField()
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto