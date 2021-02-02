from MainApp import views
from django.urls import path

urlpatterns = [
    path(r"", views.addToFavorites),
]
