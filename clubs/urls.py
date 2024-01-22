from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<int:id>/', views.delete_time, name="delete_time"),
    path('update/', views.update_time, name="update_time"),
]