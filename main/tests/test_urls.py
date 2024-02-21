from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import landing_page, register, ReceptList, AddRecept, UpdateRecept, DeleteRecept, AddSavjet

class TestUrls(SimpleTestCase):

    def test_landing_url_resolves(self):
        url = reverse('main:landing')
        self.assertEquals(resolve(url).func, landing_page)

    def test_register_url_resolves(self):
        url = reverse('main:register')
        self.assertEquals(resolve(url).func, register)

    def test_recepti_url_resolves(self):
        url = reverse('main:recepti')
        self.assertEquals(resolve(url).func.view_class, ReceptList)

    def test_add_url_resolves(self):
        url = reverse('main:add')
        self.assertEquals(resolve(url).func.view_class, AddRecept)

    def test_update_url_resolves(self):
        url = reverse('main:update', args=[1])  
        self.assertEquals(resolve(url).func.view_class, UpdateRecept)

    def test_delete_url_resolves(self):
        url = reverse('main:delete', args=[1])  
        self.assertEquals(resolve(url).func.view_class, DeleteRecept)

    def test_savjeti_url_resolves(self):
        url = reverse('main:savjeti')
        self.assertEquals(resolve(url).func.view_class, AddSavjet)
