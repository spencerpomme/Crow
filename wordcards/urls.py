from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('learn/', views.card, name='learn'),
    path('gate/', views.gate, name='gate'),
    path('finish/', views.finish, name='finish')
]
