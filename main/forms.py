from django import forms
from .models import Autor, Kategorija, Recept, Savjeti

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['ime', 'prezime']

class KategorijaForm(forms.ModelForm):
    class Meta:
        model = Kategorija
        fields = ['naziv_kategorije', 'opis_kategorije']

class ReceptForm(forms.ModelForm):
    class Meta:
        model = Recept
        fields = ['naziv', 'tezina_izrade', 'vrijeme_izrade', 'opis', 'vrijeme_objave', 'autor_recepta', 'kategorija']
        widgets = {
            'vrijeme_objave': forms.DateInput(attrs={'type': 'date'})
        }

class SavjetiForm(forms.ModelForm):
    class Meta:
        model = Savjeti
        fields = ['naslov', 'tekst_savjeta', 'autori', 'recept']