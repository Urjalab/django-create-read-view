from django.urls import path

from .views import read_view, create_view, update_view

urlpatterns = [
    path('', read_view),
    path('create/', create_view),
    path('update/<int:post_id>/', update_view),
]
