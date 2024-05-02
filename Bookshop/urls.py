from django.urls import path
from .views import get_info, get_books, detail

urlpatterns = [
    path('', get_info, name='get_info'),
    path('Bookshop<int:pk>', get_books, name='get_books'),
    path('Bookshop/detail/<int:pk>', detail, name='detail')
    ]