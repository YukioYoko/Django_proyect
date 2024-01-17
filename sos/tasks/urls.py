from django.urls import path
from  . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('<int:id>/', views.tasks, name='task'),

]
