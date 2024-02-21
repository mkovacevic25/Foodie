## factories.py
import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory
class AutorFactory(DjangoModelFactory):
    class Meta:
        model = Autor

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")

class KategorijaFactory(DjangoModelFactory):
    class Meta:
        model = Kategorija

    naziv_kategorije = factory.Faker("word")
    opis_kategorije = factory.Faker("text")

class NutritivneInformacijeFactory(DjangoModelFactory):
    class Meta:
        model = NutritivneInformacije

    recept = factory.Iterator(Recept.objects.all())
    kalorije = factory.Faker('random_int', min=50, max=1000)
    proteini = factory.Faker('random_number', digits=2)
    ugljikohidrati = factory.Faker('random_number', digits=2)
    masti = factory.Faker('random_number', digits=2)


class ReceptFactory(DjangoModelFactory):
    class Meta:
        model = Recept

    naziv = factory.Faker('sentence')
    tezina_izrade = factory.Faker('word')
    vrijeme_izrade = factory.Faker('time')
    opis = factory.Faker('text')
    vrijeme_objave = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    autor_recepta = factory.Iterator(Autor.objects.all())
    kategorija = factory.Iterator(Kategorija.objects.all())
    nutritivne_informacije = factory.RelatedFactory(NutritivneInformacijeFactory, 'recept')


class SavjetiFactory(DjangoModelFactory):
    class Meta:
        model = Savjeti

    naslov = factory.Faker("word")
    tekst_savjeta = factory.Faker('text')
    recept = factory.Iterator(Recept.objects.all())

    @factory.post_generation
    def autori(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for autor in extracted:
                self.autori.add(autor)
        else:
            self.autori.add(AutorFactory())