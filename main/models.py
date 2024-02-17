from django.db import models
from django.utils import timezone

# Create your models here.

class Autor(models.Model):
    ime = models.CharField(max_length=25)
    prezime = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.ime} {self.prezime}"
    
class Kategorija(models.Model):
    naziv_kategorije = models.CharField(max_length=100)
    opis_kategorije = models.TextField()

    def __str__(self):
        return self.naziv_kategorije

class Recept(models.Model):
    naziv = models.CharField(max_length=100)
    tezina_izrade = models.CharField(max_length=20)
    vrijeme_izrade = models.TimeField()
    opis = models.TextField()
    vrijeme_objave = models.DateTimeField(default=timezone.now)
    autor_recepta = models.ForeignKey(Autor, on_delete=models.CASCADE)
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv
    
class Savjeti(models.Model):
    naslov = models.CharField(max_length=25)
    tekst_savjeta = models.TextField()
    autori = models.ManyToManyField(Autor) 
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)

    def __str__(self):
        return self.naslov