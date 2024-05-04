from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import BooksForm
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


def add_books(request):
    form = BooksForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Books:get_info')
    context = {
        'form': form
        }
    return render(request, 'create.html', context=context)



def update_books(request, pk):
    data = Books.objects.get(pk=pk)
    form = BooksForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('Books:get_info')
    context = {
        'form': form
        }
    return render(request, 'update.html', context=context)



def delete_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('Books:get_info')

    return render(request, 'delete.html', {'book': book})
