from django.db import models


# Create your models here.

class Store(models.Model):
    immagine = models.ImageField()
    titolo = models.CharField(max_length=100)
    artista = models.CharField(max_length=30)
    prezzo = models.FloatField()

    def __str__(self):
        return self.titolo
