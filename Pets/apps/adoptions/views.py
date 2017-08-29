from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def adoptions_main(request):
    return HttpResponse('Adoptions Main Page')
