from django.shortcuts import render
from .models import Genres, Books

# Create your views here.


def get_info(request):
    genres = Genres.objects.all()
    context = {
        'genres' : genres
    }
    return render(request, 'index.html', context=context)


def get_books(request, pk):
    books = Books.objects.filter(genre=pk)
    context = {
        'books' : books
    }
    return render(request, 'books.html', context=context)

def detail(request, pk):
    book = Books.objects.get(pk=pk)
    context = {
        'book' : book
    }
    return render(request, 'detail.html', context=context)

