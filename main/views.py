from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Autor, Kategorija, Recept, Savjeti
from .forms import AutorForm, KategorijaForm, ReceptForm, SavjetiForm 
# Create your views here.

@login_required
def landing_page(request):
    return render(request, 'landing.html')

class ReceptList(ListView):
    model = Recept
    form_class=ReceptForm
    template_name = 'recept_list.html'
    context_object_name = 'recept_list'


class AddRecept(CreateView):
    model = Recept
    template_name = 'recept_create.html'
    form_class = ReceptForm
    success_url = reverse_lazy('main:recepti')

class UpdateRecept(UpdateView):
    model = Recept
    template_name = 'recept_update.html'
    form_class = ReceptForm
    success_url = reverse_lazy('main:recepti')


class DeleteRecept(DeleteView):
    model = Recept
    template_name = 'recept_delete.html'
    success_url = reverse_lazy('main:recepti')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recept_list'] = self.get_object()
        return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:landing')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

class PregledSavjeta(ListView):
    model = Recept
    form_class=ReceptForm
    template_name = 'recept_list.html'
    context_object_name = 'recept_list'


class AddSavjet(CreateView):
    model = Savjeti
    template_name = 'savjeti_create.html'
    form_class = SavjetiForm
    success_url = reverse_lazy('main:recepti')
