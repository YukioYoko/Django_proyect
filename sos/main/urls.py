from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('repairs', views.repairs, name='repairs'),
]
