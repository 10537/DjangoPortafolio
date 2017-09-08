"""Pets URL Configuration

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
from apps.pets.views import pets_main, pets_unlink, PetsList, PetsNew, PetsUpdate, PetsUnlink

urlpatterns = [
    url(r'^$', pets_main, name='PetsMain'),
    url(r'^new$', PetsNew.as_view(), name='PetsForm'),
    url(r'^list$', PetsList.as_view(), name='PetsList'),
    url(r'^edit/(?P<pk>\d+)/$', PetsUpdate.as_view(), name='PetsEdit'),
    url(r'^unlink/(?P<pk>\d+)/$', PetsUnlink.as_view(), name='PetsUnlink'),
]
