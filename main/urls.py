from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('register/', views.register, name='register'),
    path('recepti/', views.ReceptList.as_view(), name='recepti'),
    path('dodajte-recept/', views.AddRecept.as_view(), name='add'),
    path('update-recept/<int:pk>', views.UpdateRecept.as_view(), name='update'),
    path('delete-recept/<int:pk>', views.DeleteRecept.as_view(), name='delete'),
    path('dodajte-savjet/', views.AddSavjet.as_view(), name='savjeti'),

]
