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
from apps.adoptions.views import adoptions_main, AdoptionRequestList, AdoptionRequestCreate, AdoptionRequestUpdate,\
    UnlinkAdoptionRequest

urlpatterns = [
    url(r'^$', adoptions_main),
    url(r'^list$', AdoptionRequestList.as_view(), name='AdoptionRequestList'),
    url(r'^new$', AdoptionRequestCreate.as_view(), name='AdoptionRequestNew'),
    url(r'^edit/(?P<pk>\d+)$', AdoptionRequestUpdate.as_view(), name='AdoptionRequestEdit'),
    url(r'^unlink/(?P<pk>\d+)$', UnlinkAdoptionRequest.as_view(), name='AdoptionRequestUnlink'),
]
