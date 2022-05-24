from django.db import models

# Create your models here.

class MyBase(models.Model):
    name = models.CharField(max_length=20)
    barcha = models.IntegerField()
    ish_jarayonida = models.IntegerField()
    bajarildi = models.IntegerField()
    muddati_otgan = models.IntegerField()
    muddati_otin_ijro_etilgan = models.IntegerField()

    def __str__(self):
        return f"{self.name}"