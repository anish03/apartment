"""apartment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from apt.views import ApartmentView, SearchApartmentView,ApartmentDetailView,ApartmentCreateView,ApartmentUpdateView,HomeView
from profiles.views import ProfileDetailView, RegisterView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logut'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^$',HomeView.as_view(template_name='home.html'),name='home'),
    url(r'^apartments/$',ApartmentView.as_view(),name='apartments'),
    url(r'^apartments/create/$',ApartmentCreateView.as_view(),name='add'),
    url(r'^apartments/filter/(?P<slug>[\w|\W]+)/$',SearchApartmentView.as_view()),
    #url(r'^apartments/(?P<apt_id>\w+)/$',ApartmentDetailView.as_view()),
    url(r'^apartments/(?P<slug>[\w-]+)/update/$',ApartmentUpdateView.as_view(),name='apartment-detail-update'),
    url(r'^apartments/(?P<slug>[\w-]+)/$',ApartmentDetailView.as_view(),name='apartment-detail'),
    url(r'^profiles/(?P<username>[\w-]+)/$',ProfileDetailView.as_view(),name='profile-detail'),
]

