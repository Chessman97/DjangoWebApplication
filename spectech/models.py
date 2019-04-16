from django.db import models

# Create your models here.
class Tech(models.Model):
    name = models.CharField(max_length=130)
    modell = models.CharField(max_length=100)
    marka = models.CharField(max_length=130)
    gruz = models.CharField(max_length=130)
    massa = models.CharField(max_length=130)
    dvig = models.CharField(max_length=130)
    cost = models.CharField(max_length=130)

class Technic(models.Model):
    name = models.CharField(max_length=130)
    modell = models.CharField(max_length=100)
    marka = models.CharField(max_length=130)
    gruz = models.CharField(max_length=130)
    massa = models.CharField(max_length=130)
    dvig = models.CharField(max_length=130)
    cost = models.CharField(max_length=130)

def __str__(self):
    return self.name