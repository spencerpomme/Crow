from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('learn/', views.card, name='learn'),
    path('learn/show/', views.card2, name='learnshow'),
    path('learn/update', views.update_word, name='update'),
    path('gate/', views.gate, name='gate'),
    path('finish/', views.finish, name='finish'),
    path('error/', views.error, name='error'),
]
