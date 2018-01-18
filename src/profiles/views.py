# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm

User = get_user_model()

class RegisterView(CreateView):

    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect('/logout/')
        return super(RegisterView,self).dispatch(*args,**kwargs)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    queryset = User.objects.filter(is_active=True)
    template_name = 'profiles/user.html'
    login_url = '/login/'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User,username__iexact=username, is_active=True)

