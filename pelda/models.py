from django.db import models

# Create your models here.
class Termek(models.Model):
    azonosito = models.CharField(max_length=20, unique=True)
    nev = models.CharField(max_length=50)
    leiras = models.TextField()
    ar = models.DecimalField(max_digits=6, decimal_places=2)
    raktaron = models.BooleanField(default=False)
    letrehozva = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nev
        
    