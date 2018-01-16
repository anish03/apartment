from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from django.db.models import Q
from .models import apartment

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,*args,**kwargs):
        context = super(HomeView,self).get_context_data(*args,**kwargs)
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

    # def get_context_data(self,*args,**kwargs):
    #     context = super(ApartmentDetailView,self).get_context_data(*args, **kwargs)
    #     return context

    def get_object(self,*args,**kwargs):
        apt_id = self.kwargs.get('apt_id')
        obj = get_object_or_404(apartment,pk=apt_id)
        return obj
