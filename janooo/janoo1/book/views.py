from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from .models import *

def list_book(request):
    books=Book.objects.all()
    return render(request,'book/list.html',context={'books':books})
def details_book(request, id):
    context = {'book': Book.objects.get(id=id)}
    return render(request, 'book/details_book.html', context=context)
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect('/book/list')
def add_book(request):
    return render(request,'book/add_book.html')

def update_book(request):
    return render(request,'book/update_book.html')