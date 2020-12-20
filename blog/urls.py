from django.urls import path

from .views import read_view, create_view, update_view, delete_view

urlpatterns = [
    path('', read_view, name='home_page'),
    path('create/', create_view, name='create_post'),
    path('update/<int:post_id>/', update_view, name='update_post'),
    path('delete/<int:post_id>/', delete_view, name='delete_post'),
]
