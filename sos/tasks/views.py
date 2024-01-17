from django.shortcuts import render, HttpResponse

# Create your views here.

def tasks(request):
    HttpResponse('Tasks')

def task(request, id):
    HttpResponse('<h1>Pagina principal</h1>')