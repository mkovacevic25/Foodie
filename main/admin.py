from django.contrib import admin
from .models import *

model_list = [Autor, Kategorija, Recept, Savjeti]
admin.site.register(model_list)