from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Personne
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Personne

from django.shortcuts import render
from django.views.generic import ListView
from .models import Personne

class PersonneListView(ListView):
    model = Personne
    template_name = 'personnes/personne_list.html'

    def get_queryset(self):
        personnes = Personne.objects.all()
        return personnes


class PersonneDetailView(DetailView):
    model = Personne
    template_name = 'personne_detail.html'

class PersonneCreateView(CreateView):
    model = Personne
    template_name = 'personnes/personne_new.html'
    fields = ('nom',  'age', 'email')


class PersonneUpdateView(UpdateView):
    model = Personne
    template_name = 'personne_edit.html'
    fields = ('nom', 'email', 'age')

class PersonneDeleteView(DeleteView):
    model = Personne
    template_name = 'personne_delete.html'
    success_url = reverse_lazy('personne_list')
