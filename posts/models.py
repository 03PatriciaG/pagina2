from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField(default = "")
    descripcion = models.TextField(default = "")
    def __str__(self):
        return self.text[:100]

