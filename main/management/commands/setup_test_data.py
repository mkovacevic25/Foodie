import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Autor, Kategorija, Recept, Savjeti, NutritivneInformacije
from main.factory import (
    AutorFactory,
    KategorijaFactory,
    ReceptFactory,
    SavjetiFactory,
    NutritivneInformacijeFactory
)

NUM_AUTOR = 10
NUM_KATEGORIJE = 3
NUM_RECEPTI = 100
NUM_SAVJETI = 50
NUM_INFORMACIJE = 0

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Autor, Kategorija, Recept]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_AUTOR):
            autor = AutorFactory()

        for _ in range(NUM_KATEGORIJE):
            kategorija = KategorijaFactory()

        for _ in range(NUM_RECEPTI):
            recept = ReceptFactory()
    
        for _ in range(NUM_SAVJETI):
            savjeti = SavjetiFactory()

        for _ in range(NUM_INFORMACIJE):
            informacije = NutritivneInformacijeFactory()