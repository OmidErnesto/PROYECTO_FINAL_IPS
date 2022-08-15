from datetime import MAXYEAR, MINYEAR
from typing import AbstractSet
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import  timezone
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from AppZonaTurismo.settings import MEDIA_URL, STATIC_URL
# Create your models here.

class Distrito(models.Model):
    nombre_distrito = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre_distrito

class Estructura(models.Model):
    nombre_estructura = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre_estructura
        
class ZonaTuristica(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)
    descripcion = models.TextField()
    distrito = models.ForeignKey(Distrito, on_delete=CASCADE)
    estructura = models.ForeignKey(Estructura, on_delete=CASCADE)
    horario = models.TimeField()
    year = models.IntegerField( blank=True,validators=[MinValueValidator(1895), MaxValueValidator(2022)])
    disponible = models.BooleanField(default=False)   
    img = models.ImageField(upload_to='pics', blank=True)

    def get_absolute_url (self):
        return reverse('AppTurismo:zona-detail', kwargs={'pk': self.nombre})

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)

class UsuarioCliente (AbstractUser):
    image = models.ImageField(upload_to='users', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self):
        texto = "{0}"
        return texto.format(self.username)
