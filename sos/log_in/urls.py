from django.urls import path
from  . import views

urlpatterns = [
    path('login/', views.log_in_page, name='log_in'),
]
