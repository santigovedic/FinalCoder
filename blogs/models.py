from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Articulo(models.Model):  # Este modelo muestra cada receta de cada bebida en particular.

    fecha = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes", null=True)

    def __str__(self):
        return f"Titulo: {self.titulo}, detalle: {self.subtitulo}"


class Comentario(models.Model):  # Este modelo almacena los comentarios que se hacen a cada artículo en particular.
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=20, null=True)
    comentar = models.TextField()
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True, related_name="comentarios")


class RespCom(models.Model):  # Este modelo almacena las respuestas a c/ comentario en particular.

    fecha = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    responder = models.TextField()
    respuesta = models.ForeignKey(Comentario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.autor} responde: {self.responder}"

