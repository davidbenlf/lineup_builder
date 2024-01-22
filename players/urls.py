from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('teste/', views.testedeAPI, name="testedeAPI"),
    path('delete/<int:id>/', views.delete_jogador, name="delete_jogador"),
    path('update/', views.update_jogador, name="update_jogador"),
    path('search/<str:player_name>/', views.search_jogador, name="search_jogador"),
]