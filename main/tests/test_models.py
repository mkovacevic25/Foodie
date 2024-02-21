from django.test import TestCase
from main.models import Autor, Kategorija, Recept, Savjeti, NutritivneInformacije
from django.utils import timezone

class ModelsTestCase(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(ime="Test", prezime="Autor")
        self.kategorija = Kategorija.objects.create(naziv_kategorije="Test Kategorija", opis_kategorije="Opis test kategorije")
        self.recept = Recept.objects.create(naziv="Test Recept", tezina_izrade="Lagano", vrijeme_izrade="00:30:00", opis="Opis test recepta", autor_recepta=self.autor, kategorija=self.kategorija)
        self.savjet = Savjeti.objects.create(naslov="Test Savjet", tekst_savjeta="Tekst test savjeta", recept=self.recept)
        self.nutritivne_informacije = NutritivneInformacije.objects.create(recept=self.recept, kalorije=100, proteini=10.5, ugljikohidrati=20.3, masti=5.2)

    def test_autor_str(self):
        autor = Autor.objects.get(ime="Test")
        self.assertEqual(str(autor), "Test Autor")

    def test_kategorija_str(self):
        kategorija = Kategorija.objects.get(naziv_kategorije="Test Kategorija")
        self.assertEqual(str(kategorija), "Test Kategorija")

    def test_recept_str(self):
        recept = Recept.objects.get(naziv="Test Recept")
        self.assertEqual(str(recept), "Test Recept")

    def test_savjet_str(self):
        savjet = Savjeti.objects.get(naslov="Test Savjet")
        self.assertEqual(str(savjet), "Test Savjet")

    def test_nutritivne_informacije_str(self):
        nutritivne_informacije = NutritivneInformacije.objects.get(recept=self.recept)
        self.assertEqual(str(nutritivne_informacije), "Nutritivne informacije za recept: Test Recept")
