
from django.shortcuts import render
from   django.http import HttpResponse

def indexa(request):
    return HttpResponse("hello in author page")
