# inscription/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.nouvelle_inscription, name='nouvelle_inscription'),
    path('confirmation/<int:pk>/', views.confirmation, name='confirmation'),
    path('telecharger-recu/<int:pk>/', views.telecharger_recu, name='telecharger_recu'),
    path('verifier-statut/', views.verifier_statut, name='verifier_statut'),
]