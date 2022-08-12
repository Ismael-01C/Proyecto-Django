from django.db import models

# Create your models here.
class Producto(models.Model):
    Titulo = models.CharField(max_length=100)
    Contenido = models.TextField()
    Imagen = models.ImageField(upload_to="projects")
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechamodificacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Titulo

class Contactanos(models.Model):
    Titulo = models.CharField(max_length=100)
    Contenido = models.TextField()
    Imagen = models.ImageField(upload_to="projects")
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechamodificacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Titulo