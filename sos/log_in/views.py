from django.shortcuts import render, HttpResponse

# Create your views here.
def log_in_page(request):
    return render(request, "base.html", {})