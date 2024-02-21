from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Autor, Kategorija, Recept, Savjeti
from main.views import landing_page, ReceptList, AddRecept, UpdateRecept, DeleteRecept, register, PregledSavjeta, AddSavjet
from main.forms import ReceptForm, SavjetiForm
import datetime

class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='testpassword')
        self.autor = Autor.objects.create(ime="Test", prezime="Autor")
        self.kategorija = Kategorija.objects.create(naziv_kategorije="Test Kategorija", opis_kategorije="Opis test kategorije")
        self.recept = Recept.objects.create(naziv="Test Recept", tezina_izrade="Lagano", vrijeme_izrade=datetime.time(0, 30, 0), opis="Opis test recepta", autor_recepta=self.autor, kategorija=self.kategorija)
        self.savjet = Savjeti.objects.create(naslov="Test Savjet", tekst_savjeta="Tekst test savjeta", recept=self.recept)
        
    def test_landing_page(self):
        request = self.factory.get(reverse('landing_page'))
        request.user = self.user
        response = landing_page(request)
        self.assertEqual(response.status_code, 200)
        
    def test_recept_list_view(self):
        request = self.factory.get(reverse('recept_list'))
        request.user = self.user
        response = ReceptList.as_view()(request)
        self.assertEqual(response.status_code, 200)
        
    def test_add_recept_view(self):
        request = self.factory.post(reverse('add_recept'), {'naziv': 'Novi recept', 'tezina_izrade': 'Lagano', 'vrijeme_izrade': datetime.time(0, 30, 0), 'opis': 'Opis novog recepta', 'autor_recepta': self.autor.id, 'kategorija': self.kategorija.id})
        request.user = self.user
        response = AddRecept.as_view()(request)
        self.assertEqual(response.status_code, 302)  
        
    def test_update_recept_view(self):
        request = self.factory.post(reverse('update_recept', kwargs={'pk': self.recept.pk}), {'naziv': 'Novi naziv recepta'})
        request.user = self.user
        response = UpdateRecept.as_view()(request, pk=self.recept.pk)
        self.assertEqual(response.status_code, 302)  # Should redirect after successful update
        
    def test_delete_recept_view(self):
        request = self.factory.post(reverse('delete_recept', kwargs={'pk': self.recept.pk}))
        request.user = self.user
        response = DeleteRecept.as_view()(request, pk=self.recept.pk)
        self.assertEqual(response.status_code, 302)  
        
    def test_register_view(self):
        request = self.factory.post(reverse('register'), {'username': 'newuser', 'password1': 'testpass123', 'password2': 'testpass123'})
        response = register(request)
        self.assertEqual(response.status_code, 302)  

    def test_pregled_savjeta_view(self):
        request = self.factory.get(reverse('pregled_savjeta'))
        request.user = self.user
        response = PregledSavjeta.as_view()(request)
        self.assertEqual(response.status_code, 200)
        
    def test_add_savjet_view(self):
        request = self.factory.post(reverse('add_savjet'), {'naslov': 'Novi savjet', 'tekst_savjeta': 'Tekst novog savjeta', 'recept': self.recept.id})
        request.user = self.user
        response = AddSavjet.as_view()(request)
        self.assertEqual(response.status_code, 302)  
