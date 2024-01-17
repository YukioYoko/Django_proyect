from django.urls import path
from  . import views

urlpatterns = [
    path('', views.log_in_page, name='log_in'),
]
