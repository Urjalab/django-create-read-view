from django.urls import path

from .views import read_view, create_view

urlpatterns = [
    path('', read_view),
    path('create/', create_view),
]
