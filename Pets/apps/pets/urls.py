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
from apps.pets.views import pets_main, pets_form, pets_list, pets_edit, pets_unlink

urlpatterns = [
    url(r'^$', pets_main, name='PetsMain'),
    url(r'^new$', pets_form, name='PetsForm'),
    url(r'^list$', pets_list, name='PetsList'),
    url(r'^edit/(?P<reg_id>\d+)/$', pets_edit, name='PetsEdit'),
    url(r'^unlink/(?P<reg_id>\d+)/$', pets_unlink, name='PetsUnlink'),
]
