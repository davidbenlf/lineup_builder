from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<int:id>/', views.delete_nacionalidade, name="delete_nacionalidade"),
    path('update/', views.update_nacionalidade, name="update_nacionalidade"),
]