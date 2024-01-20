from django.shortcuts import render, HttpResponse

# Create your views here.
def admin_login(request):
    return render(request, "admin_login.html", {})