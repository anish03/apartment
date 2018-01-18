from __future__ import unicode_literals

from collections import defaultdict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from django.db.models import Q
from .models import apartment
from .forms import apartmentForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,*args,**kwargs):
        #context = super(HomeView,self).get_context_data(*args,**kwargs)
        context = defaultdict(list)
        for item in apartment.objects.all():

            context['location'].append([item.name.encode('ascii'),item.lat,item.long])
        print context['location']
        return context


class ApartmentView(ListView):
    #template_name = 'apt/apartment_list.html'
    context_object_name = 'apartments_list'

    def get_queryset(self):
        queryset = apartment.objects.all()
        return queryset

class SearchApartmentView(ListView):
    template_name = 'apt/apartment_list.html'
    context_object_name = 'apartments_list'

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        if slug:
            queryset = apartment.objects.filter(
                Q(city__iexact=slug)
            )
        else:
            queryset = apartment.objects.all()
        return queryset

class ApartmentDetailView(DetailView):
    queryset = apartment.objects.all()


class ApartmentCreateView(LoginRequiredMixin,CreateView):
    form_class = apartmentForm
    template_name = 'apt/apartment_form.html'
    success_url = '/apartments/'
    login_url = '/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user

        return super(ApartmentCreateView, self).form_valid(form)


class ApartmentUpdateView(UpdateView):

    model = apartment
    fields = ['name','city','address','rating','capacity','amenities','lat','long']
    success_url = '/apartments/'
