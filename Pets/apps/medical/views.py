from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def medical_main(request):
    return HttpResponse('Medical Main Page')
