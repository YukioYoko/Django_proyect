from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    HttpResponse('<h1>Pagina principal</h1>')
