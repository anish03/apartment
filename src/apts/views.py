# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'base.html'

class UserView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self,*args,**kwargs):
        context = super(UserView,self).get_context_data(*args,**kwargs)
        return context
