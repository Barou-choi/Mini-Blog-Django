from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:pk>/', views.detail_article, name='detail_article'),
    path('article/creer/', views.creer_article, name='creer_article'),
    path('article/<int:pk>/supprimer/', views.supprimer_article, name='supprimer_article'),
] 