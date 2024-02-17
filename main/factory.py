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