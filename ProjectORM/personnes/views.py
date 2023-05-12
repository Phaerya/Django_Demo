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
    context_object_name = 'personne_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        nom = self.request.GET.get('nom')
        age = self.request.GET.get('age')

        if nom and age:
            queryset = queryset.filter(nom=nom, age=age)
        elif nom:
            queryset = queryset.filter(nom=nom)
        elif age:
            queryset = queryset.filter(age=age)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recherche_terminee'] = any([self.request.GET.get('nom'), self.request.GET.get('age')])
        context['personne_list_complete'] = self.model.objects.all()
        return context



class PersonneDetailView(DetailView):
    model = Personne
    template_name = 'personne_detail.html'

class PersonneCreateView(CreateView):
    model = Personne
    template_name = 'personnes/personne_new.html'
    fields = ('nom',  'age', 'email')
    success_url = '/personnes/'  # Redirige vers la liste des personnes après la création


class PersonneUpdateView(UpdateView):
    model = Personne
    template_name = 'personne_edit.html'
    fields = ('nom', 'email', 'age')

class PersonneDeleteView(DeleteView):
    model = Personne
    template_name = 'personne_delete.html'
    success_url = reverse_lazy('personne_list')
