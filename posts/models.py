from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField(default = "")
    descripcion = models.TextField(default = "")
    infromacion = models.TextField(default = "")
    def __str__(self):
        return self.text[:500]


class Informacion(models.Model):
    text = models.TextField(default = "")
    descripcion = models.TextField(default = "")
    infromacion = models.TextField(default = "")
    def __str__(self):
        return self.text[:500]

class Informacion2(models.Model):
    text = models.TextField(default = "")
    descripcion = models.TextField(default = "")
    infromacion = models.TextField(default = "")
    def __str__(self):
        return self.text[:500]

class Informacion3(models.Model):
    text = models.TextField(default = "")
    descripcion = models.TextField(default = "")
    infromacion = models.TextField(default = "")
    def __str__(self):
        return self.text[:500]
class Informacion4(models.Model):
    text = models.TextField(default = "")
    descripcion = models.TextField(default = "")
    infromacion = models.TextField(default = "")
    def __str__(self):
        return self.text[:500]

   

